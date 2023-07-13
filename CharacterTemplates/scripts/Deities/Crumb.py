from CharacterTemplates.scripts.CharacterItem import CharacterItem
from configurator.Entity import Entity


class Crumb(Entity, CharacterItem):
	def __init__(self):
		Entity.__init__(self)
		CharacterItem.__init__(self)
		self._name = 'Crumb'

	def register(self):
		super().register()

	def update(self):
		super().update()
