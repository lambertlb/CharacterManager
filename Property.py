from BaseItem import BaseItem


class Property(BaseItem):
	def __init__(self):
		super(Property, self).__init__()

	def loadData(self, propertyData: dict, propertyDefinitions: dict):
		self.definition = propertyDefinitions.copy()
		self.attributes = self.definition.get('Attributes')
		if self.attributes:
			self.definition.pop('Attributes')
		assert len(propertyData.keys()) == 1, f'Can only have one key {propertyData}'

		key = list(propertyData.keys())[0]
		data = propertyData[key]
		self.validate(key, data)
		self.getPropertyData(key, data)

	def getPropertyData(self, key, data):
		dataType = 'Text'
		if self.definition:
			dataType = list(self.definition.values())[0]
		if dataType == 'Text':
			setattr(self, key, data)
			return
		elif dataType == 'Numeric':
			setattr(self, key, int(data))
			return
		assert False, f'Unsupported data type {dataType}'

	def validate(self, key, data):
		# add validation code
		pass
