from enum import Enum
from configurator.Entity import Entity

class EnhanceableItem():

	def __init__(self, entity: Entity, name: str, type: str) -> None:
		self.entity: Entity = entity
		self.name: str = name
		self.type: str = type
		self.enhancements = []
	
	def validate(self, data):
		Entity.validate(self.type, data)



class Enhancement():
	def __init__(self, entity: Entity, description: str, value) -> None:
		self.entity: Entity = entity
		self.description: str = description
		self.value = value


class Enhancements():
	
	def __init__(self) -> None:
		self.enhanceableItems = {}

	def clear(self):
		self.enhanceableItems = {}
	
	def addItemThatCanBeEnhanced(self, entity: Entity, name: str, type: str):
		existing = self.enhanceableItems.get(name)
		assert not existing, f'Ehancement {name} exists'
		existing = EnhanceableItem(entity, name, type)
		self.enhanceableItems[name] = existing
		return existing

	def findEnhanceable(self, name: str)  -> None | EnhanceableItem:
		return self.enhanceableItems.get(name)

	def addEnhancement(self, entity: Entity, name: str, description: str, value):
		enhanceable: EnhanceableItem = self.enhanceableItems.get(name)
		assert enhanceable, f'Enhanceable {name} does not exists'
		enhanceable.validate(value)
		enhancement = Enhancement(entity, description, value)
		enhanceable.enhancements.append(enhancement)
		return enhancement
	
	def getEnhancements(self, name: str):
		enhanceable: EnhanceableItem = self.enhanceableItems.get(name)
		assert enhanceable, f'Enhanceable {name} does not exists'
		return enhanceable.enhancements.copy()
