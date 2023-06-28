import traceback
from unittest import TestCase
import unittest

from jsonschema import Draft7Validator, validate

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

	def test_EntityDefinitionSetterAndGetter(self):
		entity = Entity()
		entity.definition = {"Item": 1}
		assert entity.definition
		assert entity.definition['Item'] == 1

	def test_EntityGetPropertyDefinition(self):
		entity = Entity()
		entity.definition = TestEntities.testSchema
		pi = entity.getPropertyDefinition('PersonalInformation')
		assert pi

	def test_EntityGetPropertyDefinition2(self):
		entity = Entity()
		entity.definition = {}
		pi = entity.getPropertyDefinition('PersonalInformationA')
		assert not pi		

	def test_EntityLoadScript(self):
		definition = {
			"properties": {
				"$script": {
					"className": "test.TestSavedCharacters.scripts.Skills"
				}
			}
		}
		entity = Entity.createEntityFromJsonData({}, definition)
		assert hasattr(entity, 'registered')
		entity.update()
		assert hasattr(entity, 'updated')
		pass

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

	def test_ValidateSchemas(self):
		schemaData = JsonUtils.loadJsonSchema('./CharacterTemplates/CharacterTemplate.json')
		Draft7Validator.check_schema(schemaData)
		data = JsonUtils.loadJsonFile('./test/TestSavedCharacters/Character_1.json')
		validate(data, schemaData)


if __name__ == '__main__':
	unittest.main()
