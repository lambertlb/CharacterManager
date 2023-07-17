from CharacterTemplates.scripts.CharacterEntity import CharacterEntity
from CharacterTemplates.scripts.CharacterItem import CharacterItem


class Weapon(CharacterItem):
	def __init__(self):
		super().__init__()


class Long_Sword(CharacterEntity, Weapon):
	def __init__(self):
		CharacterEntity.__init__(self)
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


class Unarmed(CharacterEntity, Weapon):
	def __init__(self):
		CharacterEntity.__init__(self)
		CharacterItem.__init__(self)
		self._name = 'Unarmed'
		self._isWeapon = True
		self._rollForDamage = '1d3'

	def register(self):
		super().register()

	def update(self):
		super().update()


class Long_Bow(CharacterEntity, Weapon):
	def __init__(self):
		CharacterEntity.__init__(self)
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
