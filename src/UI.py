# pylint: disable=line-too-long, attribute-defined-outside-init

from PySide6.QtCore import QMetaObject, QCoreApplication
# from PySide6.QtGui import
from PySide6.QtWidgets import (
    QWidget, QGroupBox, QGridLayout,
    QCheckBox, QPushButton, QLabel, QPlainTextEdit,
    QSpacerItem, QSizePolicy,
)


class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(800, 600)

        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.glCent = QGridLayout(self.centralwidget)
        self.glCent.setObjectName(u"glCent")


        self.gbConvert = QGroupBox(self.centralwidget)
        self.glConvert = QGridLayout(self.gbConvert)

        self.glConvert.addItem(
            QSpacerItem(616, 20, QSizePolicy.Expanding, QSizePolicy.Minimum),
            0, 0, 1, 1
        )

        self.chkAuto = QCheckBox(self.centralwidget)
        self.chkAuto.setObjectName(u"chkAuto")
        self.chkAuto.setChecked(True)
        self.glConvert.addWidget(self.chkAuto, 0, 1, 1, 1)

        self.btnTxtEscape = QPushButton(self.centralwidget)
        self.btnTxtEscape.setObjectName(u"btnTxtEscape")
        self.glConvert.addWidget(self.btnTxtEscape, 0, 2, 1, 1)

        self.btnEscapeTxt = QPushButton(self.centralwidget)
        self.btnEscapeTxt.setObjectName(u"btnEscapeTxt")
        self.glConvert.addWidget(self.btnEscapeTxt, 0, 3, 1, 1)

        self.glCent.addWidget(self.gbConvert, 0, 0, 1, 1)


        self.lbTest = QLabel(self.centralwidget)
        self.lbTest.setObjectName(u"lbTest")
        self.glCent.addWidget(self.lbTest, 1, 0)

        self.pteText = QPlainTextEdit(self.centralwidget)
        self.pteText.setObjectName(u"pteText")
        self.glCent.addWidget(self.pteText, 2, 0)

        self.lbEscape = QLabel(self.centralwidget)
        self.lbEscape.setObjectName(u"lbEscape")
        self.glCent.addWidget(self.lbEscape, 3, 0)

        self.pteEscape = QPlainTextEdit(self.centralwidget)
        self.pteEscape.setObjectName(u"pteEscape")
        self.glCent.addWidget(self.pteEscape, 4, 0)

        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("MainWindow", u"\uc720\ub2c8\ucf54\ub4dc \ubcc0\ud658\uae30", None))
        self.gbConvert.setTitle(QCoreApplication.translate("Main", u"\ubcc0\ud658", None))
        self.chkAuto.setText(QCoreApplication.translate("Main", u"\uc790\ub3d9 \ubcc0\ud658", None))
        self.btnTxtEscape.setText(QCoreApplication.translate("Main", u"\ud14d\uc2a4\ud2b8\u2192Escape", None))
        self.btnEscapeTxt.setText(QCoreApplication.translate("Main", u"Escape\u2192\ud14d\uc2a4\ud2b8", None))
        self.lbTest.setText(QCoreApplication.translate("Main", u"\uc6d0\ubcf8 \ud14d\uc2a4\ud2b8", None))
        self.lbEscape.setText(QCoreApplication.translate("Main", u"Unicode Escape", None))
    # retranslateUi
