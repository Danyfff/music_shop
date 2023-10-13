# import sys
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import pyqtSignal
from client.ui.login_form_ui import Ui_MainWindow as Ui_logginForm


class LogginForm(QMainWindow, Ui_logginForm):

    login_corent = pyqtSignal(int, int)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.push_login.clicked.connect(self.check_login)
        self.push_cancel.clicked.connect(self.exit)

    def check_login(self):
        id = 1
        post = 1
        if not id:
            print('Такого пользователя нет')
            return
        print('вот так')
        self.login_corent.emit(id, post)
        self.close()

    def exit(self):
        self.close()
