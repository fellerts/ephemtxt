#!/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QFont, QKeyEvent, QTextOption, QFontMetricsF
import qdarktheme

class PlainTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super(PlainTextEdit, self).__init__(parent)
        # Remove focus border
        self.setStyleSheet("QTextEdit { outline: none; }")
        # Allow whatever size the user wants
        self.setMinimumSize(1, 1)

    def insertFromMimeData(self, source):
        if source.hasText(): # Insert as plain text
            self.insertPlainText(source.text())

    def resetCursorBlink(self):
        cursor = self.textCursor()
        self.setTextCursor(cursor)

class EphemeralTextWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMinimumSize(1, 1)

    def initUI(self):
        monospaceFont = QFont("Monospace")
        self.textEdit = PlainTextEdit(self)
        self.textEdit.setFont(monospaceFont)
        self.textEdit.setWordWrapMode(QTextOption.WrapAtWordBoundaryOrAnywhere)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.installEventFilter(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(100, 100, 300, 150)

        # Fix tabs not aligning with n spaces
        # https://forum.qt.io/topic/91327/tabs-not-working-as-intended-for-monospace-font-on-linux/3
        char_width = QFontMetricsF(self.textEdit.font()).width(' ')
        text_option = QTextOption()
        text_option.setTabStop(char_width * 4) # tab = 4 spaces wide
        self.textEdit.document().setDefaultTextOption(text_option)

        self.show()

    def resizeEvent(self, event):
        self.textEdit.resize(self.size())
        super(EphemeralTextWidget, self).resizeEvent(event)

def main():
    qdarktheme.enable_hi_dpi()
    app = QApplication(sys.argv)
    qdarktheme.setup_theme("auto")
    ephemtxt = EphemeralTextWidget()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()