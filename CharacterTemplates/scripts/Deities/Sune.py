from CharacterTemplates.scripts.CharacterEntity import CharacterEntity
from CharacterTemplates.scripts.CharacterItem import CharacterItem


class SuneScript(CharacterEntity, CharacterItem):
	def __init__(self):
		CharacterEntity.__init__(self)
		CharacterItem.__init__(self)
		self._name = 'Sune'

	def register(self):
		super().register()

	def update(self):
		super().update()
