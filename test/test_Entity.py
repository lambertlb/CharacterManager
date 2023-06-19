from unittest import TestCase
import unittest

from Entity import Entity
from JsonUtils import JsonUtils
from Property import Property
from Services import Services
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
		entity = Entity()
		definition = {
			"properties": {
				"$script": {
					"className": "test.TestSavedCharacters.scripts.Skills"
				}
			}
		}
		entity.loadData({},definition)
		assert hasattr(entity, 'registered')
		assert hasattr(entity, '_script')
		entity._script.update(entity)
		assert hasattr(entity, 'updated')
		pass

	def test_EntityLoadScriptWithException(self):
		entity = Entity()
		definition = {
			"properties": {
				"$script": {
					"className": "test.TestSavedCharacters.scripts.SkillsE"
				}
			}
		}
		logger = Services.getLogger()
		assert not logger.lastLogged
		entity.loadData({},definition)
		assert logger.lastLogged

	def test_EntityLoadData(self):
		result = JsonUtils.loadJsonSchema('./test/TestSavedCharacters/CharacterTemplate.json')
		entity = Entity.loadJsonFile('./test/TestSavedCharacters/Character_1.json', result)
		assert entity


if __name__ == '__main__':
	unittest.main()
