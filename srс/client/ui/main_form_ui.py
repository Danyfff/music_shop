# Form implementation generated from reading ui file 'main_form.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(756, 565)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_add_fio = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.line_add_fio.setObjectName("line_add_fio")
        self.verticalLayout.addWidget(self.line_add_fio)
        self.line_add_phone = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.line_add_phone.setObjectName("line_add_phone")
        self.verticalLayout.addWidget(self.line_add_phone)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.Button_add = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Button_add.setObjectName("Button_add")
        self.horizontalLayout.addWidget(self.Button_add)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.line_add_email = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.line_add_email.setObjectName("line_add_email")
        self.verticalLayout_2.addWidget(self.line_add_email)
        self.line_add_address = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.line_add_address.setObjectName("line_add_address")
        self.verticalLayout_2.addWidget(self.line_add_address)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Button_delite = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Button_delite.setObjectName("Button_delite")
        self.verticalLayout_3.addWidget(self.Button_delite)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 756, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.line_add_fio.setPlaceholderText(_translate("MainWindow", "ФИО"))
        self.line_add_phone.setPlaceholderText(_translate("MainWindow", "Телефон"))
        self.Button_add.setText(_translate("MainWindow", "Добавить "))
        self.line_add_email.setPlaceholderText(_translate("MainWindow", "Почта"))
        self.line_add_address.setPlaceholderText(_translate("MainWindow", "Аддрес"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ФИО"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Телефон"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Почта"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Аддрес"))
        self.Button_delite.setText(_translate("MainWindow", "Удалить"))
