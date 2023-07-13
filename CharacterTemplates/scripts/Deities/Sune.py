from CharacterTemplates.scripts.CharacterItem import CharacterItem
from configurator.Entity import Entity


class SuneScript(Entity, CharacterItem):
	def __init__(self):
		super().__init__()
		self._name = 'Sune'

	def register(self):
		super().register()

	def update(self):
		super().update()
