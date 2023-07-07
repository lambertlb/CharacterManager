from CharacterTemplates.scripts.CharacterItem import RaceItem
from configurator.Entity import Entity


class HumanScript(Entity, RaceItem):
	def __init__(self):
		Entity.__init__(self)
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
		super(HumanScript, self).register()

	def update(self):
		super(HumanScript, self).update()
