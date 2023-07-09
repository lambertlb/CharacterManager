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

	def __init__(self, entity: Entity, orderInBar, *args):
		super().__init__(*args)
		self.buttonBarItem = ButtonBarItem(self)
		self.orderInBar = orderInBar
		self.entity = entity

	def getButtonBarItem(self):
		return self.buttonBarItem

	def getOrderInBar(self):
		return self.orderInBar
	
	def getEntity(self):
		return self.entity
	
	def setupView(self):
		pass
