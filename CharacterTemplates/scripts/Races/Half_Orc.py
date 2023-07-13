from CharacterTemplates.scripts.CharacterItem import RaceItem
from configurator.Entity import Entity


class Half_Orc(Entity, RaceItem):
	def __init__(self):
		super().__init__()
		self._name = 'Half Orc'
		self._addToStrength = 2
		self._addToConstitution = 1
		self._addToIntelligence = -1
		self._size = 2

	def register(self):
		super().register()

	def update(self):
		super().update()
