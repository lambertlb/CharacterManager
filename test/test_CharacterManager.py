import json
import os
from unittest import TestCase
import unittest

from ConfigurationManager import ConfigurationManager
from JsonUtils import JsonUtils
from Services import Services
from main import CharacterManager
from test.TestLogger import TestLogger


class TestCharacterManager(TestCase):
	testIni = './testConfig2.ini'

	@classmethod
	def setUpClass(cls):
		Services.setLogger(TestLogger())
		if os.path.exists(TestCharacterManager.testIni):
			os.remove(TestCharacterManager.testIni)
		config = ConfigurationManager(TestCharacterManager.testIni)
		Services.setConfigurationManager(config)
		config.setValue(ConfigurationManager.saveCharacterKey, ConfigurationManager.saveCharacterDirectoryKey,
						'./test/TestSavedCharacters')
		config.setValue(ConfigurationManager.sourcesKey, ConfigurationManager.characterTemplateDirectoryKey,
						'./test/TestSavedCharacters')

	@classmethod
	def tearDownClass(cls):
		if os.path.exists(TestCharacterManager.testIni):
			os.remove(TestCharacterManager.testIni)
		pass

	def testLoadCharacter(self):
		cm = CharacterManager('./test/TestSavedCharacters')
		cm.loadCharacter('Character 1')
		dump = JsonUtils.convertToJson(cm.character)
		assert cm.character
		assert cm.character.definition
		assert cm.character.ParameterData.Name == 'Fred FlintStone'
		assert cm.character.ParameterData.Age == 22
		assert not cm.character.ParameterData.Dead
		assert cm.character.ParameterData.Name == 'Fred FlintStone'
		assert cm.character.ParameterData.Weight == 110.5
		assert cm.character.Skills[0].Hide == 10
		assert cm.character.Skills[1].Sneak == 11
		assert cm.character.Skills[2].Athletics == 12

if __name__ == '__main__':
    unittest.main()
