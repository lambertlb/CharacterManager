from PySide6.QtWidgets import QListWidgetItem
from CharacterServices import CharacterServices
from builder.Classes_ui import Ui_Form
from views.SubView import SubView


class ClassesView(SubView, Ui_Form):

	def __init__(self, *args):
		super().__init__(*args)
		self.loadingData = True
		self.setupUi(self)
		super().setupView(20)
		self.buttonBarItem.setText('Cla')

	def setupView(self):
		self.loadingData = True
		self.setEntity(CharacterServices.getCharacterManager().character.Classes)
		self.loadClasses()

	def loadClasses(self):
		self.classesListWidget.clear()
		for cls in self.entity:
			item = QListWidgetItem(cls.Class)
			self.classesListWidget.addItem(item)
		pass