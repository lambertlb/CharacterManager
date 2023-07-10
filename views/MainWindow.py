from functools import partial

from PySide6 import QtCore, QtWidgets

from builder.MainWindow_ui import Ui_MainWindow
from CharacterServices import CharacterServices
from configurator.Entity import Entity
from views.CharacterManagementView import CharacterManagementView
from views.PersonalInformationView import PersonalInformationView
from views.SubView import SubView


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

	def __init__(self, *args):
		super().__init__(*args)
		self.setupUi(self)
		self.subViews = {}
		self.startingSubView = None
		self.currentView = None
		self.loadSubViews()
		self.enableButtons(False)
		self.buttonClicked(self.startingSubView)

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
	
	def addToButtonBar(self, subView: SubView):
		pushButton = subView.getButtonBarItem()
		pushButton.setParent(self.scrollAreaWidgetContents)
		pushButton.setMaximumSize(QtCore.QSize(40, 30))
		index = self.horizontalLayout.indexOf(self.horizontalSpacer)
		self.horizontalLayout.insertWidget(index, pushButton)
		pushButton.clicked.connect(partial(self.buttonClicked, subView))

	def editCharacter(self):
		self.setWindowTitle(CharacterServices.getCharacterManager().character.PersonalInformation.Name)
		self.enableButtons(True)

	def enableButtons(self, state):
		if not state:
			self.setWindowTitle('Select Character To Edit')
		for subView in self.subViews.values():
			subView.enableButtonBarItem(state)
	
	def buttonClicked(self, newSubView):
		if self.currentView:
			self.currentView.setVisible(False)
		self.currentView = newSubView
		self.currentView.setVisible(True)
		newSubView.setupView()

	def getSubViews(self):
		views = Entity.getListOfClassesFromDirectory('./views', SubView)
		for newView in views:
			self.subViews[newView.getOrderInBar()] = newView
