from PySide6 import QtWidgets

from CharacterServices import CharacterServices
from builder.PersonalInformation_ui import Ui_Form
from views.SubView import SubView


class PersonalInformationView(SubView, Ui_Form):

	def __init__(self, *args):
		super().__init__(10, *args)
		self.setupUi(self)
		self.verticalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.gridLayout.addItem(self.verticalSpacer, 40, 1, 1, 1)
		self.row = 0
		self.buttonBarItem.setText('Per')

	def setupView(self):
		self.setEntity(CharacterServices.getCharacterManager().character.PersonalInformation)
		self.character = CharacterServices.getCharacterManager().character
		displayData = self.entity.propertiesForDisplay()
		self.clearChildViews(self.frame)
		self.addDisplayItems(displayData)
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
		self.addLabel(propertyName)
		self.addEditor(propertyType, propertyData, optionalData)

	def addLabel(self, propertyName):
		label = QtWidgets.QLabel(self.frame)
		label.setText(propertyName + ':')
		self.gridLayout.addWidget(label, self.row, 0, 1 ,1)

	def addEditor(self, propertyType, propertyData, optionalData):
		editor = None
		if propertyType == 'string':
			editor = QtWidgets.QLineEdit(self.frame)
			editor.setText(propertyData)
			self.gridLayout.addWidget(editor, self.row, 1, 1 ,1)
		elif propertyType == 'integer' or propertyType == 'number':
			editor = QtWidgets.QLineEdit(self.frame)
			editor.setText(str(propertyData))
			self.gridLayout.addWidget(editor, self.row, 1, 1 ,1)
		elif propertyType == 'composite':
			editor = self.addCompositeData(propertyData, optionalData)
		elif propertyType == 'object':
			self.row += 1
			self.addDisplayItems(optionalData)
		if editor:
			self.gridLayout.addWidget(editor, self.row, 1, 1 ,1)

	def addCompositeData(self, propertyData, optionalData):
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
		return editor