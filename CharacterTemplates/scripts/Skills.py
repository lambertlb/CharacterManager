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
		enhancements.addItemThatCanBeEnhanced(self, 'AcrobaticsProficiency', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'AnimalHandlingProficiency', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'ArcanaProficiency', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'AthleticsProficiency', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'DeceptionProficiency', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'HistoryProficiency', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'InsightProficiency', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'IntimidationProficiency', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'InvestigationProficiency', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'MedicineProficiency', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'NatureProficiency', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'PerceptionProficiency', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'PerformanceProficiency', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'PersuasionProficiency', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'ReligionProficiency', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'SleightOfHandProficiency', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'StealthProficiency', 'integer')
		enhancements.addItemThatCanBeEnhanced(self, 'SurvivalProficiency', 'integer')

	def addEnhancements(self, enhancements: Enhancements):
		# enhancements.addEnhancement(self, 'StealthProficiency', "Test", 1)
		# enhancements.addEnhancement(self, 'ArcanaProficiency', "Test", 1)
		# enhancements.addEnhancement(self, 'AcrobaticsProficiency', "Test", 1)
		pass

	def applyEnhancements(self, enhancements: Enhancements):
		character = CharacterServices.getCharacterManager().character
		attributes = character.Attributes
		self.applyEnhancement(enhancements, 'AcrobaticsProficiency', attributes.dexterityBonus)
		self.applyEnhancement(enhancements, 'AnimalHandlingProficiency', attributes.wisdomBonus)
		self.applyEnhancement(enhancements, 'ArcanaProficiency', attributes.intelligenceBonus)
		self.applyEnhancement(enhancements, 'AthleticsProficiency', attributes.strengthBonus)
		self.applyEnhancement(enhancements, 'DeceptionProficiency', attributes.charismaBonus)
		self.applyEnhancement(enhancements, 'HistoryProficiency', attributes.intelligenceBonus)
		self.applyEnhancement(enhancements, 'InsightProficiency', attributes.wisdomBonus)
		self.applyEnhancement(enhancements, 'IntimidationProficiency', attributes.charismaBonus)
		self.applyEnhancement(enhancements, 'InvestigationProficiency', attributes.intelligenceBonus)
		self.applyEnhancement(enhancements, 'MedicineProficiency', attributes.wisdomBonus)
		self.applyEnhancement(enhancements, 'NatureProficiency', attributes.intelligenceBonus)
		self.applyEnhancement(enhancements, 'PerceptionProficiency', attributes.wisdomBonus)
		self.applyEnhancement(enhancements, 'PerformanceProficiency', attributes.charismaBonus)
		self.applyEnhancement(enhancements, 'PersuasionProficiency', attributes.charismaBonus)
		self.applyEnhancement(enhancements, 'ReligionProficiency', attributes.wisdomBonus)
		self.applyEnhancement(enhancements, 'SleightOfHandProficiency', attributes.dexterityBonus)
		self.applyEnhancement(enhancements, 'StealthProficiency', attributes.dexterityBonus)
		self.applyEnhancement(enhancements, 'SurvivalProficiency', attributes.wisdomBonus)
		pass

	def applyEnhancement(self, enhancements, whichEnhancement, howMuch):
		character = CharacterServices.getCharacterManager().character
		proficiencyBonus = character.skillProficiency
		computed = '_computed' + whichEnhancement
		enhances = enhancements.getEnhancements(whichEnhancement)
		attr = howMuch
		for enhance in enhances:
			attr = (enhance.value * proficiencyBonus) + howMuch
		setattr(self, computed, attr)

	def getDataForProperty(self, propertyName, propertyType):
		enhancements = CharacterServices.getEnhancements()
		proficiencyName = propertyName + 'Proficiency'
		enhances = enhancements.getEnhancements(proficiencyName)
		propertyInfo = enhances
		computed = '_computed' + proficiencyName
		propertyData = getattr(self, computed)
		return (propertyName, propertyType, propertyData, propertyInfo)
