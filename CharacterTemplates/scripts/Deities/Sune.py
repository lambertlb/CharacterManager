from CharacterTemplates.scripts.CharacterItem import CharacterItem
from configurator.Entity import Entity


class SuneScript(Entity, CharacterItem):
	def __init__(self):
		Entity.__init__(self)
		CharacterItem.__init__(self)

	def register(self):
		super(SuneScript, self).register()
		print('Sune registered')

	def update(self):
		super(SuneScript, self).update()
		print('Sune updated')
