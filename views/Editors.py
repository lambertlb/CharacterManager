from PySide6 import QtWidgets
from PySide6.QtGui import QDoubleValidator, QIntValidator


class BaseEditor:

	def __init__(self, entity, propertyName, callback, *args, **kwargs):
		self._entity = entity
		self._propertyName = propertyName
		self.callback = callback

	@property
	def entity(self):
		return self._entity

	@property
	def propertyName(self):
		return self._propertyName

	def getValue(self):
		return None

	def setValue(self, value):
		pass

	def badValue(self, good):
		pass


class LabelEditor(QtWidgets.QLabel, BaseEditor):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


class TextEditor(QtWidgets.QLineEdit, BaseEditor):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.textChanged[str].connect(self.onChanged)

	def onChanged(self, mewText):
		self.callback(self)

	def getValue(self):
		return self.text()

	def setValue(self, value):
		self.setText(value)

	def badValue(self, good):
		if good:
			self.setStyleSheet("QLineEdit" "{background : white; }")
		else:
			self.setStyleSheet("QLineEdit" "{background : red; }")
		pass


class IntegerEditor(TextEditor, BaseEditor):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setValidator(QIntValidator())

	def getValue(self):
		return int(self.text())

	def setValue(self, value):
		self.setText(str(value))


class NumberEditor(TextEditor, BaseEditor):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setValidator(QDoubleValidator())

	def getValue(self):
		return float(self.text())

	def setValue(self, value):
		self.setText(str(value))


class CompositeEditor(QtWidgets.QComboBox, BaseEditor):
	def __init__(self, optionalData, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.currentTextChanged.connect(self.onChanged)
		self.optionalData = optionalData
		if optionalData:
			index = 0
			for data in optionalData:
				if type(data) is str:
					dataToAdd = data
				else:
					dataToAdd = data._name
				self.addItem(dataToAdd)
				index += 1

	def getValue(self):
		return self.currentText()

	def setValue(self, value):
		foundIndex = 0
		if self.optionalData:
			index = 0
			for data in self.optionalData:
				if type(data) is str:
					dataToAdd = data
				else:
					dataToAdd = data._name
				if dataToAdd == value:
					foundIndex = index
				index += 1
		self.setCurrentIndex(foundIndex)

	def onChanged(self, mewText):
		self.callback(self)


class RadialEditor(QtWidgets.QRadioButton, BaseEditor):
	def __init__(self, propertyName, isSet, *args, **kwargs):
		super().__init__(propertyName=propertyName, *args, **kwargs)
		self.isSet = isSet
		self.setText(propertyName)
		self.setChecked(isSet)

	def getValue(self):
		return self.isChecked()
