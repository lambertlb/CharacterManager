from main import CharacterManager


from configurator.Services import Services


class CharacterServices(Services):
	_characterManager: CharacterManager | None = None

	@staticmethod
	def getCharacterManager() -> CharacterManager:
		return CharacterServices._characterManager

	@staticmethod
	def setCharacterManager(value):
		CharacterServices._characterManager = value
