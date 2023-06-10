class BaseItem:
	def __init__(self):
		self._attributes: dict | None = None
		self._definition: dict | None = None

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

	def loadData(self, propertyData: dict, propertyDefinitions: dict):
		raise Exception("Child Class must implement loadData Method")