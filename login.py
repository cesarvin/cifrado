# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(198, 100, 106);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(230, 120, 351, 331))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 190, 241, 16))
        self.label.setObjectName("label")
        self.masterPassword = QtWidgets.QTextEdit(self.frame)
        self.masterPassword.setGeometry(QtCore.QRect(40, 220, 261, 31))
        self.masterPassword.setStyleSheet("")
        self.masterPassword.setObjectName("masterPassword")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 281, 121))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../../Downloads/logo.jpeg"))
        self.label_2.setObjectName("label_2")
        self.ingresar = QtWidgets.QPushButton(self.frame)
        self.ingresar.setGeometry(QtCore.QRect(120, 270, 113, 32))
        self.ingresar.setStyleSheet("background-color: rgb(198, 100, 106);\n"
"color: rgb(255, 255, 255);")
        self.ingresar.setObjectName("ingresar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Contraseña maestra"))
        self.ingresar.setText(_translate("MainWindow", "Ingresar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

