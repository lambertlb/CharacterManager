class BaseItem:
	def __init__(self):
		self._definition: dict | None = None

	@property
	def definition(self):
		return self._definition

	@definition.setter
	def definition(self, value):
		self._definition = value
  
	def loadData(self, itemData: dict, itemDefinitions: dict):
		pass
