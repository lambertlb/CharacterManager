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
		self.defineSkillProficiencies()
		self.defineAttributeProperties()
		self.defineSavingThrowProperties()

	def defineWeaponProperties(self):
		self._isWeapon = False
		self._isAmmunition = False
		self._isFinesse = False
		self._isHeavy = False
		self._isLight = False
		self._isRange = False
		self._isReach = False
		self._isSpecial = False
		self._isThrown = False
		self._isTwoHanded = False
		self._isVersatile = False
		self._addToAttack = 0
		self._rollForDamage = '1d6'
		self._addToDamage = 0
		self._isWieldedInPrimary = False
		self._isWieldedInSecondary = False

	def defineArmorProperties(self):
		self._isArmor = False
		self._isLightArmor = False
		self._isHeavyArmor = False
		self._isMediumArmor = False
		self._isShieldArmor = False
		self._addToAc = 0
		self._isWorn = False
		self._hasMaxDexterityBonus = False
		self._maxDexterityBonus = 0

	def defineSkillProficiencies(self):
		self._addToAcrobatics = 0
		self._addToAnimalHandling = 0
		self._addToArcana = 0
		self._addToAthletics = 0
		self._addToDeception = 0
		self._addToHistory = 0
		self._addToInsight = 0
		self._addToIntimidation = 0
		self._addToInvestigation = 0
		self._addToMedicine = 0
		self._addToNature = 0
		self._addToPerception = 0
		self._addToPerformance = 0
		self._addToPersuasion = 0
		self._addToReligion = 0
		self._addToSleightOfHand = 0
		self._addToStealth = 0
		self._addToSurvival = 0

		# level of Proficiency
		self._levelOfAcrobatics = 0
		self._levelOfAnimalHandling = 0
		self._levelOfArcana = 0
		self._levelOfAthletics = 0
		self._levelOfDeception = 0
		self._levelOfHistory = 0
		self._levelOfInsight = 0
		self._levelOfIntimidation = 0
		self._levelOfInvestigation = 0
		self._levelOfMedicine = 0
		self._levelOfNature = 0
		self._levelOfPerception = 0
		self._levelOfPerformance = 0
		self._levelOfPersuasion = 0
		self._levelOfReligion = 0
		self._levelOfSleightOfHand = 0
		self._levelOfStealth = 0
		self._levelOfSurvival = 0

	def defineAttributeProperties(self):
		self._addToStrength = 0
		self._addToDexterity = 0
		self._addToConstitution = 0
		self._addToIntelligence = 0
		self._addToWisdom = 0
		self._addToCharisma = 0

	def defineSavingThrowProperties(self):
		self._addToStrengthSave = 0
		self._addToDexteritySave = 0
		self._addToConstitutionSave = 0
		self._addToIntelligenceSave = 0
		self._addToWisdomSave = 0
		self._addToCharismaSave = 0

		# level of Proficiency
		self._levelOfStrengthSave = 0
		self._levelOfDexteritySave = 0
		self._levelOfConstitutionSave = 0
		self._levelOfIntelligenceSave = 0
		self._levelOfWisdomSave = 0
		self._levelOfCharismaSave = 0

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
