#!/usr/bin/env python3

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QStyle

from UI import Ui_Main
from python_qt_hangul_input import PythonQtHangulInputFilter, HangulIndicator


class Main(QMainWindow, Ui_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.__status = 0
        self.__auto = True
        self.__hangul_input_filter = PythonQtHangulInputFilter()
        self.__hangul_input_indicator = HangulIndicator(self)

        self.__hangul_input_filter.hangul_status_changed.connect(
            self.__hangul_input_indicator.set_hangul_status
        )
        self.chkHangulInput.toggled.connect(
            self.__on_hangul_input_enabled_changed
        )
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

    # Hangul input related
    def __on_hangul_input_enabled_changed(self, enabled: bool):
        if enabled:
            self.__hangul_input_indicator.show()
            QApplication.instance().installEventFilter(
                self.__hangul_input_filter
            )
        else:
            self.__hangul_input_filter.reset()
            self.__hangul_input_indicator.hide()
            QApplication.instance().removeEventFilter(
                self.__hangul_input_filter
            )

    def __move_hangul_indicator(self):
        indicator_size = self.__hangul_input_indicator.size()
        rect = QStyle.alignedRect(
            Qt.LeftToRight, Qt.AlignBottom | Qt.AlignRight,
            indicator_size, self.geometry()
        )
        self.__hangul_input_indicator.setPosition.emit(
            rect.x(), rect.y() + indicator_size.height()
        )
    # End hangul input

    def moveEvent(self, _):
        self.__move_hangul_indicator()

    def resizeEvent(self, _):
        self.__move_hangul_indicator()


def main():
    app = QApplication()

    main = Main()
    main.show()

    app.exec()


if __name__ == "__main__":
    main()
