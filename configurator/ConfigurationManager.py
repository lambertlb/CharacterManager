import configparser


class ConfigurationManager:
	"""
	Class to contain application configuration
	"""

	def __init__(self, configFile='config.ini'):
		self.filePath = configFile
		self.config = configparser.ConfigParser()
		self.setDefaultsIfNeeded()
		self.config.read(self.filePath)
		pass

	def setDefaultsIfNeeded(self):
		pass

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
