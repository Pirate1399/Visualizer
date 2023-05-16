from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import QFileDialog

from MainWindow import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)
        self.FILE = None
        self.Window = Ui_MainWindow()
        self.Window.setupUi(self)
        self.initSignals()

    def initSignals(self):
        self.Window.pushButton.clicked.connect(self.change_file)
        self.Window.ButtonStart.clicked.connect(self.showParametrs)

    def change_file(self):
        file = QFileDialog.getOpenFileName(self, filter='*.dat')
        path = file[0]
        with open(fr'{path}') as f:
            self.FILE = f.read()
        f.close()

    def showParametrs(self, status):

        if status:
            if self.FILE is None:
                print("Нужно выбрать файл")
            else:
                self.Window.labelDate.setText(self.FILE[4:12])
                self.Window.labelDate_2.setText(self.FILE[50:58])
                self.Window.labelSpeed.setText(self.FILE[84:90])
                self.Window.labelSpeed_2.setText(self.FILE[64:74])
        else:
            self.Window.labelDate.setText("Нет данных")
            self.Window.labelDate_2.setText("Нет данных")
            self.Window.labelSpeed.setText("Нет данных")
            self.Window.labelSpeed_2.setText("Нет данных")












if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()