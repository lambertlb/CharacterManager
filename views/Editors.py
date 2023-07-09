from PySide6 import QtWidgets
from PySide6.QtGui import QDoubleValidator, QIntValidator

class BaseEditor():

	def __init__(self, entity, propertyName, callback, *args, **kwargs):
		self._entity = entity
		self._propertyName = propertyName
		self.callback = callback
		pass

	@property
	def entity(self):
		return self._entity
	
	@property
	def propertyName(self):
		return self._propertyName

	def getNewData(self):
		return None

class TextEditor(QtWidgets.QLineEdit, BaseEditor):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.textChanged[str].connect(self.onChanged)

	def onChanged(self, mewText):
		self.callback(self)
	
	def getNewData(self):
		return self.text()

class IntegerEditor(TextEditor, BaseEditor):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setValidator(QIntValidator())

class NumberEditor(TextEditor, BaseEditor):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setValidator(QDoubleValidator())

class CompositeEditor(QtWidgets.QComboBox, BaseEditor):
	def __init__(self, optionalData, selectedData, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.currentTextChanged.connect(self.onChanged)
		if optionalData:
			index = 0
			foundIndex = 0
			for data in optionalData:
				if type(data) is str:
					dataToAdd = data
				else:
					dataToAdd = data._name
				self.addItem(dataToAdd)
				if dataToAdd == selectedData:
					foundIndex = index
				index += 1
			self.setCurrentIndex(foundIndex)

	def getNewData(self):
		return self.currentText()

	def onChanged(self, mewText):
		self.callback(self)
	
