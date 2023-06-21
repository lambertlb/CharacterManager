import importlib
import inspect
import re
from types import ModuleType

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

	This class is also the base class for any scripts referenced in a schema.
	"""

	schemas = {}

	def __init__(self):
		self._definition: dict | None = None

	@property
	def definition(self):
		return self._definition

	@definition.setter
	def definition(self, value):
		self._definition = value

	def register(self):
		pass

	def update(self):
		pass
	
	@staticmethod
	def loadJsonFile(path, jsonSchema):
		data = JsonUtils.loadJsonFile(path)
		entity = Entity.createEntityFromJsonData(data, jsonSchema)
		return entity

	@staticmethod
	def createEntityFromJsonData(jsonData, jsonSchema):
		entity = Entity.createEntity(jsonSchema)
		entity.loadInData(jsonData, jsonSchema)
		try:
			entity.register()
		except Exception as ex:
			Services.getLogger().logException('Exception while registering', ex)
		return entity

	@staticmethod
	def createEntity(jsonSchema):
		properties = jsonSchema.get('properties')
		if properties:
			scriptProperty = properties.get('$script')
			if scriptProperty:
				return Entity.loadScriptFromProperty(scriptProperty)
		return Entity()
		
	@staticmethod
	def loadScriptFromProperty(scriptProperty):
		scriptName = scriptProperty.get('className')
		assert scriptName, '$script need key word "className"'
		return Entity.instanceFromScript(scriptName)

	@staticmethod
	def instanceFromScript(scriptName):
		scriptName = re.sub("[^a-zA-Z0-9.]", "_", scriptName)
		classToLoad = Entity.schemas.get(scriptName)
		if not classToLoad:
			module = importlib.import_module(scriptName)
			classToLoad =  Entity.findClassFromModule(module)
			Entity.schemas[scriptName] = classToLoad
		
		# magic to create instance of class
		alias = "SomeAlias"
		return eval(alias + '()', {alias: classToLoad})

	@staticmethod
	def findClassFromModule(module: ModuleType):
		members = inspect.getmembers(module)
		for member in members:
			name, item = member
			if inspect.isclass(item) and issubclass(item, Entity):
				if name != 'Entity':
					return getattr(module, name)
		assert False, f'Found no class derived from Entity in module {module.__name__}'

	def loadInData(self, entityData, dataDefinition):
		self.definition = dataDefinition
		for parameter in list(entityData.items()):
			Property.loadData(self, parameter)

	def getPropertyDefinition(self, propertyName):
		if self._definition:
			properties = self._definition.get('properties')
			if properties:
				return properties.get(propertyName)
		return None
