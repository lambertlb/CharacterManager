class Property:
	"""
	Class to handle parsing properties on an object in json format
	and adding them to an entity
	"""

	"""
	map json data types to python types
	"""
	typeMap = {
		'string': type(''),
		'integer': type(int(0)),
		'number': type(float(1.1)),
		'boolean': type(True),
		'null': type(None),
		'array': type([]),
		'object': type({})
	}

	@staticmethod
	def loadData(where, propertyData):
		"""
		Load the property defined in propertyData onto the
		Entity specified in where
		Args:
			where (Entity): where to place property
			propertyData (tuple): contains key and data for property
		"""
		propertyName, data = propertyData
		Property.getPropertyData(where, propertyName, data)

	@staticmethod
	def getPropertyData(where, propertyName, data):
		"""
		Get data for property
		Args:
			where (Entity): where to place property
			propertyName (string): name of property
			data (Any): data for the property
		"""
		from Entity import Entity  # avoid circular reference
		entity: Entity = where
		definition = entity.getPropertyDefinition(propertyName)
		dataType = 'string'
		if definition:
			# if there is a definition then use it for validation
			dataType = list(definition.values())[0]
			Property.validate(dataType, data)
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
			Property.addArrayData(array, definition, data)
			return
		if dataType == 'object':
			dataObject = Property.createEntity(data, definition)
			setattr(entity, propertyName, dataObject)
			return

		assert False, f'Unsupported data type {dataType}'

	@staticmethod
	def createEntity(data, definition):
		from Entity import Entity
		dataObject = Entity()
		dataObject.loadData(data, definition)
		return dataObject
		
	@staticmethod
	def addArrayData(array: list, definition: dict, data):
		"""
		Add data to array if it exists
		Args:
			array (list): destination for data
			definition (dict): used for validation
			data (Any): data to add to array
		"""
		if not data:
			return
		types = []
		if definition and definition.get('items'):
			types = definition['items'].get('type')
			if not isinstance(types, list):
				types = [types]
		for element in data:
			assert Property.isValidType(types, element)
			if isinstance(element, dict):
				dataObject = Property.createEntity(element, definition['items'])
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
		if not types:
			return True	 # default to true if no definition
		typeOfElement = type(data)
		for typeToCheck in types:
			allowedType = Property.typeMap.get(typeToCheck)
			if typeOfElement == allowedType:
				return True
			# integer is ok if number is also allowed
			if isinstance(typeOfElement, int) and isinstance(allowedType, float):
				return True
		return False

	@staticmethod
	def validate(dataType, data):
		assert Property.isValidType([dataType], data)
