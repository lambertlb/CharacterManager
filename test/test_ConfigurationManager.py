import os
from unittest import TestCase
import unittest
from CharacterManagerConfig import CharacterManagerConfig


class TestConfigurationManager(TestCase):
	testIni = './testConfig.ini'

	@classmethod
	def setUpClass(cls):
		if os.path.exists(TestConfigurationManager.testIni):
			os.remove(TestConfigurationManager.testIni)

	def testSetDefaultsIfNeeded(self):
		config = CharacterManagerConfig(TestConfigurationManager.testIni)
		assert os.path.exists(self.testIni)
		assert config.getValue(CharacterManagerConfig.sourcesKey, CharacterManagerConfig.characterTemplateDirectoryKey,
									'default') == './CharacterTemplates'

	def testSaveValue(self):
		config = CharacterManagerConfig(TestConfigurationManager.testIni)
		config.setValue('TestSection', 'TestKey', 'Test Value')
		config2 = CharacterManagerConfig(self.testIni)
		assert config2.getValue('TestSection', 'TestKey', 'fail') == 'Test Value'

	def testGetValue(self):
		config = CharacterManagerConfig(TestConfigurationManager.testIni)
		config.setValue('TestSection2', 'TestKey2', 'Test Value2')
		assert config.getValue('TestSection2', 'TestKey2', 'fail') == 'Test Value2'
		assert config.getValue('TestSection2', 'TestKey3', 'fail') == 'fail'

	@classmethod
	def tearDownClass(cls):
		if os.path.exists(TestConfigurationManager.testIni):
			os.remove(TestConfigurationManager.testIni)


if __name__ == '__main__':
	unittest.main()
