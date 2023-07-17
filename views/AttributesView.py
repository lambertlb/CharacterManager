from PySide6 import QtWidgets

from CharacterServices import CharacterServices
from builder.Attributes_ui import Ui_Form
from views.Editors import BaseEditor
from views.SubView import SubView


class AttributeView(SubView, Ui_Form):

	def __init__(self, *args):
		super().__init__(*args)
		self.setupUi(self)
		super().setupView(20)
		self.buttonBarItem.setText('Att')
		self.setParentFrame = self.frame
		self.setGridToFill(self.attributeGrid)
		self.verticalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
													QtWidgets.QSizePolicy.Expanding)
		self.attributeGrid.addItem(self.verticalSpacer, 40, 1, 1, 1)

	def setupView(self):
		self.loadingData = True
		self.setEntity(CharacterServices.getCharacterManager().character.Attributes)
		self.clearChildViews(self.frame)
		self.fillGridWithData()
		self.loadingData = False
		self.computeBonuses()

	def editorDataChanged(self, editor: BaseEditor):
		if self.loadingData:
			return
		super().editorDataChanged(editor)
		goodValue = self.entity.isValidPropertyChange(editor.propertyName, editor.getValue())
		editor.badValue(goodValue)
		if not goodValue:
			print(f'{editor.propertyName} is bad')
		self.computeBonuses()

	def computeBonuses(self):
		self.strengthBonusEdit.setText(str(self.entity.computeAttributeBonus(self.entity.Strength)))
		self.dexterityBonusEdit.setText(str(self.entity.computeAttributeBonus(self.entity.Dexterity)))
		self.constitutionBonusEdit.setText(str(self.entity.computeAttributeBonus(self.entity.Constitution)))
		self.intelligenceBonusEdit.setText(str(self.entity.computeAttributeBonus(self.entity.Intelligence)))
		self.wisdomBonusEdit.setText(str(self.entity.computeAttributeBonus(self.entity.Wisdom)))
		self.charismaBonusEdit.setText(str(self.entity.computeAttributeBonus(self.entity.Charisma)))
		self.buyPointsEdit.setText(str(self.entity.getPointCost()))
