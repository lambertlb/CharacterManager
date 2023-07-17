import os
from configurator.ConfigurationManager import ConfigurationManager


class CharacterManagerConfig(ConfigurationManager):
	iniFile = './CharacterManager.ini'
	sourcesKey = 'Sources'
	characterTemplateDirectoryKey = 'CharacterTemplates'
	saveCharacterKey = 'SavedCharacters'
	saveCharacterDirectoryKey = 'SaveCharacterDirectory'
	scriptsKey = 'Scripts'
	scriptsDirectoryKey = 'ScriptsDirectory'

	def __init__(self, configFile=iniFile):
		super().__init__(configFile)

	def setDefaultsIfNeeded(self):
		if not os.path.exists(self.filePath):
			self.config.add_section(CharacterManagerConfig.sourcesKey)
			self.config.set(self.sourcesKey, self.characterTemplateDirectoryKey, './CharacterTemplates')
			self.config.add_section(CharacterManagerConfig.saveCharacterKey)
			self.config.set(self.saveCharacterKey, self.saveCharacterDirectoryKey, './SavedCharacters')
			self.config.add_section(CharacterManagerConfig.scriptsKey)
			self.config.set(self.scriptsKey, self.scriptsDirectoryKey, './CharacterTemplates/scripts')
			self.saveConfiguration()
