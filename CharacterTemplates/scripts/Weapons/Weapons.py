from CharacterTemplates.scripts.CharacterEntity import CharacterEntity
from CharacterTemplates.scripts.CharacterItem import CharacterItem
from CharacterTemplates.scripts.Offense import WeaponProperties


class Weapon(CharacterItem):
	def __init__(self):
		super().__init__()


class Long_Sword(CharacterEntity, Weapon):
	def __init__(self):
		CharacterEntity.__init__(self)
		CharacterItem.__init__(self)
		self._name = 'Long Sword'
		self._isWeapon = True
		self._weaponProperties = WeaponProperties.Versatile
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
		self._weaponProperties = WeaponProperties.Heavy & WeaponProperties.TwoHanded & WeaponProperties.Ranged
		self._rollForDamage = '1d8'
		self._weight = 2

	def register(self):
		super().register()

	def update(self):
		super().update()
