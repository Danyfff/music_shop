import sys
from PyQt6 import QtWidgets
from client.ui import main_form_ui


class LogginForm(QtWidgets.QMainWindow, main_form_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LogginForm()
    window.show()
    app.exec()
