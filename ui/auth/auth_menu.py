from PyQt5 import QtCore, QtGui, QtWidgets, uic
from ui.adminPanel.admin import AdminPanel
from ui.cookPanel.cookPanel import cookPanel
from ui.officPanel.officPanel import officPanel
from classes.bd import dataBase
import sys

class AuthMenu(object):
    def __init__(self, app):
        self.ui = uic.loadUi('ui/auth/auth_menu.ui')
        self.app = app
        self.ui.show()
        self.bd = dataBase()
        self.ui.auth_button.clicked.connect(self.login)
        self.run()

    def run(self):
        self.app.exec_()

    def login(self):
        login = self.ui.log_ent.text()
        # self.bd.getRole("111111111")[0]
        if login == "admin":
            self.ui.hide()
            self.newWindow = AdminPanel()
            return 0
        role = self.bd.getRole(login)[0]
        id = self.bd.getRole(login)[1]
        print(role, id)
        if role == "Повар":
            self.ui.hide()
            self.newWindow = cookPanel(id)
        elif role == "Официант":
            self.ui.hide()
            self.newWindow = officPanel()

