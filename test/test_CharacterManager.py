import os
import unittest
from unittest import TestCase
from CharacterManagerConfig import CharacterManagerConfig

from configurator.Services import Services
from main import CharacterManager
from test.TestLogger import TestLogger


class TestCharacterManager(TestCase):
	testIni = './testConfig2.ini'

	@classmethod
	def setUpClass(cls):
		Services.setLogger(TestLogger())
		if os.path.exists(TestCharacterManager.testIni):
			os.remove(TestCharacterManager.testIni)
		config = CharacterManagerConfig(TestCharacterManager.testIni)
		Services.setConfigurationManager(config)
		config.setValue(CharacterManagerConfig.saveCharacterKey, CharacterManagerConfig.saveCharacterDirectoryKey,
						'./test/TestSavedCharacters')
		config.setValue(CharacterManagerConfig.sourcesKey, CharacterManagerConfig.characterTemplateDirectoryKey,
						'./test/TestSavedCharacters')

	@classmethod
	def tearDownClass(cls):
		if os.path.exists(TestCharacterManager.testIni):
			os.remove(TestCharacterManager.testIni)
		pass

	def testLoadCharacter(self):
		cm = CharacterManager()
		cm.loadCharacter('Character 1')
		assert cm.character
		assert cm.character.schema
		assert cm.character.PersonalInformation.Name == 'Fred FlintStone'
		assert cm.character.PersonalInformation.Age == 22
		assert cm.character.PersonalInformation.Weight == 110.5
		assert cm.character.Skills.History == 10
		assert cm.character.Skills.Stealth == 10
		assert cm.character.Skills.Athletics == 10
		pass


if __name__ == '__main__':
	unittest.main()
