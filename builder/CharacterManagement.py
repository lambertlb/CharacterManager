# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CharacterManagement.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 306)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 274, 264))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.characterListWidget = QListWidget(self.scrollAreaWidgetContents)
        self.characterListWidget.setObjectName(u"characterListWidget")

        self.verticalLayout.addWidget(self.characterListWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.createCharacterButton = QPushButton(self.frame)
        self.createCharacterButton.setObjectName(u"createCharacterButton")

        self.gridLayout_3.addWidget(self.createCharacterButton, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.newCharacterNameText = QLineEdit(self.frame)
        self.newCharacterNameText.setObjectName(u"newCharacterNameText")

        self.gridLayout_3.addWidget(self.newCharacterNameText, 1, 0, 1, 1)

        self.loadCharacterButton = QPushButton(self.frame)
        self.loadCharacterButton.setObjectName(u"loadCharacterButton")

        self.gridLayout_3.addWidget(self.loadCharacterButton, 0, 0, 1, 1)

        self.deleteCharacterButton = QPushButton(self.frame)
        self.deleteCharacterButton.setObjectName(u"deleteCharacterButton")

        self.gridLayout_3.addWidget(self.deleteCharacterButton, 3, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_3)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.createCharacterButton.setText(QCoreApplication.translate("Form", u"Create Character", None))
        self.newCharacterNameText.setPlaceholderText(QCoreApplication.translate("Form", u"Enter new Character Name", None))
        self.loadCharacterButton.setText(QCoreApplication.translate("Form", u"Load Selected Character", None))
        self.deleteCharacterButton.setText(QCoreApplication.translate("Form", u"Delete Selected Character", None))
    # retranslateUi

