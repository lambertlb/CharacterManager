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
		entity.schema = {"Item": 1}
		assert entity.schema
		assert entity.schema['Item'] == 1
		assert not Services.getLogger().lastLogged

	def test_EntityGetPropertyDefinition(self):
		entity = Entity()
		entity.schema = TestEntities.testSchema
		pi = entity.getPropertyDefinition('PersonalInformation')
		assert pi
		assert not Services.getLogger().lastLogged

	def test_EntityGetPropertyDefinition2(self):
		entity = Entity()
		entity.schema = {}
		pi = entity.getPropertyDefinition('PersonalInformationA')
		assert not pi		
		assert not Services.getLogger().lastLogged

	def test_EntityLoadScript(self):
		definition = {
				"$script": {
					"className": "test.TestSavedCharacters.scripts.Skills"
				}
		}
		entity = Entity.createEntityFromJsonData({}, definition)
		assert hasattr(entity, 'registered')
		entity.update()
		assert hasattr(entity, 'updated')
		assert not Services.getLogger().lastLogged

	def test_EntityLoadScriptWithException(self):
		definition = {
				"$script": {
					"className": "test.TestSavedCharacters.scripts.SkillsE"
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
		data = JsonUtils.loadJsonFile('./SavedCharacters/Fred_FlintStone.json')
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
	
	def test_DataProperty(self):
		entity = Entity()
		assert entity.data == None
		entity.data = "Test"
		assert entity.data == "Test"

	def test_getListOfClassesFromDirectory(self):
		classes = Entity.getListOfClassesFromDirectory("./test/TestSavedCharacters/scripts", Entity)
		assert classes != None
		assert len(classes) == 4

	def test_createFromTemplate(self):
		result = JsonUtils.loadJsonSchema('./test/TestSavedCharacters/CharacterTemplate.json')
		item = Entity.createFromTemplate(result)
		assert item != None
	
	def test_createFromTemplateNoRequired(self):
		result = JsonUtils.loadJsonSchema('./test/TestSavedCharacters/CharacterTemplate.json')
		del result['required']
		item = Entity.createFromTemplate(result)
		assert item != None
	
	def test_propertiesForDisplay(self):
		result = JsonUtils.loadJsonSchema('./test/TestSavedCharacters/CharacterTemplate.json')
		item = Entity.loadJsonFile('./test/TestSavedCharacters/Character_1.json', result)
		attributes = item.Attributes
		assert attributes != None
		displayItems = attributes.propertiesForDisplay()
		assert displayItems != None
		assert len(displayItems) == 6
		name, type, value, obj = displayItems[0]
		assert name == 'Strength'
		assert type == 'integer'
		assert value == 15
		assert obj == None

if __name__ == '__main__':
	unittest.main()
