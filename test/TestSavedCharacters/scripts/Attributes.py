from CharacterTemplates.scripts.CharacterEntity import CharacterEntity
from CharacterTemplates.scripts.CharacterItem import CharacterItem
from CharacterTemplates.scripts.Enhancements import EnhancementType, Enhancements
from configurator.Entity import Entity


class Attributes(CharacterEntity):

	def __init__(self):
		super().__init__()
		self.Strength = 0
		self.Dexterity = 0
		self.Constitution = 0
		self.Intelligence = 0
		self.Wisdom = 0
		self.Charisma = 0
		self._computedStrength = 0
		self._computedDexterity = 0
		self._computedConstitution = 0
		self._computedIntelligence = 0
		self._computedWisdom = 0
		self._computedCharisma = 0

	def register(self):
		super().register()

	def addEnhanceables(self, enhancements: Enhancements):
		enhancements.addItemThatCanBeEnhanced(self, 'Strength', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'Dexterity', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'Constitution', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'Intelligence', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'Wisdom', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'Charisma', 'integer')
		pass

	def addEnhancements(self, enhancements: Enhancements):
		# enhancements.addEnhancement(self, 'Strength', "Test", 2)
		# enhancements.addEnhancement(self, 'Strength', "Test", 17, EnhancementType.Absolute)
		# enhancements.addEnhancement(self, 'Strength', "Test", 19, EnhancementType.Absolute)
		# enhancements.addEnhancement(self, 'Strength', "Test", 4)
		pass

	def applyEnhancements(self, enhancements: Enhancements):
		self.applyEnhancement(enhancements, 'Strength')
		self.applyEnhancement(enhancements, 'Dexterity')
		self.applyEnhancement(enhancements, 'Constitution')
		self.applyEnhancement(enhancements, 'Intelligence')
		self.applyEnhancement(enhancements, 'Wisdom')
		self.applyEnhancement(enhancements, 'Charisma')
		pass

	def applyEnhancement(self, enhancements, whichEnhancement):
		computed = '_computed' + whichEnhancement
		attr = getattr(self, whichEnhancement)
		enhances = enhancements.getEnhancements(whichEnhancement)
		hadAbsoluteValue = False
		absoluteValue = 0
		for enhance in enhances:
			if enhance.enhancementType == EnhancementType.Absolute:
				if hadAbsoluteValue:
					if absoluteValue < enhance.value:
						absoluteValue = enhance.value
				else:
					absoluteValue = enhance.value
				attr = absoluteValue
				hadAbsoluteValue = True
			elif not hadAbsoluteValue:
				attr += enhance.value
		setattr(self, computed, attr)
		pass

	@property
	def strengthBonus(self):
		return self.computeAttributeBonus(self._computedStrength)

	@property
	def dexterityBonus(self):
		return self.computeAttributeBonus(self._computedDexterity)

	@property
	def constitutionBonus(self):
		return self.computeAttributeBonus(self._computedConstitution)

	@property
	def intelligenceBonus(self):
		return self.computeAttributeBonus(self._computedIntelligence)

	@property
	def wisdomBonus(self):
		return self.computeAttributeBonus(self._computedWisdom)

	@property
	def charismaBonus(self):
		return self.computeAttributeBonus(self._computedCharisma)

	def computeDexterityBonusToAC(self):
		maxDexterity = 10
		for entity in Entity._allEntities:
			if isinstance(entity, CharacterItem):
				maxDexterity = entity.computeMaxDexterityBonus(maxDexterity)
		dexBonus = self.dexterityBonus
		if dexBonus < maxDexterity:
			return dexBonus
		return maxDexterity

	def computeAttributeBonus(self, attribute):
		stat = attribute - 10
		return int(stat / 2)

	def isValidPropertyChange(self, propertyName, propertyData):
		data = int(propertyData)
		if data > 15 or data < 8:
			return False
		return True

	def getPointCost(self):
		cost = 0
		cost += self.costOfAPoint(self.Strength)
		cost += self.costOfAPoint(self.Dexterity)
		cost += self.costOfAPoint(self.Constitution)
		cost += self.costOfAPoint(self.Intelligence)
		cost += self.costOfAPoint(self.Wisdom)
		cost += self.costOfAPoint(self.Charisma)
		return cost

	def costOfAPoint(self, value):
		if value <= 8:
			return 0
		if value < 14:
			return value - 8
		if value == 14:
			return 7
		return 9
