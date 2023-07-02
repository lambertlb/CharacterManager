from CharacterTemplates.scripts.CharacterItem import CharacterItem
from configurator.Entity import Entity


class Weapon(CharacterItem):
	def __init__(self):
		super().__init__()


class Long_Sword(Entity, Weapon):
	def __init__(self):
		Entity.__init__(self)
		Weapon.__init__(self)
		self._isWeapon = True
		self._isVersatile = True
		self._rollForDamage = '1d8'
		self._weight = 3
	
	def register(self):
		super(Long_Sword, self).register()
		print('Long Sword registered')

	def update(self):
		super(Long_Sword, self).update()
		print('Long Sword updated')


class Unarmed(Entity, Weapon):
	def __init__(self):
		Entity.__init__(self)
		Weapon.__init__(self)
		self._isWeapon = True
		self._rollForDamage = '1d3'

	def register(self):
		super(Unarmed, self).register()
		print('Unarmed registered')

	def update(self):
		super(Unarmed, self).update()
		print('Unarmed updated')


class Long_Bow(Entity, Weapon):
	def __init__(self):
		Entity.__init__(self)
		Weapon.__init__(self)
		self._isRange = True
		self._rollForDamage = '1d8'
		self._weight = 2
		self._isHeavy = True
		self._isTwoHanded = True

	def register(self):
		super(Long_Bow, self).register()
		print('Long Bow registered')

	def update(self):
		super(Long_Bow, self).update()
		print('Long Bow updated')
