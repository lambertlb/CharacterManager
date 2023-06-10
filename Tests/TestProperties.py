import json
from unittest import TestCase

from JsonUtils import JsonUtils
from Property import Property


class TestCharacterManager(TestCase):
	@classmethod
	def setUpClass(cls):
		pass

	@classmethod
	def tearDownClass(cls):
		pass

	def testLoadPropertyWithNoAttributes(self):
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

