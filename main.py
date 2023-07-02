import re
import traceback

from CharacterManagerConfig import CharacterManagerConfig
from configurator.Entity import Entity
from configurator.JsonUtils import JsonUtils
from configurator.Logger import Logger
from configurator.Services import Services


class CharacterManager:

	def __init__(self, templatePath):
		self.character = None
		self.templatePath = templatePath

	def loadCharacter(self, name):
		pathToSavedCharacters = Services.getConfigurationManager().getValue(CharacterManagerConfig.saveCharacterKey,
																			CharacterManagerConfig.saveCharacterDirectoryKey)
		name = re.sub("[^a-zA-Z0-9]", "_", name)
		if 'json' not in name:
			name += '.json'
		characterPath = pathToSavedCharacters + '/' + name
		try:
			self.character = Entity.loadJsonFile(characterPath, self.loadTemplate())
		except (Exception,):
			Services.getLogger().log(traceback.format_exc())

	# noinspection PyMethodMayBeStatic
	def loadTemplate(self):
		result = JsonUtils.loadJsonSchema(self.templatePath + '/CharacterTemplate.json')
		return result

	def saveCharacter(self, name):
		path = Services.getConfigurationManager().getValue(CharacterManagerConfig.saveCharacterKey,
															CharacterManagerConfig.saveCharacterDirectoryKey)
		name = re.sub("[^a-zA-Z0-9]", "_", name)
		if 'json' not in name:
			name += '.json'
		characterPath = path + '/' + name
		try:
			self.character = JsonUtils.saveJsonFile(characterPath, self.character)
		except Exception as ex:
			Services.getLogger().logException(f'Exception while saving character {name}', ex)


if __name__ == "__main__":
	Services.setConfigurationManager(CharacterManagerConfig())
	Services.setLogger(Logger())
	characterManager = CharacterManager('./CharacterTemplates')
	characterManager.loadCharacter('Fred')
	characterManager.saveCharacter('Fred Save')
	pass
