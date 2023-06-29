from CharacterTemplates.scripts.CharacterItem import CharacterItem
from configurator.Entity import Entity


class CharacterScript(Entity):

	def __init__(self):
		super().__init__()

	def register(self):
		super().register()
		self.update()

	def update(self):
		super().update()
		self.Attributes.update()
		self.computeAC()

	def computeAC(self):
		self._computedAC = 10
		self._computedAC += self.computeDexterityBonus()
		for entity in Entity._allEntities:
			if isinstance(entity, CharacterItem):
				self._computedAC += entity._addToAc
		pass

	def computeDexterityBonus(self):
		maxDexterity = 10
		for entity in Entity._allEntities:
			if isinstance(entity, CharacterItem):
				if entity._hasMaxDexterityBonus and entity._maxDexterityBonus < maxDexterity:
					maxDexterity = entity._maxDexterityBonus
		if hasattr(self.Attributes, "_computedDexterity"):	# might be doing unit test
			dexBonus = self.computeAttributeBonus(self.Attributes._computedDexterity)
		else:
			dexBonus = 0
		if dexBonus < maxDexterity:
			return dexBonus
		return maxDexterity

	def computeAttributeBonus(self, attribute):
		stat = attribute - 10
		return int(stat / 2)