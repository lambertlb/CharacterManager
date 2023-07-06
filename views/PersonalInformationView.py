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
		self.schema = self.character.getPropertyDefinition('PersonalInformation')
		self.clearChildViews(self.frame)
		self.addItems()
		# self.gridLayout.addWidget(self.verticalSpacer, self.row, 0)
		pass

	def clearChildViews(self, what):
		self.row = 0
		for child in what.children():
			if child != self.textEdit and child != self.horizontalLayout:
				child.deleteLater()

	def addItems(self):
		x = self.schema.get('properties')
		properties = list(x.items())
		for property in properties:
			self.addItemFromProperty(property)
			self.row += 1


	def addItemFromProperty(self, property):
		propertyName, type = property
		if propertyName == '$script':
			return
		propertyType = type.get('type')
		self.addLabel(propertyName)
		self.addEditor(propertyName)

	def addLabel(self, propertyName):
		label = QtWidgets.QLabel(self.frame)
		label.setText(propertyName + ':')
		self.gridLayout.addWidget(label, self.row, 0, 1 ,1)

	def addEditor(self, propertyName):
		propertyType = self.personalInformation.getPropertyType(propertyName)
		if propertyType == 'string':
			editor = QtWidgets.QLineEdit(self.frame)
			editor.setText(getattr(self.personalInformation,propertyName))
			self.gridLayout.addWidget(editor, self.row, 1, 1 ,1)
		if propertyType == 'integer' or propertyType == 'number':
			editor = QtWidgets.QLineEdit(self.frame)
			editor.setText(str(getattr(self.personalInformation,propertyName)))
			self.gridLayout.addWidget(editor, self.row, 1, 1 ,1)
		pass