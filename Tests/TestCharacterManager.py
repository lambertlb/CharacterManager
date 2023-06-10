import os
from unittest import TestCase

from ConfigurationManager import ConfigurationManager
from Services import Services
from Tests.TestLogger import TestLogger
from main import CharacterManager


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
						'./TestSavedCharacters')

	@classmethod
	def tearDownClass(cls):
		if os.path.exists(TestCharacterManager.testIni):
			os.remove(TestCharacterManager.testIni)
		pass

	def testLoadCharacter(self):
		cm = CharacterManager('../CharacterTemplates')
		cm.loadCharacter('Character 1')
