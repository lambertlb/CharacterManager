# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Attributes.ui'
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
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(887, 653)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.attributeGrid = QGridLayout()
        self.attributeGrid.setObjectName(u"attributeGrid")

        self.horizontalLayout.addLayout(self.attributeGrid)

        self.bonusGrid = QGridLayout()
        self.bonusGrid.setObjectName(u"bonusGrid")
        self.strengthBonusEdit = QLineEdit(self.frame)
        self.strengthBonusEdit.setObjectName(u"strengthBonusEdit")
        self.strengthBonusEdit.setReadOnly(True)

        self.bonusGrid.addWidget(self.strengthBonusEdit, 1, 2, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.bonusGrid.addWidget(self.label_7, 5, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.bonusGrid.addWidget(self.label_2, 7, 0, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.bonusGrid.addWidget(self.label_6, 4, 0, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.bonusGrid.addWidget(self.label_4, 2, 0, 1, 1)

        self.constitutionBonusEdit = QLineEdit(self.frame)
        self.constitutionBonusEdit.setObjectName(u"constitutionBonusEdit")
        self.constitutionBonusEdit.setReadOnly(True)

        self.bonusGrid.addWidget(self.constitutionBonusEdit, 3, 2, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.bonusGrid.addWidget(self.label_8, 6, 0, 1, 1)

        self.wisdomBonusEdit = QLineEdit(self.frame)
        self.wisdomBonusEdit.setObjectName(u"wisdomBonusEdit")
        self.wisdomBonusEdit.setReadOnly(True)

        self.bonusGrid.addWidget(self.wisdomBonusEdit, 5, 2, 1, 1)

        self.intelligenceBonusEdit = QLineEdit(self.frame)
        self.intelligenceBonusEdit.setObjectName(u"intelligenceBonusEdit")
        self.intelligenceBonusEdit.setReadOnly(True)

        self.bonusGrid.addWidget(self.intelligenceBonusEdit, 4, 2, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.bonusGrid.addWidget(self.label_5, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.bonusGrid.addItem(self.verticalSpacer_2, 8, 2, 1, 1)

        self.charismaBonusEdit = QLineEdit(self.frame)
        self.charismaBonusEdit.setObjectName(u"charismaBonusEdit")
        self.charismaBonusEdit.setReadOnly(True)

        self.bonusGrid.addWidget(self.charismaBonusEdit, 6, 2, 1, 1)

        self.dexterityBonusEdit = QLineEdit(self.frame)
        self.dexterityBonusEdit.setObjectName(u"dexterityBonusEdit")
        self.dexterityBonusEdit.setReadOnly(True)

        self.bonusGrid.addWidget(self.dexterityBonusEdit, 2, 2, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.bonusGrid.addWidget(self.label_3, 1, 0, 1, 1)

        self.buyPointsEdit = QLineEdit(self.frame)
        self.buyPointsEdit.setObjectName(u"buyPointsEdit")
        self.buyPointsEdit.setReadOnly(True)

        self.bonusGrid.addWidget(self.buyPointsEdit, 7, 2, 1, 1)


        self.horizontalLayout.addLayout(self.bonusGrid)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Wisdom Bonus:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Buy Points Spent:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Intelligence Bonus:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Dexterity Bonus:", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Charisma Bonus:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Constitution Bonus:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Strength Bonus:", None))
    # retranslateUi

