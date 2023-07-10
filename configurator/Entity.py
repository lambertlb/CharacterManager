import importlib
import inspect
import os
import re
from types import ModuleType
from CharacterManagerConfig import CharacterManagerConfig
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

	# keep track of loaded classes from scripts
	scriptInModule = {}
	# modules with entity classes
	modules = {}

	# map types in json data to python types. Used for validation
	typeMap = {
		'string': type(''),
		'integer': type(int(0)),
		'number': type(float(1.1)),
		'boolean': type(True),
		'null': type(None),
		'array': type([]),
		'object': type({})
	}

	_allEntities = {}

	def __init__(self):
		self._definition: dict | None = None

	@property
	def definition(self):
		return self._definition

	@definition.setter
	def definition(self, value):
		self._definition = value

	@staticmethod
	def getEntities():
		return list(Entity._allEntities.values())
	
	def register(self):
		"""
		This should be overridden in derived classes
		"""
		Entity._allEntities[self] = self
		pass

	def unRegister(self):
		Entity._allEntities.pop(self)
		
	def update(self):
		"""
		This should be overridden in derived classes
		"""
		pass
	
	def loadInDataForProperties(self, jsonData, dataDefinition):
		"""
		Load in all property data defined in the json data
		and attach it to this entity

		Args:
			jsonData (_type_): data defined in json file
			dataDefinition (_type_): schema for data
		"""
		self.definition = dataDefinition
		for parameter in list(jsonData.items()):
			Entity.loadPropertyData(self, parameter)

	def getPropertyDefinition(self, propertyName):
		"""
		Find this property name in the schema

		Args:
			propertyName (str): to look for

		Returns:
			schema defining this property
		"""
		if self._definition:
			properties = self._definition.get('properties')
			if properties:
				return properties.get(propertyName)
		return None

	@staticmethod
	def loadJsonFile(path, jsonSchema):
		"""
		Create an Entity based on the data in the json file

		Args:
			path (str): Path to json file
			jsonSchema (dict): schema for data

		Returns:
			Entity: populated entity
		"""
		data = JsonUtils.loadJsonFile(path)
		entity = Entity.createEntityFromJsonData(data, jsonSchema)
		return entity

	@staticmethod
	def createEntityFromJsonData(jsonData, jsonSchema):
		"""
		Create entity with this json data

		Args:
			jsonData (dict): json data
			jsonSchema (dict): schema for data

		Returns:
			Entity: populated entity
		"""
		entity = Entity.createEntity(jsonSchema)
		entity.loadInDataForProperties(jsonData, jsonSchema)
		try:
			entity.register()
		except Exception as ex:
			Services.getLogger().logException('Exception while registering', ex)
		return entity

	@staticmethod
	def createEntity(jsonSchema):
		"""
		Create entity based on schema.
		If the schema has a $schema tag the use that to look up and
		create the Entity

		Args:
			jsonSchema (dict): schema

		Returns:
			Entity: new Entity
		"""
		properties = jsonSchema.get('properties')
		if properties:
			scriptProperty = properties.get('$script')
			if scriptProperty:
				return Entity.loadScriptFromProperty(scriptProperty)
		return Entity()
		
	@staticmethod
	def loadScriptFromProperty(scriptProperty):
		"""
		Load in the script from this property definition

		Args:
			scriptProperty (dict): property description

		Returns:
			Entity: new Entity
		"""
		scriptName = scriptProperty.get('className')
		assert scriptName, '$script need key word "className"'
		return Entity.instanceFromScript(scriptName)

	@staticmethod
	def instanceFromScript(scriptName):
		"""
		Create an instance of Entity from script name

		Args:
			scriptName (str): full name of script

		Returns:
			Entity: new Entity
		"""
		scriptName = re.sub("[^a-zA-Z0-9.#]", "_", scriptName)
		classToLoad = Entity.scriptInModule.get(scriptName)
		if classToLoad:
			return Entity.createInstanceFromClass(classToLoad)
		parts = scriptName.split('#')
		if len(parts) == 2:
			return Entity.nameFromScript(parts[0], parts[1], scriptName)
		classToLoad = Entity.scriptInModule.get(scriptName)
		if not classToLoad:
			module = Entity.getModule(scriptName)
			classToLoad = Entity.findClassFromModule(module)
			Entity.scriptInModule[scriptName] = classToLoad
		
		return Entity.createInstanceFromClass(classToLoad)

	@staticmethod
	def createInstanceFromClass(classToCreate):
		# magic to create instance of class
		alias = "SomeAlias"
		return eval(alias + '()', {alias: classToCreate})

	@staticmethod
	def nameFromScript(nameSpace, className, scriptName):
		module = Entity.getModule(nameSpace)
		classToLoad = getattr(module, className)
		Entity.scriptInModule[scriptName] = classToLoad
		return Entity.createInstanceFromClass(classToLoad)

	@staticmethod
	def getModule(scriptName):
		module = Entity.modules.get(scriptName)  # use cached one
		if not module:
			module = importlib.import_module(scriptName)
			Entity.modules[scriptName] = module
		return module

	@staticmethod
	def findClassFromModule(module: ModuleType):
		"""
		Find subclass of Entity in the module

		Args:
			module (ModuleType): that holds the classes

		Returns:
			cls: subclass of Entity
		"""
		members = inspect.getmembers(module)
		for member in members:
			name, item = member
			if inspect.isclass(item) and issubclass(item, Entity):
				if name != 'Entity':
					return getattr(module, name)
		assert False, f'Found no class derived from Entity in module {module.__name__}'

	@staticmethod
	def getListOfClassesFromDirectory(path, filter):
		foundScripts = []
		files = os.listdir(path)
		for file in files:
			fullPath = path + '/' + file
			if os.path.isfile(fullPath):
				fullPath = re.sub("/", ".", fullPath)
				fullPath = re.sub("\.\.", "", fullPath)
				fullPath = re.sub("\.py", "", fullPath)
				foundScripts.append(fullPath)
		classes = {}
		Entity.getClassesFromScripts(foundScripts, filter, classes)
		return(list(classes.values()))

	@staticmethod
	def getClassesFromScripts(listOfScripts, filter, classes):
		for script in listOfScripts:
			Entity.getClassesFromScript(script, filter, classes)

	@staticmethod
	def getClassesFromScript(scriptName, filter, classes):
		module = Entity.getModule(scriptName)
		Entity.getClassesFromModule(module, filter, classes)

	@staticmethod
	def getClassesFromModule(module, filter, classes):
		members = inspect.getmembers(module)
		for member in members:
			name, item = member
			if inspect.isclass(item) and issubclass(item, filter):
				if name != filter.__name__:
					if not classes.get(name):
						classes[name] = Entity.createInstanceFromClass(getattr(module, name))

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
	def getPropertyData(entity, propertyName, data):
		"""
		Get data for property
		Args:
			entity: where to place property
			propertyName (string): name of property
			data (Any): data for the property
		"""
		definition = entity.getPropertyDefinition(propertyName)
		dataType = 'string'  # default to string if no definition
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
			if isinstance(element, dict):  # adding Entity?
				dataObject = Entity.createEntityFromJsonData(element, definition['items'])
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
		"""
		Is this valid data

		Args:
			dataType (_type_): type to test against
			data (Any): data to test
		"""
		assert Entity.isValidType([dataType], data)

	@staticmethod
	def createFromTemplate(schema):
		"""
		Create a new entity based on template (schema) information

		Args:
			schema (_type_): schema for item

		Returns:
			Entity: Entity with properties based on schema
		"""
		entity = Entity.createEntity(schema)
		entity.addRequiredProperties(schema)
		return entity
	
	def addRequiredProperties(self, schema):
		required = schema.get('required')
		if not required:
			return
		properties = schema.get('properties')
		for needed in required:
			self.addNeededProperty(properties, needed)
	
	def addNeededProperty(self, properties, needed):
		neededSchema = properties.get(needed)
		neededType = neededSchema.get('type')
		if neededType == 'string':
			setattr(self, needed, '')
			return
		if neededType == 'integer':
			setattr(self, needed, int(0))
			return
		if neededType == 'number':
			setattr(self, needed, float(0.0))
			return
		if neededType == 'boolean':
			setattr(self, needed, False)
			return
		if neededType == 'null':
			setattr(self, needed, None)
			return
		if neededType == 'array':
			array = []
			setattr(self, needed, array)
			return
		if neededType == 'object':
			setattr(self, needed, self.createFromTemplate(neededSchema))
		pass

	def propertiesForDisplay(self):
		displayData = []
		properties = list(self.definition.get('properties').items())
		for property in properties:
			dd = self.addDisplayDataFromProperty(property)
			if dd:
				displayData.append(dd)
		return displayData

	def addDisplayDataFromProperty(self, property):
		propertyName, type = property
		if propertyName == '$script':
			return None
		propertyType = type.get('type')
		return self.getDataForProperty(propertyName, propertyType)
	
	def getDataForProperty(self, propertyName, propertyType):
		propertyInfo = None
		propertyData = getattr(self, propertyName)
		if propertyType == 'object':
			propertyInfo = propertyData.propertiesForDisplay()
		return (propertyName, propertyType, propertyData, propertyInfo)

	def isValidPropertyChange(self, propertyName, propertyData):
		return True
	
	def changeProperty(self, propertyName, propertyData):
		if self.isValidPropertyChange(propertyName, propertyData):
			setattr(self, propertyName, propertyData)