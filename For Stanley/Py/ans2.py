# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\pc\Desktop\gg\ans2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_People(object):
    def setupUi(self, People):
        People.setObjectName("People")
        People.resize(400, 265)
        People.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.393323, y1:0.46, x2:0.911, y2:0.994318, stop:0.00995025 rgba(242, 255, 0, 255), stop:1 rgba(255, 121, 0, 255));")
        self.verticalLayout = QtWidgets.QVBoxLayout(People)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(People)
        self.listWidget.setMinimumSize(QtCore.QSize(378, 205))
        self.listWidget.setMaximumSize(QtCore.QSize(378, 205))
        self.listWidget.setStyleSheet("font: 63 14pt \"Cascadia Mono\";\n"
"background-color: qlineargradient(spread:pad, x1:0.482925, y1:0, x2:0.538, y2:1, stop:0.00995025 rgba(197, 221, 98, 255), stop:1 rgba(255, 157, 110, 255));")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout.addWidget(self.listWidget)
        self.pushButton = QtWidgets.QPushButton(People)
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.548, y1:0.0856364, x2:0.532701, y2:0.955, stop:0.00995025 rgba(227, 255, 113, 255), stop:1 rgba(255, 157, 110, 255));\n"
"font: 10pt \"Cascadia Mono\";")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(People)
        QtCore.QMetaObject.connectSlotsByName(People)

    def retranslateUi(self, People):
        _translate = QtCore.QCoreApplication.translate
        People.setWindowTitle(_translate("People", "Dialog"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("People", "No, no, no! NO!"))
        item = self.listWidget.item(2)
        item.setText(_translate("People", "It’s just for Stanley!"))
        item = self.listWidget.item(4)
        item.setText(_translate("People", "Go away!"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("People", "Leave"))

