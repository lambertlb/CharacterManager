from unittest import TestCase
import unittest

import pytest
from configurator.Entity import Entity

from configurator.JsonUtils import JsonUtils


class TestProperties(TestCase):
	testSchema = None
	@classmethod
	def setUpClass(cls):
		TestProperties.testSchema = JsonUtils.loadJsonSchema('./test/TestSavedCharacters/CharacterTemplate.json')

	@classmethod
	def tearDownClass(cls):
		pass

	def test_LoadPropertyWithString(self):
		jsonPropertyData = ("Name", "Fred FlintStone")
		entity = Entity()
		entity._definition = TestProperties.testSchema['properties']['PersonalInformation']
		Entity.loadPropertyData(entity, jsonPropertyData)
		assert hasattr(entity, 'Name')
		assert entity.Name == 'Fred FlintStone'

	def test_LoadPropertyWithInteger(self):
		jsonPropertyData = ("Age", 22)
		entity = Entity()
		entity._definition = TestProperties.testSchema['properties']['PersonalInformation']
		Entity.loadPropertyData(entity,jsonPropertyData)
		assert hasattr(entity, 'Age')
		assert entity.Age

	def test_LoadPropertyWithNumber(self):
		jsonPropertyData = ("Weight", 110.5)
		entity = Entity()
		entity._definition = TestProperties.testSchema['properties']['PersonalInformation']
		Entity.loadPropertyData(entity,jsonPropertyData)
		assert hasattr(entity, 'Weight')
		assert entity.Weight == 110.5

	def test_LoadPropertyWithBoolean(self):
		jsonPropertyData = ("Dead", False)
		entity = Entity()
		entity.definition = {
			"properties": {
				"Dead": {
					"type": "boolean"
				}
			}}
		Entity.loadPropertyData(entity,jsonPropertyData)
		assert hasattr(entity, 'Dead')
		assert entity.Dead == False

	def test_LoadPropertyWithNull(self):
		jsonPropertyData = ("NullType", None)
		entity = Entity()
		entity.definition = {
			"properties": {
				"NullType": {
					"type": "null"
				}
			}}
		Entity.loadPropertyData(entity,jsonPropertyData)
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
		entity.definition = {
			"properties": {
				"MixedArray": {
					"type": "array",
					"items": 
						{ "type": ["string", "integer", "number", "null", "boolean"] }
				}
			}}
		Entity.loadPropertyData(entity,jsonPropertyData)
		assert hasattr(entity, 'MixedArray')
		assert isinstance(entity.MixedArray, list)
		assert len(entity.MixedArray) == 5
		assert entity.MixedArray[0] == 'a String'
		assert entity.MixedArray[1] == 33
		assert entity.MixedArray[2] == 44.4
		assert entity.MixedArray[3] is None
		assert entity.MixedArray[4]

	def test_LoadPropertySingleTypeArray(self):
		data = [
			1,
			2,
			3,
			4,
			5
		]
		jsonPropertyData = ("SingleType", data)
		entity = Entity()
		entity.definition = {
			"properties": {
				"SingleType": {
					"type": "array",
					"items": 
						{ "type": "integer" }
				}
			}}
		Entity.loadPropertyData(entity,jsonPropertyData)
		assert hasattr(entity, 'SingleType')
		assert isinstance(entity.SingleType, list)
		assert len(entity.SingleType) == 5
		assert entity.SingleType[0] == 1
		assert entity.SingleType[1] == 2
		assert entity.SingleType[2] == 3
		assert entity.SingleType[3] == 4
		assert entity.SingleType[4] == 5

	def test_LoadPropertySingleTypeObjectArray(self):
		data = [
			{"Object1": 1},
			{"Object2": 2},
			{"Object3": 3},
			{"Object4": 4},
			{"Object5": 5}
		]
		jsonPropertyData = ("ObjectType", data)
		entity = Entity()
		entity.definition = {
			"properties": {
				"ObjectType": {
					"type": "array",
					"items": 
						{ "type": "object",
							"properties": {
									"Object1": {
										"type": "integer"
									},
									"Object2": {
										"type": "integer"
									},
									"Object3": {
										"type": "integer"
									},
									"Object4": {
										"type": "integer"
									},
									"Object5": {
										"type": "integer"
									}
       						}
					}
			}}}
		Entity.loadPropertyData(entity,jsonPropertyData)
		assert hasattr(entity, 'ObjectType')
		assert isinstance(entity.ObjectType, list)
		assert len(entity.ObjectType) == 5
		assert entity.ObjectType[0].Object1 == 1
		assert entity.ObjectType[1].Object2 == 2
		assert entity.ObjectType[2].Object3 == 3
		assert entity.ObjectType[3].Object4 == 4
		assert entity.ObjectType[4].Object5 == 5

	def test_LoadPropertyWithObject(self):
		jsonPropertyData = ( "PersonalInformation", {
			"Name": "Fred FlintStone",
			"Age": 22,
			"Dead": False,
			"NullType": None,
			"Weight": 110.5
			})
		entity = Entity()
		entity._definition = TestProperties.testSchema
		Entity.loadPropertyData(entity,jsonPropertyData)
		assert hasattr(entity, 'PersonalInformation')
		assert isinstance(entity.PersonalInformation, Entity)
		assert hasattr(entity.PersonalInformation, 'Name')
		assert hasattr(entity.PersonalInformation, 'Age')
		assert hasattr(entity.PersonalInformation, 'Dead')
		assert hasattr(entity.PersonalInformation, 'NullType')
		assert hasattr(entity.PersonalInformation, 'Weight')
		assert entity.PersonalInformation.Name == 'Fred FlintStone'
		assert entity.PersonalInformation.Age == 22
		assert not entity.PersonalInformation.Dead
		assert not entity.PersonalInformation.NullType
		assert entity.PersonalInformation.Weight == 110.5
		
	def	test_ValidateRaisesException(self):
		with pytest.raises(Exception):
			Entity.validate('boolean', 22)

		
	def	test_ValidateIntegerIsNumber(self):
		Entity.validate('number', 22)


if __name__ == '__main__':
	unittest.main()
