# pylint: disable=line-too-long, attribute-defined-outside-init

from PySide6.QtCore import QMetaObject, QCoreApplication
# from PySide6.QtGui import
from PySide6.QtWidgets import (
    QHBoxLayout, QWidget, QGroupBox, QGridLayout,
    QCheckBox, QPushButton, QLabel, QPlainTextEdit,
    QSpacerItem, QSizePolicy,
)


class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName("Main")
        Main.resize(800, 600)

        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.glCent = QGridLayout(self.centralwidget)
        self.glCent.setObjectName("glCent")


        self.gbConvert = QGroupBox(self.centralwidget)
        self.hlConvert = QHBoxLayout(self.gbConvert)

        self.hlConvert.addItem(
            QSpacerItem(616, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        )

        self.chkHangulInput = QCheckBox(self.centralwidget)
        self.chkHangulInput.setObjectName("chkHangulInput")
        self.hlConvert.addWidget(self.chkHangulInput)

        self.chkAuto = QCheckBox(self.centralwidget)
        self.chkAuto.setObjectName("chkAuto")
        self.chkAuto.setChecked(True)
        self.hlConvert.addWidget(self.chkAuto)

        self.btnTxtEscape = QPushButton(self.centralwidget)
        self.btnTxtEscape.setObjectName("btnTxtEscape")
        self.hlConvert.addWidget(self.btnTxtEscape)

        self.btnEscapeTxt = QPushButton(self.centralwidget)
        self.btnEscapeTxt.setObjectName("btnEscapeTxt")
        self.hlConvert.addWidget(self.btnEscapeTxt)

        self.glCent.addWidget(self.gbConvert)


        self.lbTest = QLabel(self.centralwidget)
        self.lbTest.setObjectName("lbTest")
        self.glCent.addWidget(self.lbTest, 1, 0)

        self.pteText = QPlainTextEdit(self.centralwidget)
        self.pteText.setObjectName("pteText")
        self.glCent.addWidget(self.pteText, 2, 0)

        self.lbEscape = QLabel(self.centralwidget)
        self.lbEscape.setObjectName("lbEscape")
        self.glCent.addWidget(self.lbEscape, 3, 0)

        self.pteEscape = QPlainTextEdit(self.centralwidget)
        self.pteEscape.setObjectName("pteEscape")
        self.glCent.addWidget(self.pteEscape, 4, 0)

        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("MainWindow", "\uc720\ub2c8\ucf54\ub4dc \ubcc0\ud658\uae30", None))
        self.gbConvert.setTitle(QCoreApplication.translate("Main", "\ubcc0\ud658", None))
        self.chkHangulInput.setText(QCoreApplication.translate("Main", "\ud55c\uae00 \uc785\ub825\uae30 \ud65c\uc131\ud654", None))
        self.chkAuto.setText(QCoreApplication.translate("Main", "\uc790\ub3d9 \ubcc0\ud658", None))
        self.btnTxtEscape.setText(QCoreApplication.translate("Main", "\ud14d\uc2a4\ud2b8\u2192Escape", None))
        self.btnEscapeTxt.setText(QCoreApplication.translate("Main", "Escape\u2192\ud14d\uc2a4\ud2b8", None))
        self.lbTest.setText(QCoreApplication.translate("Main", "\uc6d0\ubcf8 \ud14d\uc2a4\ud2b8", None))
        self.lbEscape.setText(QCoreApplication.translate("Main", "Unicode Escape", None))
    # retranslateUi
