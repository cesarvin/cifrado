# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from read import Ui_Read
from createDelete import Ui_CreateDelete

class Ui_Home(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(198, 100, 106);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 80, 711, 140))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo.jpeg"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.agregar = QtWidgets.QPushButton(self.frame)
        self.agregar.setStyleSheet("background-color: rgb(198, 100, 106);\n"
        "color: rgb(255, 255, 255);")
        self.agregar.setObjectName("agregar")
        self.horizontalLayout.addWidget(self.agregar)
        self.eliminar = QtWidgets.QPushButton(self.frame)
        self.eliminar.setStyleSheet("background-color: rgb(198, 100, 106);\n"
        "color: rgb(255, 255, 255);")
        self.eliminar.setObjectName("eliminar")
        self.horizontalLayout.addWidget(self.eliminar)
        self.consultar = QtWidgets.QPushButton(self.frame)
        self.consultar.setStyleSheet("background-color: rgb(198, 100, 106);\n"
        "color: rgb(255, 255, 255);")
        self.consultar.setObjectName("consultar")
        self.horizontalLayout.addWidget(self.consultar)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(40, 220, 711, 301))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(170, 60, 361, 192))
        self.tableWidget.setStyleSheet("background-color: rgb(198, 100, 106);\n"
        "color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.agregar.raise_()
        self.eliminar.raise_()
        self.consultar.raise_()
        self.tableWidget.raise_()
        self.label_2.raise_()
        self.agregar.clicked.connect(self.openCreateDelete)
        self.eliminar.clicked.connect(self.openCreateDelete)
        self.consultar.clicked.connect(self.openRead)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.agregar.setText(_translate("MainWindow", "Agregar"))
        self.eliminar.setText(_translate("MainWindow", "Eliminar"))
        self.consultar.setText(_translate("MainWindow", "Consultar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Sitio Web"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Password"))

    def openRead(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Read()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def openCreateDelete(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CreateDelete()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Home = QtWidgets.QMainWindow()
    ui = Ui_Home()
    ui.setupUi(Home)
    Home.show()
    sys.exit(app.exec_())

