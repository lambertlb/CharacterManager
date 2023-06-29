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
			if isinstance(entity, CharacterItem):
				self._computedStrength += entity._addToStrength
				self._computedDexterity += entity._addToDexterity
				self._computedConstitution += entity._addToConstitution
				self._computedIntelligence += entity._addToIntelligence
				self._computedWisdom += entity._addToWisdom
				self._computedCharisma += entity._addToCharisma
		pass
