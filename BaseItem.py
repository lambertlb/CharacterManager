class BaseItem:
	def __init__(self):
		self._attributes: dict | None = None
		self._definition: dict | None = None
		self._properties: dict | None = None

	@property
	def definition(self):
		return self._definition

	@definition.setter
	def definition(self, value):
		self._definition = value

	@property
	def attributes(self):
		return self._attributes

	@attributes.setter
	def attributes(self, value):
		self._attributes = value

	@property
	def properties(self):
		return self._properties

	@properties.setter
	def properties(self, new_properties):
		self._properties = new_properties
  
	def loadData(self, propertyData: dict, propertyDefinitions: dict):
		pass
