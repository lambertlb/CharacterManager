from PySide6 import QtWidgets

from CharacterServices import CharacterServices
from views.Editors import BaseEditor, CompositeEditor, IntegerEditor, LabelEditor, NumberEditor, TextEditor


class ButtonBarItem(QtWidgets.QPushButton):
	def __init__(self, subView, *args):
		super().__init__(*args)
		self.subView = subView


class SubView(QtWidgets.QWidget):

	def __init__(self, *args):
		super().__init__(*args)
		self.buttonBarItem = ButtonBarItem(self)
		self.orderInBar = 0
		self.row = 0
		self.entity = None
		self.gridToFill = None
		self.parentFrame = None
		self.loadingData = True

	def setEntity(self, value):
		self.entity = value

	def setGridToFill(self, value):
		self.gridToFill = value

	def setParentFrame(self, value):
		self.parentFrame = value

	def getButtonBarItem(self):
		return self.buttonBarItem

	def enableButtonBarItem(self, state):
		self.buttonBarItem.setEnabled(state)

	def getOrderInBar(self):
		return self.orderInBar

	def getEntity(self):
		return self.entity

	def setupView(self, orderInBar):
		self.orderInBar = orderInBar

	def fillGridWithData(self):
		displayData = self.entity.propertiesForDisplay()
		self.addDisplayItems(displayData, self.entity)
		pass

	def addDisplayItems(self, displayData, entity):
		for property in displayData:
			self.addItemFromProperty(property, entity)
			self.row += 1

	def addItemFromProperty(self, property, entity):
		self.addLabel(property)
		self.addEditor(property, entity, 1)

	def addLabel(self, property):
		propertyName, propertyType, propertyData, optionalData = property
		label = LabelEditor(entity=None, propertyName=None, callback=None, parent=self.parentFrame)
		label.setText(propertyName + ':')
		self.gridToFill.addWidget(label, self.row, 0, 1, 1)

	def addEditor(self, property, entity, column):
		propertyName, propertyType, propertyData, optionalData = property
		editor = None
		if propertyType == 'string':
			editor = TextEditor(entity=entity, propertyName=propertyName, callback=self.editorDataChanged,
								parent=self.parentFrame)
			editor.setValue(propertyData)
		elif propertyType == 'integer':
			editor = IntegerEditor(entity=entity, propertyName=propertyName, callback=self.editorDataChanged,
								   parent=self.parentFrame)
			editor.setValue(propertyData)
		elif propertyType == 'number':
			editor = NumberEditor(entity=entity, propertyName=propertyName, callback=self.editorDataChanged,
								  parent=self.parentFrame)
			editor.setValue(propertyData)
		elif propertyType == 'composite':
			editor = CompositeEditor(entity=entity, propertyName=propertyName, callback=self.editorDataChanged,
									 optionalData=optionalData, parent=self.parentFrame)
			editor.setValue(propertyData)
		elif propertyType == 'object':
			self.row += 1
			self.addDisplayItems(optionalData, getattr(entity, propertyName))
		if editor:
			self.gridToFill.addWidget(editor, self.row, column, 1, 1)
		return editor

	def editorDataChanged(self, editor: BaseEditor):
		if self.loadingData:
			return
		editor.entity.changeProperty(editor._propertyName, editor.getValue())
		CharacterServices.getCharacterManager().save()

	def clearChildViews(self, what):
		self.row = 0
		for child in what.children():
			if isinstance(child, BaseEditor):
				child.deleteLater()
