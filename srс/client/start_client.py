import sys
from PyQt6 import QtWidgets
from src.login_form import LogginForm
from src.main_form import MainForm

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LogginForm()
    main_form = MainForm()
    window.login_corent.connect(main_form.set_user_data)
    window.login_corent.connect(main_form.show)
    window.show()
    app.exec()
