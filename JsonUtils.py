import json


class CustomEncoder(json.JSONEncoder):
	def default(self, item):
		itemCopy = item.__dict__.copy()
		for key in item.__dict__.keys():
			if key.startswith('_'): # don't dump private properties
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

	def loadScript(path):
		with open(path) as f:
			data = f.read()
		return data
	
	@staticmethod
	def convertToJson(item):
		return json.dumps(item, cls=CustomEncoder)
