import configparser
import os


class ConfigurationManager:
	"""
	Class to contain application configuration
	"""

	iniFile = './CharacterManager.ini'
	sourcesKey = 'Sources'
	characterTemplateDirectoryKey = 'CharacterTemplates'
	saveCharacterKey = 'SavedCharacters'
	saveCharacterDirectoryKey = 'SaveCharacterDirectory'
	scriptsKey = 'Scripts'
	scriptsDirectoryKey = 'ScriptsDirectory'

	def __init__(self, configFile=iniFile):
		self.filePath = configFile
		self.config = configparser.ConfigParser()
		self.setDefaultsIfNeeded()
		self.config.read(self.filePath)
		pass

	def setDefaultsIfNeeded(self):
		if not os.path.exists(self.filePath):
			self.config.add_section(ConfigurationManager.sourcesKey)
			self.config.set(self.sourcesKey, self.characterTemplateDirectoryKey, './CharacterTemplates')
			self.config.add_section(ConfigurationManager.saveCharacterKey)
			self.config.set(self.saveCharacterKey, self.saveCharacterDirectoryKey, './SavedCharacters')
			self.config.add_section(ConfigurationManager.scriptsKey)
			self.config.set(self.scriptsKey, self.scriptsDirectoryKey, './CharacterTemplates/scripts')
			self.saveConfiguration()

	def saveConfiguration(self):
		with open(self.filePath, 'w') as configfile:
			self.config.write(configfile)

	def setValue(self, section, key, value):
		if not self.config.__contains__(section):
			self.config.add_section(section)
		self.config.set(section, key, value)
		self.saveConfiguration()

	def getValue(self, section, key, default=None):
		if not self.config.__contains__(section):
			return default
		sec = self.config[section]
		if not sec.__contains__(key):
			return default
		return sec[key]
