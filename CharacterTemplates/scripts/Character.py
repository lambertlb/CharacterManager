from CharacterTemplates.scripts.CharacterItem import CharacterItem
from configurator.Entity import Entity


class Character(Entity):

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
		self.Skills.update()
		self.updateOffense()
		self.updateDefense()

	def computeAC(self):
		self._computedAC = 10
		self._computedAC += self.Attributes.computeDexterityBonusToAC()
		for entity in Entity._allEntities:
			if isinstance(entity, CharacterItem):
				self._computedAC += entity.amountToAddToAC()
		pass
	
	def updateOffense(self):
		for offense in self.Offense:
			offense.update()

	def updateDefense(self):
		for defense in self.Defense:
			defense.update()