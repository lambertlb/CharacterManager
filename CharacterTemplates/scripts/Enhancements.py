from enum import Enum
from configurator.Entity import Entity

class EnhanceableItem():

	def __init__(self, entity: Entity, name: str, type: str) -> None:
		self.entity: Entity = entity
		self.name: str = name
		self.type: str = type
		self.enhancements = {}

class Enhancements():
	
	def __init__(self) -> None:
		self.enhanceableItems = {}

	def addItemThatCanBeEnhanced(self, entity: Entity, name: str, type: str):
		existing = self.enhanceableItems.get(name)
		assert not existing, f'Ehancement {name} exists'
		existing = EnhanceableItem(entity, name, type)
		self.enhanceableItems[name] = existing
		return existing

