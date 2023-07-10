from typing import Optional
from PySide6 import QtWidgets
import PySide6.QtCore
import PySide6.QtWidgets

from configurator.Entity import Entity

class ButtonBarItem(QtWidgets.QPushButton):
	def __init__(self, subView, *args):
		super().__init__(*args)
		self.subView = subView

class SubView(QtWidgets.QWidget):

	def __init__(self, *args):
		super().__init__(*args)
		self.buttonBarItem = ButtonBarItem(self)
		self.orderInBar = 0
		self.entity = None

	def setEntity(self, value):
		self.entity = value
	
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
