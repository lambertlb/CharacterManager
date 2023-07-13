from PySide6.QtWidgets import QListWidgetItem
from CharacterServices import CharacterServices
from builder.Classes_ui import Ui_Form
from views.SubView import SubView


class ClassesView(SubView, Ui_Form):

	def __init__(self, *args):
		super().__init__(*args)
		self.loadingData = True
		self.selectedClass = None
		self.classToDelete = None
		self.setupUi(self)
		super().setupView(30)
		self.buttonBarItem.setText('Cla')
		self.classesComboBox.currentTextChanged.connect(self.classComboSelected)
		self.classesListWidget.itemClicked.connect(self.classSelected)
		self.addClassButton.clicked.connect(self.addSelectedClass)
		self.deleteClassButton.clicked.connect(self.deleteSelectedClass)

	def setupView(self):
		self.loadingData = True
		self.addClassButton.setEnabled(False)
		self.deleteClassButton.setEnabled(False)
		self.setEntity(CharacterServices.getCharacterManager().character.ClassInformation.Classes)
		self.loadAllClasses()
		self.loadClassesFromCharacter()
		self.loadingData = False

	def loadAllClasses(self):
		self.classesComboBox.clear()
		classes = CharacterServices.getCharacterManager().getListOfAllClasses()
		self.classesComboBox.addItem('Select Class', None)
		for cls in classes:
			self.classesComboBox.addItem(cls._name, cls)

	def loadClassesFromCharacter(self):
		self.classesListWidget.clear()
		for cls in self.entity:
			item = QListWidgetItem(cls.Class)
			item.setData(1,cls)
			self.classesListWidget.addItem(item)

	def classComboSelected(self, item):
		if self.loadingData:
			return
		cls = self.classesComboBox.currentData()
		self.textEdit.setText('')
		if cls:
			self.textEdit.setText(cls._description)
		self.selectClass(cls)

	def classSelected(self, item: QListWidgetItem):
		if self.loadingData:
			return
		cls = item.data(1)
		self.textEdit.setText(cls._classScript._description)
		self.selectClassToDelete(cls)
		pass

	def selectClass(self, cls):
		self.selectedClass = cls
		enabled = cls is not None
		self.addClassButton.setEnabled(enabled)

	def selectClassToDelete(self, cls):
		self.classToDelete = cls
		enabled = cls is not None
		self.deleteClassButton.setEnabled(enabled)

	def addSelectedClass(self):
		if self.selectedClass:
			CharacterServices.getCharacterManager().addClass(self.selectedClass)
			self.setupView()

	def deleteSelectedClass(self):
		if self.classToDelete:
			CharacterServices.getCharacterManager().deleteClass(self.classToDelete)
			self.setupView()
	