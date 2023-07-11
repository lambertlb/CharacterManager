from CharacterTemplates.scripts.CharacterItem import CharacterItem
from configurator.Entity import Entity


class Attributes(Entity):

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

	def update(self):
		super().update()
		self.updateAttributes()

	def updateAttributes(self):
		self._computedStrength = self.Strength
		self._computedDexterity = self.Dexterity
		self._computedConstitution = self.Constitution
		self._computedIntelligence = self.Intelligence
		self._computedWisdom = self.Wisdom
		self._computedCharisma = self.Charisma

		# find items that affect attributes
		for entity in Entity._allEntities:
			if isinstance(entity, CharacterItem) and entity._isWorn:
				self._computedStrength += entity._addToStrength
				self._computedDexterity += entity._addToDexterity
				self._computedConstitution += entity._addToConstitution
				self._computedIntelligence += entity._addToIntelligence
				self._computedWisdom += entity._addToWisdom
				self._computedCharisma += entity._addToCharisma

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
	