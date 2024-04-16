import sqlite3
tablesToCreate = {
    'employees': 'passport INTEGER PRIMARY KEY, full_name TEXT, role TEXT',
    '': [],
}
tables = {
    'employees': 'passport, full_name , role'
}
class dataBase():
    def __init__(self):
        self.connect = sqlite3.connect('database/database.db')
        self.cursor = self.connect.cursor()
        self.check_bd()


    def check_bd(self): # проверку таблиц можно сделать циклом, используя список, находящийся в верхней части кода
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS employees ({tablesToCreate['employees']})''')

    def insertInfo(self, table, data):
        if (data[0] == '') or (data[1] == ''):
            return "Одно из полей не заполнено"
        self.cursor.execute(f'''select * from {table} where {tables[table].split(',')[0].strip()} = {data[0]}''')
        if self.cursor.fetchone() is None:
            self.cursor.execute(f'''INSERT INTO {table} ({tables[table]}) VALUES (?, ?, ?)''', data)
            self.connect.commit()
            return "Успешное добавление"
        else:
            return "Операция не совершена.Работник с таким паспортом уже зарегистрирован"

    def assignEmplDuty(self, data):
        self.cursor.execute('''insert into duty_employee (employee_id, date) VALUES (?, ?)''', data)
        self.connect.commit()

    def newOrder(self, data):
        self.cursor.execute('''insert into orders (namefood, status) VALUES (?, ?)''', data)
        self.connect.commit()
        print('bd: order commited')

    def updateOrder(self, data, status):
        print(data)
        self.cursor.execute(f'''Update orders set status = "{status}" where idorder = {data[0]}''')
        self.connect.commit()
        print("bd: order payed")

    def deleteRow(self, table, nameRow, equal):
        self.cursor.execute(f'''DELETE FROM {table} where {nameRow} = {equal}''')
        # if self.cursor.fetchone() is None:
        #     raise "bd: no one row"
        self.connect.commit()
        print(f"bd: deleted {nameRow} = {equal} from {table}")

    def get_table(self, table):
        self.cursor.execute(f'''select * from {table}''')
        rows = self.cursor.fetchall()
        return rows

    def getRole(self, data):
        self.cursor.execute(f'''select role, passport from employees where passport = {data}''')
        role = self.cursor.fetchone()
        return role

    def disconnect(self):
        self.cursor.close()
        self.connect.close()