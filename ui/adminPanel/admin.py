import sys
from classes.bd import dataBase
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel


class AdminPanel(object):
    def __init__(self):
        self.ui = uic.loadUi('ui/adminPanel/admin.ui')
        # self.app = app
        self.bd = dataBase()
        self.ui.show()
        self.ui.ExitBtn.clicked.connect(self.exit)
        self.ui.addNewEmplBtn.clicked.connect(self.addInfoToDb)
        self.ui.fireEmplBtn.clicked.connect(self.fireEmployee)
        self.ui.showEmplBtn.clicked.connect(self.getAllEmployees)
        self.ui.checkOrderBtn.clicked.connect(self.getAllOrders)
        self.ui.commitBtn.clicked.connect(self.assignEmplToDuty)
        self.ui.getDutyBtn.clicked.connect(self.getAllDuty)
        self.viewDb = QSqlDatabase.addDatabase("QSQLITE")
        self.viewDb.setDatabaseName("database/database.db")
        self.viewDb.open()
        # self.run()

    # def run(self):
    #     self.app.exec_()

    def exit(self):
        self.bd.disconnect()
        sys.exit()

    def addInfoToDb(self):
        data = []
        data.append(self.ui.primaryData.text())
        data.append(self.ui.nameNewEmpl.text())
        data.append(self.ui.chooseRole.currentText())
        print(self.bd.insertInfo('employees', data))

    def getAllEmployees(self):
        model = QSqlTableModel()
        model.setTable("employees")
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        model.select()

        self.ui.tableView.setModel(model)

    def getAllOrders(self):
        model = QSqlTableModel()
        model.setTable("orders")
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        model.select()

        self.ui.tableView.setModel(model)

    def getAllDuty(self):
        model = QSqlTableModel()
        model.setTable("duty_employee")
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        model.select()

        self.ui.tableView.setModel(model)

    def assignEmplToDuty(self):
        data = [self.ui.idToDuty.text(), self.ui.date.text()]
        self.bd.assignEmplDuty(data)
        print('assigned')


    def fireEmployee(self):
        data = self.ui.idToDelete.text()
        if data == '':
            print("Пустое поле")
            # return "Пустое поле"
            return 0
        try:
            self.bd.deleteRow("employees", "passport", data)
        except:
            # print("Такого работника нет в базе данных")
            print("Неправильное заполнения поля. Допускается только серия и номер паспорта")
        else:
            print("admPanel: Успешное увольнение")