from BaseItem import BaseItem
from JsonUtils import JsonUtils


class Entity(BaseItem):

	def __init__(self):
		super(Entity, self).__init__()

	@staticmethod
	def loadJsonFile(path, template):
		data = JsonUtils.loadJsonFile(path)
		entity = Entity()
		entity.definition = template
		entity.loadData(data, template)
		return entity

	def loadData(self, entityData, dataDefinition):
		self.definition = dataDefinition
		for parameter in list(entityData.items()):
			from Property import Property
			Property.loadData(self, parameter)

	def getPropertyDefinition(self, propertyName):
		if self._definition:
			properties = self._definition.get('properties')
			if properties:
				return properties.get(propertyName)
		return None