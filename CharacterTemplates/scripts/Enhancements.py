from enum import Enum

from configurator.Entity import Entity


class EnhancementType(Enum):
	Additive = 0
	Absolute = 2


class EnhanceableItem:

	def __init__(self, entity: Entity, name: str, type: str, validator) -> None:
		self.entity: Entity = entity
		self.name: str = name
		self.type: str = type
		self.validator = validator
		self.enhancements = []

	def addEnhancement(self, entity: Entity, name: str, description: str, value, type):
		enhancement = Enhancement(entity, name, description, value, type)
		Entity.validate(self.type, value)
		if self.validator:
			self.validator(enhancement)
		self.enhancements.append(enhancement)
		return enhancement

	def removeEnhancement(self, enhancement):
		self.enhancements.remove(enhancement)


class Enhancement:
	def __init__(self, entity: Entity, name: str, description: str, value, type: EnhancementType) -> None:
		self.enhanceableName = name
		self.entity: Entity = entity
		self.description: str = description
		self.value = value
		self.enhancementType = type


class Enhancements:

	def __init__(self) -> None:
		self.enhanceableItems = {}

	def clear(self):
		self.enhanceableItems = {}

	def addItemThatCanBeEnhanced(self, entity: Entity, name: str, type: str, validator=None):
		existing = self.enhanceableItems.get(name)
		assert not existing, f'Enhancement {name} exists'
		existing = EnhanceableItem(entity, name, type, validator)
		self.enhanceableItems[name] = existing
		return existing

	def findEnhanceable(self, name: str) -> None | EnhanceableItem:
		return self.enhanceableItems.get(name)

	def addEnhancement(self, entity: Entity, name: str, description: str, value, type=EnhancementType.Additive):
		enhanceable: EnhanceableItem = self.enhanceableItems.get(name)
		assert enhanceable, f'Enhanceable {name} does not exists'
		enhancement = enhanceable.addEnhancement(entity, name, description, value, type)
		return enhancement

	def getEnhancements(self, name: str):
		enhanceable: EnhanceableItem = self.enhanceableItems.get(name)
		assert enhanceable, f'Enhanceable {name} does not exists'
		return enhanceable.enhancements.copy()

	def removeEnhancement(self, enhancement: Enhancement):
		enhanceable: EnhanceableItem = self.enhanceableItems.get(enhancement.enhanceableName)
		assert enhanceable, f'Enhanceable {enhancement.enhanceableName} does not exists'
		enhanceable.removeEnhancement(enhancement)
