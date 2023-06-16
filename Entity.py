from types import FunctionType, MethodType
from ConfigurationManager import ConfigurationManager
from JsonUtils import JsonUtils
from Property import Property
from Services import Services


class Entity:
	"""
	This class manages a configuration object.
	It contains properties.
		These properties mirror the ones in json schema meaning they can be as follows.
			string,
			integer,
			number,
			boolean,
			null,
			array,
			object
	It will also contain the definitions for the properties. This serves multiple
	purposes.
	1) The definitions are used to validate the data at load time.
	2) The definitions can also be used as part of a GUI to validate input at runtime.
	"""
	def __init__(self):
		self._definition: dict | None = None

	@property
	def definition(self):
		return self._definition

	@definition.setter
	def definition(self, value):
		self._definition = value

	@staticmethod
	def loadJsonFile(path, template):
		data = JsonUtils.loadJsonFile(path)
		entity = Entity()
		entity.definition = template
		entity.loadData(data, template)
		return entity

	def loadData(self, entityData, dataDefinition):
		self.definition = dataDefinition
		for parameter in list(entityData.items()):
			Property.loadData(self, parameter)
		self.loadScripts()

	def loadScripts(self):
		properties = self.definition.get('properties')
		if not properties:
			return
		script = properties.get('$script')
		if script:
			path = Services.getConfigurationManager().getValue(ConfigurationManager.scriptsKey,
								ConfigurationManager.scriptsDirectoryKey)
			path = path + '/' + script
			codeString = JsonUtils.loadScript(path)
			code = compile(codeString, "<string>", "exec")
			newFunction = FunctionType(code.co_consts[0], globals(), "update")
			self.update = MethodType(newFunction, self)
			self.update("Survival", 20)
			pass
	
	def getPropertyDefinition(self, propertyName):
		if self._definition:
			properties = self._definition.get('properties')
			if properties:
				return properties.get(propertyName)
		return None