from PyQt5 import QtCore
from random import randint
from time import sleep


class Speed(QtCore.QThread):
    speed =QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = 1

    def run(self):
        while True:
            self.speed.emit()
            sleep(self.delay)
