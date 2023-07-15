from CharacterTemplates.scripts.CharacterEntity import CharacterEntity
from CharacterTemplates.scripts.CharacterItem import RaceItem


class Half_Orc(CharacterEntity, RaceItem):
	def __init__(self):
		CharacterEntity.__init__(self)
		RaceItem.__init__(self)
		self._name = 'Half Orc'
		self._addToStrength = 2
		self._addToConstitution = 1
		self._addToIntelligence = -1
		self._size = 2

	def register(self):
		super().register()

	def update(self):
		super().update()
