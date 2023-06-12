from BaseItem import BaseItem
from Collection import Collection
from JsonUtils import JsonUtils


class Entity(BaseItem):

	def __init__(self):
		self._properties = {}
		super(Entity, self).__init__()

	@staticmethod
	def loadJsonFile(path, template):
		data = JsonUtils.loadJsonFile(path)
		entity = Entity()
		entity.readJsonData(data, template)
		pass

	def readJsonData(self, data: dict, template: dict):
		for key in template.keys():
			self.addProperty(data, key, template[key])

	def addProperty(self, data, key, propertyDefinition):
		if key not in data:
			raise Exception(f'Missing key in data key={key}')
		dataForKey = data[key]
		if 'Type' not in propertyDefinition:
			raise Exception(f'Definition missing type {propertyDefinition}')
		propertyType = propertyDefinition['Type']
		if propertyType == 'Collection':
			self.addCollectionData(key, dataForKey, propertyDefinition)
		pass

	def addCollectionData(self, key, collectionData, collectionDefinition):
		collection = Collection()
		setattr(self, key, collection)
		collection.loadData(collectionData, collectionDefinition)
		pass

	def addProperty(self, property):
		self._properties[property.propertyName] = property

	def getName(self):
		if hasattr(self, 'Name'):
			return self.Name
		return None
