from main import CharacterManager


from configurator.Services import Services


class CharacterServices(Services):
	_characterManager: CharacterManager | None = None
	_rootWindow = None
	_enhancements = None

	@staticmethod
	def getCharacterManager() -> CharacterManager:
		return CharacterServices._characterManager

	@staticmethod
	def setCharacterManager(value):
		CharacterServices._characterManager = value

	@staticmethod
	def getRootWindow():
		return CharacterServices._rootWindow

	@staticmethod
	def setRootWindow(value):
		CharacterServices._rootWindow = value


	@staticmethod
	def getEnhancements():
		return CharacterServices._enhancements

	@staticmethod
	def setEnhancements(value):
		CharacterServices._enhancements = value
