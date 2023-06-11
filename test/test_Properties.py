import json
from unittest import TestCase
import unittest

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
		definition = {"Name": "Text"}
		jsonPropertyData = {"Name": "Fred FlintStone"}
		testProperty = Property()
		testProperty.loadData(jsonPropertyData, definition)
		assert testProperty.Name
		assert testProperty.Name == 'Fred FlintStone'
		assert testProperty.definition
		dump = JsonUtils.convertToJson(testProperty)
		dataAsStr = str(jsonPropertyData).replace("'", '"')
		dumpAsStr = str(dump)
		assert dataAsStr == dumpAsStr
		definitionAsStr = str(definition).replace("'", '"')
		savedDefinitionAsStr = str(testProperty.definition).replace("'", '"')
		assert definitionAsStr == savedDefinitionAsStr
		assert not testProperty.attributes

if __name__ == '__main__':
    unittest.main()
