from CharacterTemplates.scripts.CharacterEntity import CharacterEntity
from CharacterTemplates.scripts.CharacterItem import RaceItem


class Human(CharacterEntity, RaceItem):
	def __init__(self):
		CharacterEntity.__init__(self)
		RaceItem.__init__(self)
		self._name = 'Human'
		self._addToStrength = 1
		self._addToDexterity = 1
		self._addToConstitution = 1
		self._addToIntelligence = 1
		self._addToWisdom = 1
		self._addToCharisma = 1
		self._size = 2

	def register(self):
		super().register()

	def update(self):
		super().update()
