import traceback
from unittest import TestCase
import unittest

from jsonschema import Draft7Validator, validate
import pytest

from configurator.Entity import Entity
from configurator.JsonUtils import JsonUtils
from configurator.Services import Services
from test.TestLogger import TestLogger
	
class TestEntities(TestCase):
	testSchema = None
	@classmethod
	def setUpClass(cls):
		Services.setLogger(TestLogger())
		TestEntities.testSchema = JsonUtils.loadJsonSchema('./test/TestSavedCharacters/CharacterTemplate.json')

	@classmethod
	def tearDownClass(cls):
		pass

	def setup_method(self, *args):
		Services.getLogger().clear()
		Entity._allEntities = {} # get rid of garbage from old tests


	def test_EntityDefinitionSetterAndGetter(self):
		entity = Entity()
		entity.definition = {"Item": 1}
		assert entity.definition
		assert entity.definition['Item'] == 1
		assert not Services.getLogger().lastLogged

	def test_EntityGetPropertyDefinition(self):
		entity = Entity()
		entity.definition = TestEntities.testSchema
		pi = entity.getPropertyDefinition('PersonalInformation')
		assert pi
		assert not Services.getLogger().lastLogged

	def test_EntityGetPropertyDefinition2(self):
		entity = Entity()
		entity.definition = {}
		pi = entity.getPropertyDefinition('PersonalInformationA')
		assert not pi		
		assert not Services.getLogger().lastLogged

	def test_EntityLoadScript(self):
		definition = {
			"properties": {
				"$script": {
					"className": "test.TestSavedCharacters.scripts.skills"
				}
			}
		}
		entity = Entity.createEntityFromJsonData({}, definition)
		assert hasattr(entity, 'registered')
		entity.update()
		assert hasattr(entity, 'updated')
		assert not Services.getLogger().lastLogged

	def test_EntityLoadScriptWithException(self):
		definition = {
			"properties": {
				"$script": {
					"className": "test.TestSavedCharacters.scripts.SkillsE"
				}
			}
		}
		logger = Services.getLogger()
		assert not logger.lastLogged
		entity = Entity.createEntityFromJsonData({}, definition)
		assert logger.lastLogged

	def test_EntityLoadData(self):
		result = JsonUtils.loadJsonSchema('./test/TestSavedCharacters/CharacterTemplate.json')
		entity = Entity.loadJsonFile('./test/TestSavedCharacters/Character_1.json', result)
		assert entity
		assert not Services.getLogger().lastLogged

	def test_ValidateTestSchemas(self):
		schemaData = JsonUtils.loadJsonSchema('./test/TestSavedCharacters/CharacterTemplate.json')
		Draft7Validator.check_schema(schemaData)
		data = JsonUtils.loadJsonFile('./test/TestSavedCharacters/Character_1.json')
		validate(data, schemaData)
		assert not Services.getLogger().lastLogged

	def test_ValidateSchemas(self):
		schemaData = JsonUtils.loadJsonSchema('./CharacterTemplates/CharacterTemplate.json')
		Draft7Validator.check_schema(schemaData)
		data = JsonUtils.loadJsonFile('./SavedCharacters/Fred.json')
		validate(data, schemaData)
		assert not Services.getLogger().lastLogged
	
	def test_AllEntities(self):
		assert len(Entity.getEntities()) == 0
		entity = Entity()
		assert len(Entity.getEntities()) == 0
		entity.register()
		assert len(Entity.getEntities()) == 1
		entity.unRegister()
		assert len(Entity.getEntities()) == 0

if __name__ == '__main__':
	unittest.main()
