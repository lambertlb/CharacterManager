from enum import Enum
from CharacterServices import CharacterServices
from CharacterTemplates.scripts.CharacterEntity import CharacterEntity
from CharacterTemplates.scripts.Enhancements import Enhancements

class ArmorProperties(Enum):
	No = 0
	Light = 1
	Medium = 2
	Heavy = 4
	Shield = 8


class Defense(CharacterEntity):

	def __init__(self):
		super().__init__()

	def register(self):
		super().register()

	def addEnhanceables(self, enhancements: Enhancements):
		enhancements.addItemThatCanBeEnhanced(self, 'NoArmor', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'LightArmor', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'MediumArmor', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'HeavyArmor', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'ShieldArmor', 'integer')

	def applyEnhancements(self, enhancements: Enhancements):
		character = CharacterServices.getCharacterManager().character
		attributes = character.Attributes
		self.applyEnhancement(enhancements, 'No', attributes.dexterityBonus)
		self.applyEnhancement(enhancements, 'Light', attributes.dexterityBonus)
		self.applyEnhancement(enhancements, 'Medium', attributes.dexterityBonus)
		self.applyEnhancement(enhancements, 'Heavy', 0)
		self.applyEnhancement(enhancements, 'Shield', 0)
		pass

	def applyEnhancement(self, enhancements, whichEnhancement, howMuch):
		character = CharacterServices.getCharacterManager().character
		enhances = enhancements.getEnhancements(whichEnhancement+'Armor')
		attr = 0
		for enhance in enhances:
			attr = howMuch
		setattr(self, '_'+whichEnhancement, attr)
