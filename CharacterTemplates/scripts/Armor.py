from CharacterTemplates.scripts.CharacterItem import CharacterItem
from configurator.Entity import Entity

class Armor(CharacterItem):
	def __init__(self):
		super().__init__()

class Plate_Mail(Entity, Armor):
	def __init__(self):
		Entity.__init__(self)
		Armor.__init__(self)
		self._isArmor = True
		self._addToAc = 8
		self._weight = 65
		self._hasMaxDexterityBonus = True
		self._maxDexterityBonus = 0
		self._cost = 1500

	def register(self):
		super().register()
		print('Plate Mail registered')

	def update(self):
		super().update()
		print('Plate Mail updated')

class Chain_Mail(Entity, Armor):
	def __init__(self):
		Entity.__init__(self)
		Armor.__init__(self)
		self._isArmor = True
		self._addToAc = 6
		self._weight = 65
		self._hasMaxDexterityBonus = True
		self._maxDexterityBonus = 0
		self._cost = 75

	def register(self):
		super().register()
		print('Plate Mail registered')

	def update(self):
		super().update()
		print('Plate Mail updated')

class Tower_Shield(Entity, Armor):
	def __init__(self):
		Entity.__init__(self)
		Armor.__init__(self)
		self._isArmor = True
		self._addToAc = 2
		self._weight = 6
		self._maxDexterityBonus = 100
		self._cost = 10

	def register(self):
		super().register()
		print('Tower Shield registered')

	def update(self):
		super().update()
		print('Tower Shield updated')
