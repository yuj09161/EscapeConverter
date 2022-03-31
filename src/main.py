#!/usr/bin/env python3

from PySide6.QtWidgets import QMainWindow, QApplication

from UI import Ui_Main


class Main(QMainWindow, Ui_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.__status = 0
        self.__auto = True

        self.chkAuto.stateChanged.connect(self.__set_auto)
        self.btnTxtEscape.clicked.connect(lambda: self.__text_escape(True))
        self.btnEscapeTxt.clicked.connect(lambda: self.__escape_text(True))
        self.pteText.textChanged.connect(self.__text_escape)
        self.pteEscape.textChanged.connect(self.__escape_text)

    def __set_auto(self, state):
        self.__auto = bool(state)

    def __text_escape(self, convert=False):
        if not self.__status and (self.__auto or convert):
            self.__status = 1
            self.pteEscape.setPlainText(
                self.pteText.toPlainText()
                    .encode('unicode-escape').decode('ascii')
                    .replace('\\n', '\n')
            )
            self.__status = 0

    def __escape_text(self, convert=False):
        if not self.__status and (self.__auto or convert):
            self.__status = 2
            self.pteText.setPlainText(
                self.pteEscape.toPlainText()
                    .encode('ascii').decode('unicode-escape')
            )
            self.__status = 0


def main():
    app = QApplication()

    main = Main()
    main.show()

    app.exec()


if __name__ == "__main__":
    main()
