import json
from pathlib import Path

import jsonref


class CustomEncoder(json.JSONEncoder):
	def default(self, item):
		itemCopy = item.__dict__.copy()
		for key in item.__dict__.keys():
			if key.startswith('_'):  # don't dump private properties
				itemCopy.pop(key)
		return itemCopy


class JsonUtils:

	@staticmethod
	def loadJsonFile(path):
		with open(path) as f:
			data = f.read()
		data = json.loads(data)
		return data

	@staticmethod
	def saveJsonFile(path, item):
		data = JsonUtils.convertToJson(item)
		with open(path, "wb") as f:
			f.write(data.encode())

	@staticmethod
	def convertToJson(item):
		return json.dumps(item, cls=CustomEncoder)

	@staticmethod
	def loadJsonSchema(path):
		file_a_path = Path(path).absolute()
		with file_a_path.open() as file_a:
			result = jsonref.load(file_a, base_uri=file_a_path.as_uri())
			return result

class JsonTypeHandlers:

	def __init__(self) -> None:
		self.typeMap = {}
		pass

	@property
	def stringHandler(self):
		return self.typeMap.get('string')

	@stringHandler.setter
	def stringHandler(self, value):
		self.typeMap['string'] = value

	@property
	def integerHandler(self):
		return self.typeMap.get('integer')

	@integerHandler.setter
	def integerHandler(self, value):
		self.typeMap['integer'] = value

	@property
	def numberHandler(self):
		return self.typeMap.get('number')

	@numberHandler.setter
	def numberHandler(self, value):
		self.typeMap['number'] = value

	@property
	def booleanHandler(self):
		return self.typeMap.get('boolean')

	@booleanHandler.setter
	def booleanHandler(self, value):
		self.typeMap['boolean'] = value

	@property
	def nullHandler(self):
		return self.typeMap.get('null')

	@nullHandler.setter
	def nullHandler(self, value):
		self.typeMap['null'] = value

	@property
	def arrayHandler(self):
		return self.typeMap.get('array')

	@arrayHandler.setter
	def arrayHandler(self, value):
		self.typeMap['array'] = value

	@property
	def objectHandler(self):
		return self.typeMap.get('object')

	@objectHandler.setter
	def objectHandler(self, value):
		self.typeMap['object'] = value

	def handleType(self, jsonType, propertyName, definition, data, entity):
		handler = self.typeMap.get(jsonType)
		assert handler, f'Handler for {jsonType} not found'
		handler(propertyName, definition, data, entity)