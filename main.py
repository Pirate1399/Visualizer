import os
# import sys
#
# from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QVBoxLayout
# from PyQt5 import QtCore

from PyQt5.QtGui import QFont, QFontDatabase, QImage, QPalette, QBrush

from datetime import datetime

################################################################################################
# Convert UI to PyQt5 py file
################################################################################################
os.system("pyuic5 interface.ui -o interface.py")

################################################################################################
# Import the generated UI
################################################################################################
from analoggaugewidget import *
from interface import *


################################################################################################
# MAIN WINDOW CLASS
################################################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        ################################################################################################
        # Setup the UI main window
        ################################################################################################
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        id = QFontDatabase.addApplicationFont('fonts/pobeda-regular1.ttf')
        if id < 0: print("Error")

        families = QFontDatabase.applicationFontFamilies(id)
        self.ui.label.setFont(QFont(families[0], 50))
        self.ui.label_2.setFont(QFont(families[0], 50))
        self.ui.label_3.setFont(QFont(families[0], 50))
        self.ui.label_4.setFont(QFont(families[0], 50))
        self.ui.label_5.setText(f'{datetime.now().date()}')
        self.ui.label_5.setFont(QFont(families[0], 40))
        self.ui.label_6.setText(f'{datetime.now().time()}')
        self.ui.label_6.setFont(QFont(families[0], 40))
        oimage = QImage('resources/sero_goluboj.jpg')
        soimage = oimage.scaled(self.size())
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(soimage))
        self.setPalette(palette)
        self.ui.widget.setGaugeTheme(3)
        self.ui.widget.set_scale_polygon_colors([[.00, Qt.red],
                                                 [.1, Qt.yellow],
                                                 [.15, Qt.green],
                                                 [1, Qt.transparent]])
        self.ui.widget.units = 'km/h'

        ################################################################################################
        # Show window
        ################################################################################################
        self.show()


########################################################################
## EXECUTE APP
########################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)

    ########################################################################
    ##
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

########################################################################
## END===>
########################################################################
