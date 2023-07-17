from PySide6 import QtCore

from CharacterServices import CharacterServices
from builder.Skills import Ui_Form
from views.Editors import RadialEditor
from views.SubView import SubView


class SkillsView(SubView, Ui_Form):

	def __init__(self, *args):
		super().__init__(*args)
		self.setupUi(self)
		super().setupView(40)
		self.buttonBarItem.setText('SKL')
		self.setParentFrame = self.frame
		self.setGridToFill(self.gridLayout)

	def setupView(self):
		self.loadingData = True
		self.setEntity(CharacterServices.getCharacterManager().character.Skills)
		self.clearChildViews(self.frame)
		self.row = 1
		self.fillGridWithData()
		self.loadingData = False

	def addLabel(self, property):
		propertyName, propertyType, propertyData, optionalData = property
		isSet = len(optionalData) != 0
		label = RadialEditor(entity=self.entity, propertyName=propertyName, isSet=isSet, callback=None,
							 parent=self.parentFrame)
		label.setText(propertyName + ':')
		label.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)  # ignore mouse events
		self.gridToFill.addWidget(label, self.row, 0, 1, 1)

	def addEditor(self, property, entity, column):
		editor = super().addEditor(property, entity, column + 1)
		editor.setReadOnly(True)
