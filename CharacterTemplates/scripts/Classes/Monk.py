from CharacterTemplates.scripts.CharacterItem import ClassItem
from configurator.Entity import Entity


class Monk(Entity, ClassItem):
	def __init__(self):
		super().__init__()
		self._HitDie = '1d8'
		self._name = 'Monk'
		self._description = 'I am a little monkey boy'

	def register(self):
		super().register()

	def update(self):
		super().update()
