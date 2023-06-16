from unittest import TestCase
import unittest
from Entity import Entity

from JsonUtils import JsonUtils
from Property import Property


class TestProperties(TestCase):
	testSchema = None
	@classmethod
	def setUpClass(cls):
		TestProperties.testSchema = JsonUtils.loadJsonFile('./test/TestSavedCharacters/CharacterTemplate.json')
		pass

	@classmethod
	def tearDownClass(cls):
		pass

	def test_LoadPropertyWithString(self):
		jsonPropertyData = ("Name", "Fred FlintStone")
		entity = Entity()
		entity._definition = TestProperties.testSchema['properties']['ParameterData']
		Property.loadData(entity,jsonPropertyData)
		assert hasattr(entity, 'Name')
		assert entity.Name == 'Fred FlintStone'

	def test_LoadPropertyWithInteger(self):
		jsonPropertyData = ("Age", 22)
		entity = Entity()
		entity._definition = TestProperties.testSchema['properties']['ParameterData']
		Property.loadData(entity,jsonPropertyData)
		assert hasattr(entity, 'Age')
		assert entity.Age

	def test_LoadPropertyWithNumber(self):
		jsonPropertyData = ("Weight", 110.5)
		entity = Entity()
		entity._definition = TestProperties.testSchema['properties']['ParameterData']
		Property.loadData(entity,jsonPropertyData)
		assert hasattr(entity, 'Weight')
		assert entity.Weight == 110.5

	def test_LoadPropertyWithBoolean(self):
		jsonPropertyData = ("Dead", False)
		entity = Entity()
		entity._definition = TestProperties.testSchema['properties']['ParameterData']
		Property.loadData(entity,jsonPropertyData)
		assert hasattr(entity, 'Dead')
		assert entity.Dead == False

	def test_LoadPropertyWithNull(self):
		jsonPropertyData = ("NullType", None)
		entity = Entity()
		entity._definition = TestProperties.testSchema['properties']['ParameterData']
		Property.loadData(entity,jsonPropertyData)
		assert hasattr(entity, 'NullType')
		assert entity.NullType == None
		dump = JsonUtils.convertToJson(entity)
		assert dump == '{"NullType": null}'

	def test_LoadPropertyMixedArray(self):
		data = [
			"a String",
			33,
			44.4,
			None,
			True
		]
		jsonPropertyData = ("MixedArray", data)
		entity = Entity()
		entity._definition = TestProperties.testSchema
		Property.loadData(entity,jsonPropertyData)
		assert hasattr(entity, 'MixedArray')
		assert isinstance(entity.MixedArray, list)
		assert len(entity.MixedArray) == 5
		assert entity.MixedArray[0] == 'a String'
		assert entity.MixedArray[1] == 33
		assert entity.MixedArray[2] == 44.4
		assert entity.MixedArray[3] is None
		assert entity.MixedArray[4]

	def test_LoadPropertyWithObject(self):
		jsonPropertyData = ( "ParameterData", {
			"Name": "Fred FlintStone",
			"Age": 22,
			"Dead": False,
			"NullType": None,
			"Weight": 110.5
			})
		entity = Entity()
		entity._definition = TestProperties.testSchema
		Property.loadData(entity,jsonPropertyData)
		assert hasattr(entity, 'ParameterData')
		assert isinstance(entity.ParameterData, Entity)
		assert hasattr(entity.ParameterData, 'Name')
		assert hasattr(entity.ParameterData, 'Age')
		assert hasattr(entity.ParameterData, 'Dead')
		assert hasattr(entity.ParameterData, 'NullType')
		assert hasattr(entity.ParameterData, 'Weight')
		assert entity.ParameterData.Name == 'Fred FlintStone'
		assert entity.ParameterData.Age == 22
		assert not entity.ParameterData.Dead
		assert not entity.ParameterData.NullType
		assert entity.ParameterData.Weight == 110.5


if __name__ == '__main__':
	unittest.main()
