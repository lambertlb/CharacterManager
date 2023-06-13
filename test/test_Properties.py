import json
from unittest import TestCase
import unittest
from Entity import Entity

from JsonUtils import JsonUtils


class TestProperties(TestCase):
	testSchema = None
	@classmethod
	def setUpClass(cls):
		TestProperties.testSchema = JsonUtils.loadJsonFile('./test/TestSavedCharacters/CharacterSchema.json')
		pass

	@classmethod
	def tearDownClass(cls):
		pass

	def test_LoadPropertyWithString(self):
		jsonPropertyData = {"Name": "Fred FlintStone"}
		entity = Entity()
		entity._definition = TestProperties.testSchema['properties']['ParameterData']
		from Property import Property
		Property.loadData(entity,jsonPropertyData)
		assert hasattr(entity, 'Name')
		assert entity.Name == 'Fred FlintStone'
		dump = JsonUtils.convertToJson(entity)
		dataAsStr = str(jsonPropertyData).replace("'", '"')
		dumpAsStr = str(dump)
		assert dataAsStr == dumpAsStr

	def test_LoadPropertyWithInteger(self):
		jsonPropertyData = {"Age": 22}
		entity = Entity()
		entity._definition = TestProperties.testSchema['properties']['ParameterData']
		from Property import Property
		Property.loadData(entity,jsonPropertyData)
		assert hasattr(entity, 'Age')
		assert entity.Age
		dump = JsonUtils.convertToJson(entity)
		dataAsStr = str(jsonPropertyData).replace("'", '"')
		dumpAsStr = str(dump)
		assert dataAsStr == dumpAsStr

	def test_LoadPropertyWithNumber(self):
		jsonPropertyData = {"Weight": 110.5}
		entity = Entity()
		entity._definition = TestProperties.testSchema['properties']['ParameterData']
		from Property import Property
		Property.loadData(entity,jsonPropertyData)
		assert hasattr(entity, 'Weight')
		assert entity.Weight == 110.5
		dump = JsonUtils.convertToJson(entity)
		dataAsStr = str(jsonPropertyData).replace("'", '"')
		dumpAsStr = str(dump)
		assert dataAsStr == dumpAsStr

	def test_LoadPropertyWithBoolean(self):
		jsonPropertyData = {"Dead": False}
		entity = Entity()
		entity._definition = TestProperties.testSchema['properties']['ParameterData']
		from Property import Property
		Property.loadData(entity,jsonPropertyData)
		assert hasattr(entity, 'Dead')
		assert entity.Dead == False
		dump = JsonUtils.convertToJson(entity)
		dataAsStr = str(jsonPropertyData).replace("'", '"')
		dataAsStr = str(dataAsStr).replace("False", 'false')
		dumpAsStr = str(dump)
		assert dataAsStr == dumpAsStr

	def test_LoadPropertyWithNull(self):
		jsonPropertyData = {"NullType": None}
		entity = Entity()
		entity._definition = TestProperties.testSchema['properties']['ParameterData']
		from Property import Property
		Property.loadData(entity,jsonPropertyData)
		assert hasattr(entity, 'NullType')
		assert entity.NullType == None
		dump = JsonUtils.convertToJson(entity)
		assert dump == '{"NullType": null}'

	def test_LoadPropertyMixedArray(self):
		jsonPropertyData = {"MixedArray": [
			"a String",
			33,
			44.4,
			None,
			True
		]}
		entity = Entity()
		entity._definition = TestProperties.testSchema
		from Property import Property
		Property.loadData(entity,jsonPropertyData)
		assert hasattr(entity, 'MixedArray')
		assert isinstance(entity.MixedArray, list)
		assert len(entity.MixedArray) == 5
		assert entity.MixedArray[0] == 'a String'
		assert entity.MixedArray[1] == 33
		assert entity.MixedArray[2] == 44.4
		assert entity.MixedArray[3] is None
		assert entity.MixedArray[4]


if __name__ == '__main__':
    unittest.main()
