import importlib
import inspect

from JsonUtils import JsonUtils
from Property import Property
from ScriptBase import ScriptBase
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

	schemas = {}

	def __init__(self):
		self._definition: dict | None = None
		self._script = None

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
		scriptProperty = properties.get('$script')
		if scriptProperty:
			self.loadScriptProperty(scriptProperty)

	def loadScriptProperty(self, scriptProperty):
		scriptName = scriptProperty.get('className')
		if not scriptName:
			return
		script = self.loadScript(scriptName)
		if script:
			self._script = script
			try:
				self._script.register(self)
			except Exception as ex:
				Services.getLogger().logException(f'Exception while calling register on {scriptProperty}', ex)
	
	def loadScript(self, scriptName):
		script = Entity.schemas.get(scriptName)
		if not script:
			module = importlib.import_module(scriptName)
			script =  self.getClassFromModule(module)
			if script:
				Entity.schemas[scriptName] = script
		return script

	def getClassFromModule(self, module):
		members = inspect.getmembers(module)
		for member in members:
			name, item = member
			if inspect.isclass(item) and issubclass(item, ScriptBase):
				if name != 'ScriptBase':
					classToLoad = getattr(module, name)
					alias = name + "Alias"
					return eval(alias + '()', {alias: classToLoad})

	def getPropertyDefinition(self, propertyName):
		if self._definition:
			properties = self._definition.get('properties')
			if properties:
				return properties.get(propertyName)
		return None
