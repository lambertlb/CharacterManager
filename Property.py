from BaseItem import BaseItem
from Entity import Entity


class Property:
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
	def loadData(where: Entity, propertyData):
		propertyName , data = propertyData
		Property.validate(where, propertyName, data)
		Property.getPropertyData(where, propertyName, data)

	@staticmethod
	def getPropertyData(where, propertyName, data):
		definition = where.getPropertyDefinition(propertyName)
		dataType = 'string'
		if definition:
			dataType = list(definition.values())[0]
		if dataType == 'string':
			setattr(where, propertyName, data)
			return
		if dataType == 'integer':
			setattr(where, propertyName, int(data))
			return
		if dataType == 'number':
			setattr(where, propertyName, float(data))
			return
		if dataType == 'boolean':
			setattr(where, propertyName, data)
			return
		if dataType == 'null':
			setattr(where, propertyName, None)
			return
		if dataType == 'array':
			array = []
			setattr(where, propertyName, array)
			Property.addArrayData(array, definition, data)
			return
		if dataType == 'object':
			dataObject = Entity()
			dataObject.loadData(data, definition)
			setattr(where, propertyName, dataObject)
			return

		assert False, f'Unsupported data type {dataType}'

	@staticmethod
	def	addArrayData(array: list, definition: dict, data):
		if not data:
			return
		if definition and definition.get('items'):
			types = definition['items'].get('type')
		for element in data:
			assert Property.isAllowArrayType(types, element)
			array.append(element)

	@staticmethod
	def isAllowArrayType(types, element):
		if not types:
			return True
		typeOfElement = type(element)
		for allowedType in types:
			at = Property.typeMap.get(allowedType)
			if typeOfElement == at:
				return True
			if typeOfElement == type(int(0)) and at == type(float(0)):
				return True
		return False

	@staticmethod
	def validate(where, key, data):
		# add validation code
		pass
