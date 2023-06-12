from BaseItem import BaseItem


class Property(BaseItem):
	def __init__(self):
		self.propertyName = None
		super(Property, self).__init__()

	def loadData(self, where, propertyData: dict, propertyDefinitions: dict):
		definition = propertyDefinitions.copy()
		assert len(propertyData.keys()) == 1, f'Can only have one key {propertyData}'

		key = list(propertyData.keys())[0]
		data = propertyData[key]
		self._definition = definition.get(key)
		self.validate(key, data)
		self.getPropertyData(where, key, data)

	def getPropertyData(self, where, key, data):
		self.propertyName = key
		dataType = 'string'
		if self.definition:
			dataType = list(self.definition.values())[0]
		if dataType == 'string':
			setattr(where, key, data)
			return
		elif dataType == 'integer':
			setattr(where, key, int(data))
			return
		assert False, f'Unsupported data type {dataType}'

	def validate(self, key, data):
		# add validation code
		pass
