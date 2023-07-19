from CharacterServices import CharacterServices
from CharacterTemplates.scripts.CharacterEntity import CharacterEntity
from CharacterTemplates.scripts.Enhancements import Enhancements


class Skills(CharacterEntity):
	def __init__(self):
		super().__init__()

	def register(self):
		super().register()
		pass

	def update(self):
		super().update()
		pass

	def addEnhanceables(self, enhancements: Enhancements):
		enhancements.addItemThatCanBeEnhanced(self, 'Acrobatics', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'AnimalHandling', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'Arcana', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'Athletics', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'Deception', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'History', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'Insight', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'Intimidation', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'Investigation', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'Medicine', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'Nature', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'Perception', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'Performance', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'Persuasion', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'Religion', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'SleightOfHand', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'Stealth', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'Survival', 'integer')

	def addEnhancements(self, enhancements: Enhancements):
		# enhancements.addEnhancement(self, 'Stealth', "Test", 1)
		# enhancements.addEnhancement(self, 'Arcana', "Test", 1)
		# enhancements.addEnhancement(self, 'Acrobatics', "Test", 1)
		pass

	def applyEnhancements(self, enhancements: Enhancements):
		character = CharacterServices.getCharacterManager().character
		attributes = character.Attributes
		self.applyEnhancement(enhancements, 'Acrobatics', attributes.dexterityBonus)
		self.applyEnhancement(enhancements, 'AnimalHandling', attributes.wisdomBonus)
		self.applyEnhancement(enhancements, 'Arcana', attributes.intelligenceBonus)
		self.applyEnhancement(enhancements, 'Athletics', attributes.strengthBonus)
		self.applyEnhancement(enhancements, 'Deception', attributes.charismaBonus)
		self.applyEnhancement(enhancements, 'History', attributes.intelligenceBonus)
		self.applyEnhancement(enhancements, 'Insight', attributes.wisdomBonus)
		self.applyEnhancement(enhancements, 'Intimidation', attributes.charismaBonus)
		self.applyEnhancement(enhancements, 'Investigation', attributes.intelligenceBonus)
		self.applyEnhancement(enhancements, 'Medicine', attributes.wisdomBonus)
		self.applyEnhancement(enhancements, 'Nature', attributes.intelligenceBonus)
		self.applyEnhancement(enhancements, 'Perception', attributes.wisdomBonus)
		self.applyEnhancement(enhancements, 'Performance', attributes.charismaBonus)
		self.applyEnhancement(enhancements, 'Persuasion', attributes.charismaBonus)
		self.applyEnhancement(enhancements, 'Religion', attributes.wisdomBonus)
		self.applyEnhancement(enhancements, 'SleightOfHand', attributes.dexterityBonus)
		self.applyEnhancement(enhancements, 'Stealth', attributes.dexterityBonus)
		self.applyEnhancement(enhancements, 'Survival', attributes.wisdomBonus)
		pass

	def applyEnhancement(self, enhancements, whichEnhancement, howMuch):
		character = CharacterServices.getCharacterManager().character
		proficiencyBonus = character.skillProficiency
		enhances = enhancements.getEnhancements(whichEnhancement)
		attr = howMuch
		for enhance in enhances:
			attr = (enhance.value * proficiencyBonus) + howMuch
		setattr(self, whichEnhancement, attr)

	def getDataForProperty(self, propertyName, propertyType):
		enhancements = CharacterServices.getEnhancements()
		enhances = enhancements.getEnhancements(propertyName)
		propertyInfo = enhances
		propertyData = getattr(self, propertyName)
		return (propertyName, propertyType, propertyData, propertyInfo)
