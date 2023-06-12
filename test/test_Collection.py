from unittest import TestCase

from Collection import Collection


class TestCollection(TestCase):
	@classmethod
	def setUpClass(cls):
		pass

	@classmethod
	def tearDownClass(cls):
		pass

	def test_LoadCollection(self):
		definition = {
			"Contains": "Property",
			"DataDefinitions": {
				"Name":	{ "Name" : "Text", "Attributes" : {"Required" : "True"} },
				"Age": { "Age" : "Numeric",  "Attributes" : {"Required" : "False"}},
				"Sex": { "Sex" : "Text",  "Attributes" : {"Required" : "True"}}
			},
			"Attributes" : {"AllowAddWithoutDefinition":  "True"}
		}
		collectionData = {
				"Name": "Fred FlintStone",
				"Age": "22"
			}
		testCollection = Collection()
		# testCollection.loadData(collectionData, definition)
		pass