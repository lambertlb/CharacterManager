import json
from unittest import TestCase
import unittest
from Entity import Entity

from JsonUtils import JsonUtils
from Property import Property


class TestProperties(TestCase):
	@classmethod
	def setUpClass(cls):
		pass

	@classmethod
	def tearDownClass(cls):
		pass

	def test_LoadPropertyWithNoAttributes(self):
		definition = { "Name": {"type": "string"}}
		jsonPropertyData = {"Name": "Fred FlintStone"}
		entity = Entity()
		testProperty = Property()
		testProperty.loadData(entity,jsonPropertyData, definition)
		assert entity.Name
		assert entity.Name == 'Fred FlintStone'
		assert testProperty.definition
		dump = JsonUtils.convertToJson(entity)
		dataAsStr = str(jsonPropertyData).replace("'", '"')
		dumpAsStr = str(dump)
		assert dataAsStr == dumpAsStr

	# def test_LoadPropertyWithAttributes(self):
	# 	definition = {"Name": "Text", "Attributes" : {"Required": "True"}}
	# 	jsonPropertyData = {"Name": "Fred FlintStone"}
	# 	testProperty = Property()
	# 	testProperty.loadData(jsonPropertyData, definition)
	# 	assert testProperty.Name
	# 	assert testProperty.Name == 'Fred FlintStone'
	# 	assert testProperty.definition
	# 	dump = JsonUtils.convertToJson(testProperty)
	# 	dataAsStr = str(jsonPropertyData).replace("'", '"')
	# 	dumpAsStr = str(dump)
	# 	assert dataAsStr == dumpAsStr
	# 	definitionAsStr = '{"Name": "Text"}'
	# 	savedDefinitionAsStr = str(testProperty.definition).replace("'", '"')
	# 	assert definitionAsStr == savedDefinitionAsStr
	# 	assert testProperty.attributes
	# 	savedDefAsStr = str(testProperty.attributes).replace("'", '"')
	# 	assert savedDefAsStr == '{"Required": "True"}'

	# def test_LoadPropertyWithNumeric(self):
	# 	definition = {"Age": "Numeric"}
	# 	jsonPropertyData = {"Age": "22"}
	# 	testProperty = Property()
	# 	testProperty.loadData(jsonPropertyData, definition)
	# 	assert testProperty.Age
	# 	assert testProperty.Age == 22


if __name__ == '__main__':
    unittest.main()
