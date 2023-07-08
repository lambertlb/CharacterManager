from functools import partial
import sys

from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QMainWindow, QPushButton

from builder.MainWindow_ui import Ui_MainWindow
from views.CharacterManagementView import CharacterManagementView
from views.PersonalInformationView import PersonalInformationView


class MainWindow(QMainWindow, Ui_MainWindow):

	def __init__(self, *args):
		super().__init__(*args)
		self.setupUi(self)
		self.characterManagement = CharacterManagementView(self.frame)
		self.characterManagement.setVisible(True)
		self.verticalLayout.addWidget(self.characterManagement)
		self.personalInformationView = PersonalInformationView(self.frame)
		self.verticalLayout.addWidget(self.personalInformationView)
		self.personalInformationView.setVisible(False)
		self.currentView = None
		self.setupCharacterManagement()
		for i in range(20):
			pushButton = QPushButton(self.scrollAreaWidgetContents)
			pushButton.setText(f'Btn{i}')
			pushButton.setMaximumSize(QtCore.QSize(40, 30))
			index = self.horizontalLayout.indexOf(self.horizontalSpacer)
			self.horizontalLayout.insertWidget(index, pushButton)

	def buttonClicked(self, buttonData):
		if self.currentView:
			self.currentView.setVisible(False)
		self.currentView = buttonData
		self.currentView.setVisible(True)
		buttonData.setupView()
		self.update()
		pass

	def setupCharacterManagement(self):
		self.buttonClicked(self.characterManagement)

	def clearButtonBar(self):
		for child in self.scrollAreaWidgetContents.children():
			if child != self.horizontalSpacer:
				child.deleteLater()

	def editCharacter(self):
		self.clearButtonBar()
		self.fillRibbonBar()

	def fillRibbonBar(self):
		self.addToButtonBar('Per', self.personalInformationView)
		pass

	def addToButtonBar(self, buttonText, buttonData):
		pushButton = QPushButton(self.scrollAreaWidgetContents)
		pushButton.setText(buttonText)
		pushButton.setMaximumSize(QtCore.QSize(40, 30))
		index = self.horizontalLayout.indexOf(self.horizontalSpacer)
		self.horizontalLayout.insertWidget(index, pushButton)
		pushButton.clicked.connect(partial(self.buttonClicked, buttonData))



if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	app.mainWindow = MainWindow()
	app.mainWindow.show()
	sys.exit(app.exec())
