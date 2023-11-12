from enum import IntEnum
from CharacterServices import CharacterServices
from CharacterTemplates.scripts.CharacterEntity import CharacterEntity
from CharacterTemplates.scripts.Enhancements import Enhancements

class WeaponProperties(IntEnum):
	Finesse = 0
	Heavy = 1
	Light = 2
	Ranged = 4
	Reach = 8
	Thrown = 16
	TwoHanded = 32
	Versatile = 64


class Offense(CharacterEntity):

	def __init__(self):
		super().__init__()

	def register(self):
		super().register()

	def addEnhanceables(self, enhancements: Enhancements):
		enhancements.addItemThatCanBeEnhanced(self, 'FinesseWeapon', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'HeavyWeapon', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'LightWeapon', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'RangeWeapon', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'ReachWeapon', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'ThrownWeapon', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'TwoHandedWeapon', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'VersatileWeapon', 'integer')

	def applyEnhancements(self, enhancements: Enhancements):
		character = CharacterServices.getCharacterManager().character
		attributes = character.Attributes
		self.applyEnhancement(enhancements, 'Finesse', max(attributes.dexterityBonus,attributes.strengthBonus))
		self.applyEnhancement(enhancements, 'Heavy', attributes.strengthBonus)
		self.applyEnhancement(enhancements, 'Light', max(attributes.dexterityBonus,attributes.strengthBonus))
		self.applyEnhancement(enhancements, 'Range', attributes.dexterityBonus)
		self.applyEnhancement(enhancements, 'Reach', attributes.strengthBonus)
		self.applyEnhancement(enhancements, 'Thrown', max(attributes.dexterityBonus,attributes.strengthBonus))
		self.applyEnhancement(enhancements, 'TwoHanded', attributes.strengthBonus)
		self.applyEnhancement(enhancements, 'Versatile', max(attributes.dexterityBonus,attributes.strengthBonus))
		pass

	def applyEnhancement(self, enhancements, whichEnhancement, howMuch):
		character = CharacterServices.getCharacterManager().character
		proficiencyBonus = character.skillProficiency
		enhances = enhancements.getEnhancements(whichEnhancement+'Weapon')
		attr = howMuch
		for enhance in enhances:
			attr = (enhance.value * proficiencyBonus) + howMuch
		setattr(self, '_'+whichEnhancement, attr)
