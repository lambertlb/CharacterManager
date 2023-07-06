from PySide6 import QtWidgets

from builder.CharacterManagement_ui import Ui_Form
from CharacterServices import CharacterServices


class CharacterManagementView(QtWidgets.QWidget, Ui_Form):

	def __init__(self, *args):
		super().__init__(*args)
		self.fileToLoad = None
		self.setupUi(self)
		self.findCharacters()
		self.characterListWidget.currentItemChanged.connect(self.characterSelected)
		self.characterListWidget.itemDoubleClicked.connect(self.doubleClicked)
		self.loadCharacterButton.clicked.connect(self.loadCharacter)
		self.createCharacterButton.clicked.connect(self.createCharacter)
		self.newCharacterNameText.textChanged.connect(self.characterNameChanged)
		self.deleteCharacterButton.clicked.connect(self.deleteCharacter)

	def findCharacters(self):
		self.loadCharacterButton.setEnabled(False)
		self.createCharacterButton.setEnabled(False)
		self.deleteCharacterButton.setEnabled(False)
		self.characterListWidget.clear()
		self.newCharacterNameText.setText('')
		characters = CharacterServices.getCharacterManager().existingCharacters()
		for character in characters:
			name, path, characterData = character
			item = QtWidgets.QListWidgetItem(name, self.characterListWidget)
			item.setData(1, path)
		pass

	def characterSelected(self, curr : QtWidgets.QListWidgetItem, prev):
		self.fileToLoad = curr.data(1)
		self.loadCharacterButton.setEnabled(True)
		self.deleteCharacterButton.setEnabled(True)

	def doubleClicked(self):
		items = self.characterListWidget.selectedItems()
		self.fileToLoad = items[0].data(1)
		self.loadCharacter()

	def loadCharacter(self):
		CharacterServices.getCharacterManager().loadCharacterFromFile(self.fileToLoad)
		CharacterServices.getRootWindow().editCharacter()
	
	def createCharacter(self):
		CharacterServices.getCharacterManager().createNewCharacter(self.newCharacterNameText.text())
		self.findCharacters()

	def characterNameChanged(self):
		newName = self.newCharacterNameText.text()
		if len(newName) > 3:
			self.createCharacterButton.setEnabled(True)

	def deleteCharacter(self):
		CharacterServices.getCharacterManager().deleteCharacter(self.fileToLoad)
		self.findCharacters()
