import os
import re
import sys
import traceback

from PySide6 import QtWidgets

from CharacterManagerConfig import CharacterManagerConfig
from CharacterTemplates.scripts.CharacterClass import CharacterClass
from configurator.Entity import Entity
from configurator.JsonUtils import JsonUtils
from configurator.Logger import Logger
from configurator.Services import Services


class CharacterManager:

	def __init__(self):
		self.character = None

	def loadCharacter(self, name):
		pathToSavedCharacters = Services.getConfigurationManager().getValue(CharacterManagerConfig.saveCharacterKey,
																			CharacterManagerConfig.saveCharacterDirectoryKey)
		name = re.sub("[^a-zA-Z0-9]", "_", name)
		if 'json' not in name:
			name += '.json'
		characterPath = pathToSavedCharacters + '/' + name
		self.loadCharacterFromFile(characterPath)

	def loadCharacterFromFile(self, path):
		Entity.clear()
		try:
			self.character = Entity.loadJsonFile(path, self.loadTemplate())
		except (Exception,):
			Services.getLogger().log(traceback.format_exc())
		pass

	# noinspection PyMethodMayBeStatic
	def loadTemplate(self):
		templatePath = Services.getConfigurationManager().getValue(CharacterManagerConfig.sourcesKey,
																	CharacterManagerConfig.characterTemplateDirectoryKey)
		result = JsonUtils.loadJsonSchema(templatePath + '/CharacterTemplate.json')
		return result

	def save(self):
		if self.character and self.character.PersonalInformation.Name:
			self.saveCharacter(self.character.PersonalInformation.Name)
	
	def saveCharacter(self, name):
		path = Services.getConfigurationManager().getValue(CharacterManagerConfig.saveCharacterKey,
															CharacterManagerConfig.saveCharacterDirectoryKey)
		name = re.sub("[^a-zA-Z0-9]", "_", name)
		if 'json' not in name:
			name += '.json'
		characterPath = path + '/' + name
		# try:
		# 	JsonUtils.saveJsonFile(characterPath, self.character)
		# except Exception as ex:
		# 	Services.getLogger().logException(f'Exception while saving character {name}', ex)
		JsonUtils.saveJsonFile(characterPath, self.character)

	def existingCharacters(self):
		characters = []
		path = Services.getConfigurationManager().getValue(CharacterManagerConfig.saveCharacterKey,
															CharacterManagerConfig.saveCharacterDirectoryKey)
		files = os.listdir(path)
		for file in files:
			fullPath = path + '/' + file
			if os.path.isfile(fullPath):
				characters.append(self.getCharacterInfo(fullPath))
		return characters
	
	def getCharacterInfo(self, file):
		self.loadCharacterFromFile(file)
		return (self.character.PersonalInformation.Name, file, self.character)

	def createNewCharacter(self, newName):
		template = self.loadTemplate()
		self.character = Entity.createFromTemplate(template)
		self.character.PersonalInformation.Name = newName
		self.saveCharacter(newName)

	def deleteCharacter(self, file):
		os.remove(file)

	def getListOfAllClasses(self):
		templatePath = Services.getConfigurationManager().getValue(CharacterManagerConfig.sourcesKey,
																	CharacterManagerConfig.characterTemplateDirectoryKey)
		path = templatePath + '/scripts/Classes'
		classes = Entity.getListOfClassesFromDirectory(path, Entity)
		return classes

	def addClass(self, cls):
		newCls = CharacterClass()
		newCls.Class = cls._name
		newCls.register()
		self.character.ClassInformation.Classes.append(newCls)
		self.save()
		pass

	def deleteClass(self, cls):
		for existing in self.character.ClassInformation.Classes:
			if cls == existing:
				self.character.ClassInformation.Classes.remove(cls)
				cls.unRegister()
				break
		self.save()
		pass


if __name__ == "__main__":
	from CharacterServices import CharacterServices
	CharacterServices.setConfigurationManager(CharacterManagerConfig())
	CharacterServices.setLogger(Logger())
	CharacterServices.setCharacterManager(CharacterManager())
	app = QtWidgets.QApplication(sys.argv)
	from views.MainWindow import MainWindow
	app.mainWindow = MainWindow()
	CharacterServices.setRootWindow(app.mainWindow)
	app.mainWindow.show()
	sys.exit(app.exec())
	# CharacterServices.getCharacterManager().loadCharacter('Fred')
	# CharacterServices.getCharacterManager().saveCharacter('Fred Save')
