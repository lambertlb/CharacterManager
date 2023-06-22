from CharacterTemplates.scripts.CharacterItem import CharacterItem
from configurator.Entity import Entity

class Long_Sword(Entity, CharacterItem):
	def __init__(self):
		super().__init__()
		self._isWeapon = True
		self._isVersatile = True
		self._rollForDamage = '1d8'
		self._weight = 3
	
	def register(self):
		super(Long_Sword, self).register()
		print('Long Sword registered')

	def update(self, entityWithProperties):
		super(Long_Sword, self).update()
		print('Long Sword updated')

class Unarmed(Entity, CharacterItem):
	def __init__(self):
		super().__init__()
		self._isWeapon = True
		self._rollForDamage = '1d3'

	def register(self):
		super(Unarmed, self).register()
		print('Unarmed registered')

	def update(self, entityWithProperties):
		super(Unarmed, self).update()
		print('Unarmed updated')

class Long_Bow(Entity, CharacterItem):
	def __init__(self):
		super().__init__()
		self._isRange = True
		self._rollForDamage = '1d8'
		self._weight = 2
		self._isHeavy = True
		self._isTwoHanded = True

	def register(self):
		super(Long_Bow, self).register()
		print('Long Bow registered')

	def update(self, entityWithProperties):
		super(Long_Bow, self).update()
		print('Long Bow updated')
