import re
from uuid import uuid4

from configurator.Entity import Entity


class CharacterItem:
	"""
	This is the base class for all items that can affect
	things on a character. Specific items can subclass
	this and change its properties to add specific
	effects
	All properties added here should have _ in front,
	so they don't get added to json save file
	"""

	def __init__(self):
		self._uuid = str(uuid4())
		self._name = ''
		self._description = ''
		self._weight = 0
		self._cost = 0
		self.defineWeaponProperties()
		self.defineArmorProperties()

	def defineWeaponProperties(self):
		self._isWeapon = False
		self._weaponProperties = 0
		self._addToAttack = 0
		self._rollForDamage = '1d6'
		self._addToDamage = 0
		self._isWieldedInPrimary = False
		self._isWieldedInSecondary = False

	def defineArmorProperties(self):
		self._isArmor = False
		self._armorProperties = 0
		self._addToAc = 0
		self._isWorn = False
		self._hasMaxDexterityBonus = False
		self._maxDexterityBonus = 0

	def register(self):
		self.handleModifiers(self, self)

	def handleModifiers(self, itemWithModifiers):
		if not hasattr(itemWithModifiers, '$modifiers'):
			return
		modifiers = getattr(itemWithModifiers, '$modifiers')
		for propertyList in list(modifiers.items()):
			propertyName, data = propertyList
			propertyToSet = '_' + propertyName
			if hasattr(self, propertyToSet):
				setattr(self, propertyToSet, data)
		pass

	def saveModifiers(self, itemWithModifiers):
		newMods = {}
		if hasattr(itemWithModifiers, '$modifiers'):
			delattr(itemWithModifiers, '$modifiers')
		modAdded = False
		reference = Entity.createInstanceFromClass(type(self))
		for item in reference.__dict__.items():
			name, value = item
			myValue = getattr(self, name)
			if name != '_uuid' and myValue != value:
				modName = re.sub("_", "", name)
				newMods[modName] = myValue
				modAdded = True
		if modAdded:
			setattr(itemWithModifiers, '$modifiers', newMods)

	def amountToAddToAC(self):
		return self._addToAc

	def computeMaxDexterityBonus(self, currentBonus):
		if self._hasMaxDexterityBonus and self._isWorn and self._maxDexterityBonus < currentBonus:
			return self._maxDexterityBonus
		return currentBonus


class RaceItem(CharacterItem):
	def __init__(self):
		super().__init__()
		self._speed = 30
		self._size = 2


class ClassItem(CharacterItem):
	def __init__(self):
		super().__init__()
		self._HitDie = '1d8'
