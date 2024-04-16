from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from classes.bd import dataBase
import sys

class cookPanel(object):
    def __init__(self, id):
        self.ui = uic.loadUi('ui/cookPanel/cookPanel.ui')
        # self.app = apps
        self.id = id
        self.ui.checkOrderBtn.clicked.connect(self.getAllOrders)
        self.ui.changeOrder.clicked.connect(self.changeOrder)
        self.ui.ExitBtn.clicked.connect(self.exit)
        self.bd = dataBase()
        self.viewDb = QSqlDatabase.addDatabase("QSQLITE")
        self.viewDb.setDatabaseName("database/database.db")
        self.viewDb.open()
        self.ui.show()
        # self.run()

    # def run(self):
    #     self.app.exec_()

    def exit(self):
        self.bd.disconnect()
        sys.exit()

    def getAllOrders(self):
        model = QSqlTableModel()
        model.setTable("orders")
        model.setFilter('status="Принят" or status="Готовится"')
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        model.select()

        self.ui.tableView.setModel(model)

    def changeOrder(self):
        data = self.ui.idOrder.text()
        self.bd.updateOrder(data, self.ui.comboBox.currentText())
