# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(784, 583)
        MainWindow.setStyleSheet(u"background-color: rgb(99, 99, 99);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ButtonStart = QPushButton(self.centralwidget)
        self.ButtonStart.setObjectName(u"ButtonStart")
        self.ButtonStart.setEnabled(True)
        self.ButtonStart.setGeometry(QRect(20, 30, 151, 141))
        self.ButtonStart.setStyleSheet(u"background-color: rgb(117, 126, 127);")
        icon = QIcon(QIcon.fromTheme(u"appointment-soon"))
        self.ButtonStart.setIcon(icon)
        self.ButtonStart.setCheckable(True)
        self.ButtonStart.setFlat(False)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(620, 520, 141, 41))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.Speed = QLabel(self.centralwidget)
        self.Speed.setObjectName(u"Speed")
        self.Speed.setGeometry(QRect(210, 150, 181, 41))
        font = QFont()
        font.setPointSize(24)
        self.Speed.setFont(font)
        self.labelSpeed = QLabel(self.centralwidget)
        self.labelSpeed.setObjectName(u"labelSpeed")
        self.labelSpeed.setGeometry(QRect(410, 150, 181, 41))
        self.labelSpeed.setFont(font)
        self.labelSpeed.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.Date = QLabel(self.centralwidget)
        self.Date.setObjectName(u"Date")
        self.Date.setGeometry(QRect(230, 20, 241, 41))
        self.Date.setFont(font)
        self.labelDate = QLabel(self.centralwidget)
        self.labelDate.setObjectName(u"labelDate")
        self.labelDate.setGeometry(QRect(450, 20, 181, 41))
        self.labelDate.setFont(font)
        self.labelDate.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.Date2 = QLabel(self.centralwidget)
        self.Date2.setObjectName(u"Date2")
        self.Date2.setGeometry(QRect(230, 70, 241, 41))
        self.Date2.setFont(font)
        self.labelDate_2 = QLabel(self.centralwidget)
        self.labelDate_2.setObjectName(u"labelDate_2")
        self.labelDate_2.setGeometry(QRect(450, 70, 181, 41))
        self.labelDate_2.setFont(font)
        self.labelDate_2.setStyleSheet(u"color: rgb(255, 170, 0);")
        self.Actual_lineal_meters = QLabel(self.centralwidget)
        self.Actual_lineal_meters.setObjectName(u"Actual_lineal_meters")
        self.Actual_lineal_meters.setGeometry(QRect(118, 220, 261, 41))
        font1 = QFont()
        font1.setPointSize(20)
        self.Actual_lineal_meters.setFont(font1)
        self.labelSpeed_2 = QLabel(self.centralwidget)
        self.labelSpeed_2.setObjectName(u"labelSpeed_2")
        self.labelSpeed_2.setGeometry(QRect(410, 220, 181, 41))
        self.labelSpeed_2.setFont(font)
        self.labelSpeed_2.setStyleSheet(u"color: rgb(0, 0, 255);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.ButtonStart.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ButtonStart.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.Speed.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c:", None))
        self.labelSpeed.setText(QCoreApplication.translate("MainWindow", u"0000", None))
        self.Date.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0442\u0435\u043a\u0443\u0449\u0430\u044f", None))
        self.labelDate.setText(QCoreApplication.translate("MainWindow", u"0000", None))
        self.Date2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0442\u0435\u043a\u0443\u0449\u0430\u044f", None))
        self.labelDate_2.setText(QCoreApplication.translate("MainWindow", u"0000", None))
        self.Actual_lineal_meters.setText(QCoreApplication.translate("MainWindow", u"Actual_lineal_meters", None))
        self.labelSpeed_2.setText(QCoreApplication.translate("MainWindow", u"0000", None))
    # retranslateUi

