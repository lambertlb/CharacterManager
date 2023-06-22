from CharacterTemplates.scripts.CharacterItem import CharacterItem
from configurator.Entity import Entity

class Plate_Mail(Entity, CharacterItem):
	def __init__(self):
		super().__init__()
		self._isArmor = True
		self._addToAc = 8
		self._weight = 65
		self._maxDexterityBonus = 0
		self._cost = 1500

	def register(self):
		super(Plate_Mail, self).register()
		print('Plate Mail registered')

	def update(self):
		super(Plate_Mail, self).update()
		print('Plate Mail updated')

class Tower_Shield(Entity, CharacterItem):
	def __init__(self):
		super().__init__()
		self._isArmor = True
		self._addToAc = 2
		self._weight = 6
		self._maxDexterityBonus = 100
		self._cost = 10

	def register(self):
		super(Tower_Shield, self).register()
		print('Tower Shield registered')

	def update(self):
		super(Tower_Shield, self).update()
		print('Tower Shield updated')
