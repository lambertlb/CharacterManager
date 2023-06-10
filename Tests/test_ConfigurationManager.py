import os
from unittest import TestCase
import unittest

from ConfigurationManager import ConfigurationManager


class TestConfigurationManager(TestCase):
	testIni = './testConfig.ini'

	@classmethod
	def setUpClass(cls):
		if os.path.exists(TestConfigurationManager.testIni):
			os.remove(TestConfigurationManager.testIni)

	def testSetDefaultsIfNeeded(self):
		config = ConfigurationManager(TestConfigurationManager.testIni)
		assert os.path.exists(self.testIni)
		assert config.getValue(ConfigurationManager.sourcesKey, ConfigurationManager.characterTemplateDirectoryKey,
									'default') == './CharacterTemplates'

	def testSaveValue(self):
		config = ConfigurationManager(TestConfigurationManager.testIni)
		config.setValue('TestSection', 'TestKey', 'Test Value')
		config2 = ConfigurationManager(self.testIni)
		assert config2.getValue('TestSection', 'TestKey', 'fail') == 'Test Value'

	def testGetValue(self):
		config = ConfigurationManager(TestConfigurationManager.testIni)
		config.setValue('TestSection2', 'TestKey2', 'Test Value2')
		assert config.getValue('TestSection2', 'TestKey2', 'fail') == 'Test Value2'
		assert config.getValue('TestSection2', 'TestKey3', 'fail') == 'fail'

	@classmethod
	def tearDownClass(cls):
		if os.path.exists(TestConfigurationManager.testIni):
			os.remove(TestConfigurationManager.testIni)

if __name__ == '__main__':
    unittest.main()
