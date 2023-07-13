from CharacterTemplates.scripts.CharacterItem import CharacterItem
from configurator.Entity import Entity


class Weapon(CharacterItem):
	def __init__(self):
		super().__init__()


class Long_Sword(Entity, Weapon):
	def __init__(self):
		Entity.__init__(self)
		CharacterItem.__init__(self)
		self._name = 'Long Sword'
		self._isWeapon = True
		self._isVersatile = True
		self._rollForDamage = '1d8'
		self._weight = 3
	
	def register(self):
		super().register()

	def update(self):
		super().update()


class Unarmed(Entity, Weapon):
	def __init__(self):
		Entity.__init__(self)
		CharacterItem.__init__(self)
		self._name = 'Unarmed'
		self._isWeapon = True
		self._rollForDamage = '1d3'

	def register(self):
		super().register()

	def update(self):
		super().update()


class Long_Bow(Entity, Weapon):
	def __init__(self):
		Entity.__init__(self)
		CharacterItem.__init__(self)
		self._name = 'Long Bow'
		self._isRange = True
		self._rollForDamage = '1d8'
		self._weight = 2
		self._isHeavy = True
		self._isTwoHanded = True

	def register(self):
		super().register()

	def update(self):
		super().update()
