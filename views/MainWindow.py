from functools import partial
import sys

from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QMainWindow, QPushButton
from CharacterServices import CharacterServices

from builder.MainWindow_ui import Ui_MainWindow
from views.CharacterManagementView import CharacterManagementView
from views.PersonalInformationView import PersonalInformationView
from views.SubView import SubView


class MainWindow(QMainWindow, Ui_MainWindow):

	def __init__(self, *args):
		super().__init__(*args)
		self.setupUi(self)
		self.subViews = {}
		self.startingSubView = None
		self.currentView = None
		self.loadSubViews()
		self.enableButtons(False)
		self.buttonClicked(self.startingSubView)

	def buttonClicked(self, newSubView):
		if self.currentView:
			if self.currentView.isDirty:
				return
			self.currentView.setVisible(False)
		self.currentView = newSubView
		self.currentView.setVisible(True)
		newSubView.setupView()

	def loadSubViews(self):
		self.getSubViews()
		keys = list(sorted(self.subViews.keys()))
		self.startingSubView = self.subViews[keys[0]]
		for subViewKey in keys:
			subView: SubView = self.subViews[subViewKey]
			subView.setVisible(False)
			subView.setParent(self.frame)
			self.verticalLayout.addWidget(subView)
			self.addToButtonBar(subView)
	
	def getSubViews(self):
		# make this dynamic
		view = PersonalInformationView()
		self.subViews[view.getOrderInBar()] = view
		view = CharacterManagementView()
		self.subViews[view.getOrderInBar()] = view

	def editCharacter(self):
		name = CharacterServices.getCharacterManager().character.PersonalInformation.Name
		self.setWindowTitle(name)
		self.enableButtons(True)

	def enableButtons(self, state):
		if not state:
			self.setWindowTitle('Select Character To Edit')
		for subView in self.subViews.values():
			subView.enableButtonBarItem(state)
	
	def addToButtonBar(self, subView: SubView):
		pushButton = subView.getButtonBarItem()
		pushButton.setParent(self.scrollAreaWidgetContents)
		pushButton.setMaximumSize(QtCore.QSize(40, 30))
		index = self.horizontalLayout.indexOf(self.horizontalSpacer)
		self.horizontalLayout.insertWidget(index, pushButton)
		pushButton.clicked.connect(partial(self.buttonClicked, subView))



if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	app.mainWindow = MainWindow()
	app.mainWindow.show()
	sys.exit(app.exec())
