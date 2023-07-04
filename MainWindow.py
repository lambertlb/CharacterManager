from functools import partial
import sys

from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QMainWindow, QPushButton

from generated.MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

	def __init__(self, *args):
		super().__init__(*args)
		self.setupUi(self)
		for i in range(20):
			pushButton = QPushButton(self.scrollAreaWidgetContents_2)
			pushButton.setText(f'Btn{i}')
			pushButton.setMaximumSize(QtCore.QSize(40, 30))
			index = self.horizontalLayout_2.indexOf(self.horizontalSpacer)
			self.horizontalLayout_2.insertWidget(index, pushButton)
			pushButton.clicked.connect(partial(self.buttonClicked, i))

	def buttonClicked(self, which):
		print(f'Button {which} Clicked')

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	app.mainWindow = MainWindow()
	app.mainWindow.show()
	sys.exit(app.exec())
