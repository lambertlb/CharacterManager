# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PersonalInformation.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(735, 566)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.characterNameLabel = QLabel(self.frame)
        self.characterNameLabel.setObjectName(u"characterNameLabel")

        self.gridLayout.addWidget(self.characterNameLabel, 0, 0, 1, 1)

        self.ageEdit = QLineEdit(self.frame)
        self.ageEdit.setObjectName(u"ageEdit")
        self.ageEdit.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)

        self.gridLayout.addWidget(self.ageEdit, 2, 1, 1, 1)

        self.alignmentLabel = QLabel(self.frame)
        self.alignmentLabel.setObjectName(u"alignmentLabel")

        self.gridLayout.addWidget(self.alignmentLabel, 3, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.raceComboBox = QComboBox(self.frame)
        self.raceComboBox.setObjectName(u"raceComboBox")

        self.gridLayout.addWidget(self.raceComboBox, 1, 1, 1, 1)

        self.raceLabel = QLabel(self.frame)
        self.raceLabel.setObjectName(u"raceLabel")

        self.gridLayout.addWidget(self.raceLabel, 1, 0, 1, 1)

        self.alignmentComboBox = QComboBox(self.frame)
        self.alignmentComboBox.setObjectName(u"alignmentComboBox")

        self.gridLayout.addWidget(self.alignmentComboBox, 3, 1, 1, 1)

        self.ageLabel = QLabel(self.frame)
        self.ageLabel.setObjectName(u"ageLabel")

        self.gridLayout.addWidget(self.ageLabel, 2, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout.addWidget(self.textEdit)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.characterNameLabel.setText(QCoreApplication.translate("Form", u"Character Name:", None))
        self.alignmentLabel.setText(QCoreApplication.translate("Form", u"Alignment:", None))
        self.raceLabel.setText(QCoreApplication.translate("Form", u"Race:", None))
        self.ageLabel.setText(QCoreApplication.translate("Form", u"Age:", None))
    # retranslateUi

