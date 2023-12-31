# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'class_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1220, 798, 131, 61))
        self.pushButton_2.setStyleSheet("font: 14pt \"Adobe Devanagari\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(1321, 260, 291, 71))
        self.lineEdit.setStyleSheet("font: 18pt \"Adobe Devanagari\";")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1153, 500, 161, 61))
        self.label_4.setStyleSheet("font: 24pt \"Adobe Devanagari\";")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1153, 260, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 24pt \"Adobe Devanagari\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(1321, 380, 291, 71))
        self.lineEdit_2.setStyleSheet("font: 18pt \"Adobe Devanagari\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(500, 868, 451, 150))
        self.pushButton.setStyleSheet("font: 28pt \"Adobe Devanagari\";")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(1321, 500, 291, 71))
        self.lineEdit_3.setStyleSheet("font: 18pt \"Adobe Devanagari\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 260, 900, 600))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 90, 631, 171))
        self.label.setStyleSheet("font: 48pt \"Adobe Devanagari\";")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1430, 798, 131, 61))
        self.pushButton_3.setStyleSheet("font: 14pt \"Adobe Devanagari\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1430, 908, 131, 61))
        self.pushButton_5.setStyleSheet("font: 14pt \"Adobe Devanagari\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1220, 908, 131, 61))
        self.pushButton_4.setStyleSheet("font: 14pt \"Adobe Devanagari\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1153, 380, 161, 61))
        self.label_3.setStyleSheet("font: 24pt \"Adobe Devanagari\";")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "查找"))
        self.label_4.setText(_translate("MainWindow", "学院名"))
        self.label_2.setText(_translate("MainWindow", "班号"))
        self.pushButton.setText(_translate("MainWindow", "读取当前信息"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "班号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "专业名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "学院名"))
        self.label.setText(_translate("MainWindow", "班级信息"))
        self.pushButton_3.setText(_translate("MainWindow", "添加"))
        self.pushButton_5.setText(_translate("MainWindow", "修改"))
        self.pushButton_4.setText(_translate("MainWindow", "删除"))
        self.label_3.setText(_translate("MainWindow", "专业名"))
