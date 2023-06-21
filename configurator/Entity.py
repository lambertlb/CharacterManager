import importlib
import inspect
import re
from types import ModuleType
from configurator.JsonUtils import JsonUtils

from configurator.Services import Services


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
	typeMap = {
		'string': type(''),
		'integer': type(int(0)),
		'number': type(float(1.1)),
		'boolean': type(True),
		'null': type(None),
		'array': type([]),
		'object': type({})
	}

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
			Entity.loadPropertyData(self, parameter)

	def getPropertyDefinition(self, propertyName):
		if self._definition:
			properties = self._definition.get('properties')
			if properties:
				return properties.get(propertyName)
		return None

	@staticmethod
	def loadPropertyData(where, propertyData):
		"""
		Load the property defined in propertyData onto the
		Entity specified in where
		Args:
			where (Entity): where to place property
			propertyData (tuple): contains key and data for property
		"""
		propertyName, data = propertyData
		Entity.getPropertyData(where, propertyName, data)

	@staticmethod
	def getPropertyData(where, propertyName, data):
		"""
		Get data for property
		Args:
			where (Entity): where to place property
			propertyName (string): name of property
			data (Any): data for the property
		"""
		entity = where
		definition = entity.getPropertyDefinition(propertyName)
		dataType = 'string'
		if definition:
			# if there is a definition then use it for validation
			dataType = list(definition.values())[0]
			Entity.validate(dataType, data)
		if dataType == 'string':
			setattr(entity, propertyName, data)
			return
		if dataType == 'integer':
			setattr(entity, propertyName, int(data))
			return
		if dataType == 'number':
			setattr(entity, propertyName, float(data))
			return
		if dataType == 'boolean':
			setattr(entity, propertyName, data)
			return
		if dataType == 'null':
			setattr(entity, propertyName, None)
			return
		if dataType == 'array':
			array = []
			setattr(entity, propertyName, array)
			Entity.addArrayData(array, definition, data)
			return

		# must be object if got here
		dataObject = Entity.createEntityFromJsonData(data, definition)
		setattr(entity, propertyName, dataObject)

	@staticmethod
	def createEntityForProperty(data, definition):
		from configurator.Entity import Entity
		return Entity.createEntityFromJsonData(data, definition)
		
	@staticmethod
	def addArrayData(array: list, definition: dict, data):
		"""
		Add data to array if it exists
		Args:
			array (list): destination for data
			definition (dict): used for validation
			data (Any): data to add to array
		"""
		types = []
		if definition and definition.get('items'):
			types = definition['items'].get('type')
			if not isinstance(types, list):
				types = [types]
		for element in data:
			assert Entity.isValidType(types, element)
			if isinstance(element, dict):
				dataObject = Entity.createEntityForProperty(element, definition['items'])
				array.append(dataObject)
			else:
				array.append(element)

	@staticmethod
	def isValidType(types: list, data):
		"""
		Is this valid data for property or array
		Args:
			types (array): valid json types
			data (data): data to test and add

		Returns:
			boolean: True if valid type
		"""
		typeOfElement = type(data)
		for typeToCheck in types:
			allowedType = Entity.typeMap.get(typeToCheck)
			if typeOfElement == allowedType:
				return True
			# integer is ok if number is also allowed
			if typeOfElement == int and allowedType == float:
				return True
		return False

	@staticmethod
	def validate(dataType, data):
		assert Entity.isValidType([dataType], data)
