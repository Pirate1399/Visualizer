import os

import sys


from PySide6.QtWidgets import QMainWindow, QWidget, QApplication
from PySide6.QtGui import QFont, QFontDatabase

from interface import *

os.system("PySide6-uic interface.ui -o interface.py")

class MainWindow(QMainWindow):
    def _init_(self, parent=None):
        QMainWindow._init_(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.show()

if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()

    app.exec()