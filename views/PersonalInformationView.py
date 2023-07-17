from PySide6 import QtWidgets

from CharacterServices import CharacterServices
from builder.PersonalInformation_ui import Ui_Form
from views.SubView import SubView


class PersonalInformationView(SubView, Ui_Form):

	def __init__(self, *args):
		super().__init__(*args)
		self.setupUi(self)
		super().setupView(10)
		self.verticalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
													QtWidgets.QSizePolicy.Expanding)
		self.gridLayout.addItem(self.verticalSpacer, 40, 1, 1, 1)
		self.buttonBarItem.setText('Per')
		self.setParentFrame = self.frame
		self.setGridToFill(self.gridLayout)

	def setupView(self):
		self.loadingData = True
		self.setEntity(CharacterServices.getCharacterManager().character.PersonalInformation)
		self.clearChildViews(self.frame)
		self.fillGridWithData()
		self.loadingData = False
