from CharacterTemplates.scripts.CharacterItem import CharacterItem
from configurator.Entity import Entity


class SuneScript(Entity, CharacterItem):
	def __init__(self):
		Entity.__init__(self)
		CharacterItem.__init__(self)
		self._name = 'Sune'

	def register(self):
		super(SuneScript, self).register()

	def update(self):
		super(SuneScript, self).update()
