# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Classes.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(952, 555)
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
        self.classesListWidget = QListWidget(self.frame)
        self.classesListWidget.setObjectName(u"classesListWidget")

        self.gridLayout.addWidget(self.classesListWidget, 3, 0, 1, 2)

        self.addClassButton = QPushButton(self.frame)
        self.addClassButton.setObjectName(u"addClassButton")

        self.gridLayout.addWidget(self.addClassButton, 2, 0, 1, 1)

        self.classesComboBox = QComboBox(self.frame)
        self.classesComboBox.setObjectName(u"classesComboBox")

        self.gridLayout.addWidget(self.classesComboBox, 2, 1, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pointsSpentLabel = QLabel(self.frame)
        self.pointsSpentLabel.setObjectName(u"pointsSpentLabel")

        self.gridLayout.addWidget(self.pointsSpentLabel, 1, 0, 1, 1)

        self.pointsSpentEdit = QLineEdit(self.frame)
        self.pointsSpentEdit.setObjectName(u"pointsSpentEdit")
        self.pointsSpentEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.pointsSpentEdit, 1, 1, 1, 1)


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
        self.addClassButton.setText(QCoreApplication.translate("Form", u"Add Class", None))
        self.label.setText(QCoreApplication.translate("Form", u"Classes", None))
        self.pointsSpentLabel.setText(QCoreApplication.translate("Form", u"Points Spent", None))
    # retranslateUi

