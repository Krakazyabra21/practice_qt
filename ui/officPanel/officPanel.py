import sys
from classes.bd import dataBase
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel


class officPanel(object):
    def __init__(self):
        self.ui = uic.loadUi('ui/officPanel/officPanel.ui')
        # self.app = app
        self.ui.show()
        self.bd = dataBase()
        self.viewDb = QSqlDatabase.addDatabase("QSQLITE")
        self.viewDb.setDatabaseName("database/database.db")
        self.viewDb.open()
        self.ui.showOrdersBtn.clicked.connect(self.getAllOrders)
        self.ui.newOrderBtn.clicked.connect(self.newOrder)
        self.ui.orderPayedBtn.clicked.connect(self.changeOrderStatus)
        # self.run()

    # def run(self):
    #     self.app.exec_()

    def exit(self):
        self.bd.disconnect()
        sys.exit()

    def getAllOrders(self):
        model = QSqlTableModel()
        model.setTable("orders")
        model.setFilter('not status = "Готовится"')
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        model.select()

        self.ui.tableView.setModel(model)

    def newOrder(self):
        data = [self.ui.nameFood.text(), 'Принят']
        self.bd.newOrder(data)

    def changeOrderStatus(self):
        self.bd.updateOrder(self.ui.orderPayed.text(), "Оплачено")