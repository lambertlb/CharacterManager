from CharacterTemplates.scripts.CharacterItem import CharacterItem
from configurator.Entity import Entity


class CharacterScript(Entity):

	def __init__(self):
		super().__init__()
		self._computedAC = 10
		self.Attributes = None

	def register(self):
		super().register()
		self.update()

	def update(self):
		super().update()
		self.Attributes.update()
		self.computeAC()

	def computeAC(self):
		self._computedAC = 10
		self._computedAC += self.Attributes.computeDexterityBonusToAC()
		for entity in Entity._allEntities:
			if isinstance(entity, CharacterItem):
				self._computedAC += entity.amountToAddToAC()
		pass
	