# import sys
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import pyqtSignal
from client.ui.main_form_ui import Ui_MainWindow as Ui_MainForm


class MainForm(QMainWindow, Ui_MainForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


    def set_user_data(self, bayer_id: int, bayer_fio: str):
        self.bayer_id = bayer_id
        self.bayer_fio = bayer_fio
