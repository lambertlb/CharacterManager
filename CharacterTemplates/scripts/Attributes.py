from CharacterTemplates.scripts.CharacterItem import CharacterItem
from configurator.Entity import Entity


class Attributes(Entity):

	def __init__(self):
		super().__init__()

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