# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'read.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from db import *

class Ui_Read(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(198, 100, 106);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 60, 711, 140))
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
        self.consultar = QtWidgets.QPushButton(self.frame)
        self.consultar.setStyleSheet("background-color: rgb(198, 100, 106);\n"
"color: rgb(255, 255, 255);")
        self.consultar.setObjectName("consultar")
        self.horizontalLayout.addWidget(self.consultar)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(40, 200, 711, 211))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.sitio = QtWidgets.QTextEdit(self.frame_2)
        self.sitio.setGeometry(QtCore.QRect(290, 30, 291, 31))
        self.sitio.setObjectName("sitio")
        self.password = QtWidgets.QTextEdit(self.frame_2)
        self.password.setGeometry(QtCore.QRect(290, 120, 291, 31))
        self.password.setObjectName("password")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(80, 40, 111, 16))
        self.label.setStyleSheet("font: 14pt;")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(80, 130, 151, 16))
        self.label_3.setStyleSheet("font: 14pt;")
        self.label_3.setObjectName("label_3")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(40, 410, 711, 140))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setGeometry(QtCore.QRect(175, 60, 361, 50))
        self.tableWidget.setStyleSheet("background-color: rgb(198, 100, 106);\n"
        "color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        # self.tableWidget.setColumnCount(2)
        # self.tableWidget.setRowCount(0)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(1, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.consultar.clicked.connect(self.consulta)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.consultar.setText(_translate("MainWindow", "Consultar"))
        self.label.setText(_translate("MainWindow", "Sitio Web"))
        self.label_3.setText(_translate("MainWindow", "Contraseña Maestra"))
        # item = self.tableWidget.horizontalHeaderItem(0)
        # item.setText(_translate("MainWindow", "Sitio Web"))
        # item = self.tableWidget.horizontalHeaderItem(1)
        # item.setText(_translate("MainWindow", "Password"))

    def consulta(self):
        self.tableWidget.setRowCount(0)
        sitio_buscar = self.sitio.toPlainText()
        password_principal = self.password.toPlainText()
        Find_Values(sitio_buscar, 0)


        try:
        #coneccion a la db, la crea si no existe
            cnn = conection(db_file)
                

            c = cnn.cursor()

            c.execute("SELECT pass FROM All_info WHERE Page = ?", (sitio_buscar,))
            data=c.fetchall()
            if len(data)==0:

                # if (acc==0):
                print('There is no component named %s'%sitio_buscar)
            
                return True
            else:
                print('El registro existe -- siguiendo con la operacion ')
                #if (acc==0):
                    
                # password = str(data[0])
                self.tableWidget.setColumnCount(len(data[0]))
                for i in range(len(data)):
                    self.tableWidget.insertRow(i)
                    for j in range(len(data[0])):
                        print(i, j)
                        self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(data[i][j]))
                # print ('Password is ', password[2:-3])
                return None
            cnn.commit()
            cnn.close()

        except Error as e: 
            print(e)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Read()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
