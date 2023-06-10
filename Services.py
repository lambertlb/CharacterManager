from ConfigurationManager import ConfigurationManager
from Logger import Logger


class Services:
	_configManager: ConfigurationManager | None = None
	_logger: Logger | None = None

	@staticmethod
	def getConfigurationManager() -> ConfigurationManager:
		return Services._configManager

	@staticmethod
	def setConfigurationManager(value):
		Services._configManager = value

	@staticmethod
	def getLogger() -> Logger:
		return Services._logger

	@staticmethod
	def setLogger(value):
		Services._logger = value
