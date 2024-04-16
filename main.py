from PyQt5 import QtWidgets
from ui.auth.auth_menu import AuthMenu
from classes.bd import dataBase


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AuthMenu(app)
