# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createDelete.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from db import *


class Ui_Create(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(198, 100, 106);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 100, 711, 140))
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
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(40, 240, 711, 271))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.sitio = QtWidgets.QTextEdit(self.frame_2)
        self.sitio.setGeometry(QtCore.QRect(290, 70, 291, 31))
        self.sitio.setObjectName("sitio")
        self.password = QtWidgets.QTextEdit(self.frame_2)
        self.password.setGeometry(QtCore.QRect(290, 150, 291, 31))
        self.password.setObjectName("password")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(150, 80, 111, 16))
        self.label.setStyleSheet("font: 14pt;")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(150, 160, 121, 16))
        self.label_3.setStyleSheet("font: 14pt;")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.agregar.clicked.connect(self.agregar_sitio)
        self.eliminar.clicked.connect(self.eliminar_sitio)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.agregar.setText(_translate("MainWindow", "Agregar"))
        self.eliminar.setText(_translate("MainWindow", "Eliminar"))
        self.label.setText(_translate("MainWindow", "Sitio Web"))
        self.label_3.setText(_translate("MainWindow", "Contraseña"))

    def agregar_sitio(self):
        sitio_nuevo = self.sitio.toPlainText()
        password_nuevo = self.password.toPlainText()
        Set_Values(sitio_nuevo, password_nuevo)

    def eliminar_sitio(self):
        sitio_eliminar = self.sitio.toPlainText()
        Delete_values(sitio_eliminar)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Create = QtWidgets.QMainWindow()
    ui = Ui_Create()
    ui.setupUi(Create)
    Create.show()
    sys.exit(app.exec_())
