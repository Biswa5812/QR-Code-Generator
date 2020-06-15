# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QR.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import Qt,QtCore, QtGui, QtWidgets
import pyqrcode
import os
from PIL import Image
from pathlib import Path


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(607, 564)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 611, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(27, 27, 27);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(210, 90, 291, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(60, 230, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(380, 230, 131, 28))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 230, 111, 28))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(60, 160, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 150, 181, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
    
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(70, 300, 241, 231))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(350, 510, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QR Generator"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">QR_Code Generator</span></p></body></html>"))

        self.label_2.setText(_translate("Form", "Enter URL:"))
        self.label_3.setText(_translate("Form", "Save QR:"))

        self.pushButton.setText(_translate("Form", "Click to Save"))
        self.pushButton.clicked.connect(self.browse)

        self.pushButton_2.setText(_translate("Form", "Generate QR"))
        self.pushButton_2.clicked.connect(self.generateQR)

        self.label_4.setText(_translate("Form", "Site Name:"))
        self.label_5.setText(_translate("Form", "Generated Code will be displayed here"))

    def generateQR(self):

        global url,site,url_qr
        url_qr = self.lineEdit.text()
        site = self.lineEdit_2.text()

        if url_qr == "" or site == "":
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Please enter URL and Site Name")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setStandardButtons(QtWidgets.QMessageBox.Close)
            self.x = msg.exec_()
        else:
            url = pyqrcode.create(url_qr)

    def browse(self):

        try:
            self.path_1 = os.path.dirname(os.path.abspath(__file__))
            self.store_1 = os.path.join(self.path_1,"QR_Codes")

            if os.path.isdir(self.store_1):
                url.png(self.store_1 + "\\" + site + ".PNG",scale=8)
                self.label_5.setPixmap(QtGui.QPixmap(self.store_1 + "\\" + site + ".PNG"))
                self.label_5.setScaledContents(True)
                self.label_6.setText("QR Code for: " + site)
                
            else:
                os.mkdir(self.store_1)
                url.png(self.store_1 + "\\" + site + ".PNG",scale=8)
                self.label_5.setPixmap(QtGui.QPixmap(self.store_1 + "\\" + site + ".PNG"))
                self.label_5.setScaledContents(True)
                self.label_6.setText("QR Code for: " + site)
        
        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Please enter URL and Site Name and click on Generate QR")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setStandardButtons(QtWidgets.QMessageBox.Close)
            self.x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
