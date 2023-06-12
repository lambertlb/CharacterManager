from BaseItem import BaseItem
from Property import Property


class Collection(BaseItem):
	def __init__(self):
		super(Collection, self).__init__()
		self.collectionData = {}
		self.collectionType = None

	def loadData(self, collectionData, collectionDefinition):
		if 'Contains' not in collectionDefinition:
			raise Exception(f'Collection missing Contains {collectionDefinition}')
		self.collectionType = collectionDefinition['Contains']
		dataDefinition = None
		if 'DataDefinitions' in collectionDefinition:
			dataDefinition = collectionDefinition['DataDefinitions']
		self.buildCollection(collectionData, dataDefinition)
		pass

	def buildCollection(self, collectionData, dataDefinition):
		definitions = dataDefinition.copy()
		for infor in collectionData.values():
			contained = self.getCollectionInstance()
			contained.loadData(infor, definitions)
			self.collectionData[contained.getName()] = contained
		pass

	def getCollectionInstance(self):
		if self.collectionType == 'Entity':
			from Entity import Entity
			return Entity()
		if self.collectionType == 'Collection':
			return Collection()
		if self.collectionType == 'Property':
			return Property()
		raise Exception(f'Invalid collection type {self.collectionType}')
