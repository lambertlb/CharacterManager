from PySide6 import QtWidgets

from CharacterServices import CharacterServices
from builder.PersonalInformation_ui import Ui_Form
from views.Editors import BaseEditor, CompositeEditor, IntegerEditor, NumberEditor, TextEditor
from views.SubView import SubView


class PersonalInformationView(SubView, Ui_Form):

	def __init__(self, *args):
		super().__init__(*args)
		self.loadingData = True
		self.setupUi(self)
		super().setupView(10)
		self.verticalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.gridLayout.addItem(self.verticalSpacer, 40, 1, 1, 1)
		self.row = 0
		self.buttonBarItem.setText('Per')

	def setupView(self):
		self.loadingData = True
		self.setEntity(CharacterServices.getCharacterManager().character.PersonalInformation)
		self.character = CharacterServices.getCharacterManager().character
		displayData = self.entity.propertiesForDisplay()
		self.clearChildViews(self.frame)
		self.addDisplayItems(displayData, self.entity)
		self.loadingData = False

	def clearChildViews(self, what):
		self.row = 0
		for child in what.children():
			if child != self.textEdit and child != self.horizontalLayout:
				child.deleteLater()

	def addDisplayItems(self, displayData, entity):
		for property in displayData:
			self.addItemFromProperty(property, entity)
			self.row += 1

	def addItemFromProperty(self, property, entity):
		propertyName, propertyType, propertyData, optionalData = property
		self.addLabel(propertyName)
		self.addEditor(property, entity)

	def addLabel(self, propertyName):
		label = QtWidgets.QLabel(self.frame)
		label.setText(propertyName + ':')
		self.gridLayout.addWidget(label, self.row, 0, 1 ,1)

	def addEditor(self, property, entity):
		propertyName, propertyType, propertyData, optionalData = property
		editor = None
		if propertyType == 'string':
			editor = TextEditor(entity=entity, propertyName=propertyName, callback=self.editorDataChanged, parent=self.frame)
			editor.setValue(propertyData)
		elif propertyType == 'integer':
			editor = IntegerEditor(entity=entity, propertyName=propertyName, callback=self.editorDataChanged, parent=self.frame)
			editor.setValue(propertyData)
		elif propertyType == 'number':
			editor = NumberEditor(entity=entity, propertyName=propertyName, callback=self.editorDataChanged, parent=self.frame)
			editor.setValue(propertyData)
		elif propertyType == 'composite':
			editor = CompositeEditor(entity=entity, propertyName=propertyName, callback=self.editorDataChanged, optionalData=optionalData, parent=self.frame)
			editor.setValue(propertyData)
		elif propertyType == 'object':
			self.row += 1
			self.addDisplayItems(optionalData, getattr(entity, propertyName))
		if editor:
			self.gridLayout.addWidget(editor, self.row, 1, 1 ,1)

	def editorDataChanged(self, editor: BaseEditor):
		if self.loadingData:
			return
		editor.entity.isValidPropertyChange(editor._propertyName, editor.getValue())
		pass