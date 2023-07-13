from CharacterTemplates.scripts.CharacterItem import ClassItem
from configurator.Entity import Entity


class Cleric(Entity, ClassItem):
	def __init__(self):
		super().__init__()
		self._HitDie = '1d8'
		self._name = 'Cleric'


	def register(self):
		super().register()

	def update(self):
		super().update()
