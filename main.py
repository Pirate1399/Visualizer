import os
import sys

from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QVBoxLayout
from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QFontDatabase, QImage, QPalette, QBrush
from datetime import datetime

from Threads import Speed



os.system("pyuic5 interface.ui -o interface.py")

from analoggaugewidget import *
from interface import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.startThreads()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        """Установка шрифтов на лейблы"""

        id = QFontDatabase.addApplicationFont('fonts/pobeda-regular1.ttf')
        if id < 0: print("Error")

        id2 = QFontDatabase.addApplicationFont('fonts/Disket-Mono-Bold.ttf')  # жирный

        families = QFontDatabase.applicationFontFamilies(id)
        boldfamilies = QFontDatabase.applicationFontFamilies(id2)
        self.ui.label.setFont(QFont(boldfamilies[0], 27))
        self.ui.label_2.setFont(QFont(boldfamilies[0], 25))
        self.ui.label_3.setFont(QFont(boldfamilies[0], 25))
        self.ui.label_4.setFont(QFont(boldfamilies[0], 25))
        self.ui.label_5.setFont(QFont(boldfamilies[0], 50))
        self.ui.label_6.setFont(QFont(boldfamilies[0], 35))
        self.ui.label_7.setFont(QFont(boldfamilies[0], 50))
        self.ui.label_8.setFont(QFont(boldfamilies[0], 50))
        self.ui.label_9.setFont(QFont(boldfamilies[0], 50))
        self.ui.label_9.setFont(QFont(boldfamilies[0], 50))
        self.ui.label_10.setFont(QFont(boldfamilies[0], 50))
        win_size = self.size()
        self.setMinimumSize(win_size)

        # self.ui.label.resizeEvent(QResizeEvent.size)

        """Установка заднего фона окна"""

        oimage = QImage('resources/sero_goluboj.jpg')
        soimage = oimage.scaled(self.size())
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(soimage))
        self.setPalette(palette)

        """Установка темы спидометра + внешний радиус"""
        self.ui.widget.setGaugeTheme(3)
        self.ui.widget.set_scale_polygon_colors([[.00, Qt.red],
                                                 [.1, Qt.yellow],
                                                 [.15, Qt.green],
                                                 [1, Qt.transparent]])
        self.ui.widget.units = 'mm/s'
        self.ui.widget.setMouseTracking(False)

        self.initSignals()




    def startThreads(self):
        self.speed = Speed()
        self.speed.start()

    def initSignals(self):
        self.speed.speed.connect(self.update)

    def update(self):
        FILE = ""
        with open('C:\\Users\\stasu\\Desktop\\status.dat', 'r') as f: #TODO Здесь прописать путь к файлу
            FILE = f.read()
            f.close()
        self.ui.widget.setMaxValue(int(FILE[96:99]))
        self.cspeed = int(FILE[84:87]) #currentSpeed
        self.ui.widget.updateValue(self.cspeed)
        self.ui.label_5.setText(FILE[12:14]+":"+FILE[14:16])#time
        self.ui.label_6.setText(FILE[10:12]+"-"+FILE[8:10]+"-"+FILE[4:8])
        self.ui.label_7.setText(f'{int(FILE[120:126])}') #ActualCustomer
        self.ui.label_8.setText(f'{int(FILE[64:74])%1000000}') #Actual_lineal
        self.ui.label_9.setText(f'{int(FILE[120:126])}') #cuts_customer_1
        self.ui.label_10.setText(f'{int(FILE[127:133])}') #Actual_cuts_customer_2


        # self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.showFullScreen()
    sys.exit(app.exec_())

