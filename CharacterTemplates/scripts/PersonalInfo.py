from CharacterManagerConfig import CharacterManagerConfig
from configurator.Entity import Entity
from configurator.Services import Services


class PersonalInfo(Entity):
	def __init__(self):
		super().__init__()
		self.Deity = None
		self.Race = None
		self._deityScript = None
		self._raceScript = None

	def register(self):
		super().register()
		if not self._deityScript and self.Deity != '':
			self._deityScript = Entity.instanceFromScript('CharacterTemplates.scripts.Deities.' + self.Deity)
		if self.Deity != '':
			self._deityScript.register()
		if not self._raceScript and self.Race != '':
			self._raceScript = Entity.instanceFromScript('CharacterTemplates.scripts.Races.' + self.Race)
		if self.Race != '':
			self._raceScript.register()

	def update(self):
		super().register()
		if self._raceScript:
			self._raceScript.update()
		if self._deityScript:
			self._deityScript.update()

	def getDataForProperty(self, propertyName, propertyType):
		if propertyName == 'Deity':
			return self.getPropertyDataForDeity(propertyName, propertyType)
		if propertyName == 'Race':
			return self.getPropertyDataForRace(propertyName, propertyType)
		if propertyName == 'Gender':
			return self.getPropertyDataForGender(propertyName, propertyType)
		return super().getDataForProperty(propertyName, propertyType)

	def getPropertyDataForDeity(self, propertyName, propertyType):
		templatePath = Services.getConfigurationManager().getValue(CharacterManagerConfig.sourcesKey,
																	CharacterManagerConfig.characterTemplateDirectoryKey)
		path = templatePath + '/scripts/Deities'
		deities = Entity.getListOfClassesFromDirectory(path, Entity)
		return (propertyName, 'composite', self.Deity, deities)

	def getPropertyDataForRace(self, propertyName, propertyType):
		templatePath = Services.getConfigurationManager().getValue(CharacterManagerConfig.sourcesKey,
																	CharacterManagerConfig.characterTemplateDirectoryKey)
		path = templatePath + '/scripts/Races'
		races = Entity.getListOfClassesFromDirectory(path, Entity)
		return (propertyName, 'composite', self.Race, races)

	def getPropertyDataForGender(self, propertyName, propertyType):
		return (propertyName, 'composite', self.Gender, ['Male', 'Female', 'Neuter'])

	def isValidPropertyChange(self, propertyName, propertyData):
		return True
