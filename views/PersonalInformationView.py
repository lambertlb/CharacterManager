from PySide6 import QtWidgets

from CharacterServices import CharacterServices
from builder.PersonalInformation_ui import Ui_Form


class PersonalInformationView(QtWidgets.QWidget, Ui_Form):

	def __init__(self, *args):
		super().__init__(*args)
		self.setupUi(self)
		self.verticalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.gridLayout.addItem(self.verticalSpacer, 20, 1, 1, 1)
		self.row = 0

	def setupView(self):
		self.character = CharacterServices.getCharacterManager().character
		self.personalInformation = self.character.PersonalInformation
		displayData = self.personalInformation.propertiesForDisplay()
		self.clearChildViews(self.frame)
		self.addDisplayItems(displayData)
		# self.gridLayout.addWidget(self.verticalSpacer, self.row, 0)
		pass

	def clearChildViews(self, what):
		self.row = 0
		for child in what.children():
			if child != self.textEdit and child != self.horizontalLayout:
				child.deleteLater()

	def addDisplayItems(self, displayData):
		for property in displayData:
			self.addItemFromProperty(property)
			self.row += 1

	def addItemFromProperty(self, property):
		propertyName, propertyType, propertyData, optionalData = property
		if propertyType == 'object':
			return
		self.addLabel(propertyName)
		self.addEditor(propertyType, propertyData, optionalData)

	def addLabel(self, propertyName):
		label = QtWidgets.QLabel(self.frame)
		label.setText(propertyName + ':')
		self.gridLayout.addWidget(label, self.row, 0, 1 ,1)

	def addEditor(self, propertyType, propertyData, optionalData):
		if propertyType == 'string':
			editor = QtWidgets.QLineEdit(self.frame)
			editor.setText(propertyData)
			self.gridLayout.addWidget(editor, self.row, 1, 1 ,1)
		elif propertyType == 'integer' or propertyType == 'number':
			editor = QtWidgets.QLineEdit(self.frame)
			editor.setText(str(propertyData))
			self.gridLayout.addWidget(editor, self.row, 1, 1 ,1)
		elif propertyType == 'composite':
			editor = QtWidgets.QComboBox(self.frame)
			if optionalData:
				index = 0
				foundIndex = 0
				for data in optionalData:
					if type(data) is str:
						dataToAdd = data
					else:
						dataToAdd = data._name
					editor.addItem(dataToAdd)
					if dataToAdd == propertyData:
						foundIndex = index
					index += 1
				editor.setCurrentIndex(foundIndex)
			else:
				editor.addItem(propertyData)
			self.gridLayout.addWidget(editor, self.row, 1, 1 ,1)
			pass