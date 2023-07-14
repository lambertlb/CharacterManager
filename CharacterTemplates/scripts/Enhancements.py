from enum import Enum
from configurator.Entity import Entity

class EnhancementCategory(Enum):
	Abilities = 0
	Proficiency = 1

class Enhancement():
	mapping = {
		'AbilityEnhance': EnhancementCategory.Abilities,
		'ProficiencyEnhance': EnhancementCategory.Proficiency
	}

	def __init__(self, entity: Entity, category: EnhancementCategory, whichToEnhance, howMuch) -> None:
		self.entity = entity
		self.category = category
		self.whichToEnhance = whichToEnhance
		self.howMuch = howMuch

class Enhancements():
	
	def __init__(self) -> None:
		self.allEnhancements = []
		self.enhancementsByCategory = {}

	def createEnhancement(self, entity: Entity, category: EnhancementCategory, whichToEnhance, howMuch):
		enhancement = Enhancement(entity, category, whichToEnhance, howMuch)
		group = self.enhancementsByCategory.get(category)
		if not group:
			group = []
			self.enhancementsByCategory[category] = group
		group.append(enhancement)
		self.allEnhancements.append(enhancement)
		return enhancement
	
	def getEnhancementsForCategory(self, category):
		group = self.enhancementsByCategory.get(category)
		if not group:
			return []
		return group

	def getAllEnhancements(self):
		return self.allEnhancements
	
	def addEnhancement(self, jsonData: dict, entity):
		keys = jsonData.keys()
		key = list(jsonData.keys())[0]
		data = list(jsonData.values())[0]
		ability = data.get('Ability')
		amount = data.get('Amount')
		category = Enhancement.mapping.get(key)
		if category:
			enhancement = self.createEnhancement(entity, category, ability, amount)
			return enhancement
		return None