import re
import traceback

from ConfigurationManager import ConfigurationManager
from Entity import Entity
from JsonUtils import JsonUtils
from Logger import Logger
from Services import Services


class CharacterManager:

	def __init__(self, templatePath):
		self.character = None
		self.templatePath = templatePath
		self.characterTemplate = self.loadTemplate()
		pass

	def loadCharacter(self, name):
		path = Services.getConfigurationManager().getValue(ConfigurationManager.saveCharacterKey,
										ConfigurationManager.saveCharacterDirectoryKey)
		name = re.sub("[^a-zA-Z0-9]", "_", name)
		if 'json' not in name:
			name += '.json'
		characterPath = path + '/' + name
		try:
			self.character = Entity.loadJsonFile(characterPath, self.characterTemplate)
		except (Exception,):
			Services.getLogger().log(traceback.format_exc())

	# noinspection PyMethodMayBeStatic
	def loadTemplate(self):
		result = JsonUtils.loadJsonSchema(self.templatePath + '/CharacterTemplate.json')
		return result

	def saveCharacter(self, name):
		path = Services.getConfigurationManager().getValue(ConfigurationManager.saveCharacterKey,
										ConfigurationManager.saveCharacterDirectoryKey)
		name = re.sub("[^a-zA-Z0-9]", "_", name)
		if 'json' not in name:
			name += '.json'
		characterPath = path + '/' + name
		try:
			self.character = JsonUtils.saveJsonFile(characterPath, self.character)
		except Exception as ex:
			Services.getLogger().logException(f'Exception while saving character {name}', ex)


if __name__ == "__main__":
	Services.setConfigurationManager(ConfigurationManager())
	Services.setLogger(Logger())
	characterManager = CharacterManager('./CharacterTemplates')
	characterManager.loadCharacter('Fred')
	characterManager.saveCharacter('Fred Save')
	pass
