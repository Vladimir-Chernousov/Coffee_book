import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5 import uic


class Program(QWidget):
    def __init__(self):
        super(Program, self).__init__()
        uic.loadUi('main.ui', self)
        self.view_table()

    def view_table(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        cur.execute("SELECT ID,[Название сорта],[Степень обжарки],[Молотый/в зёрнах],"
                    "[Описание вкуса],Цена,[Объём упаковки] FROM coffee")
        value = cur.fetchall()
        self.table.setRowCount(len(value))
        self.table.setColumnCount(len(value[0]))
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem('ID'))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem('Название сорта'))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem('Степень обжарки'))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem('Молотый/в зёрнах'))
        self.table.setHorizontalHeaderItem(4, QTableWidgetItem('Описание вкуса'))
        self.table.setHorizontalHeaderItem(5, QTableWidgetItem('Цена'))
        self.table.setHorizontalHeaderItem(6, QTableWidgetItem('Объём упаковки'))
        for i, elem in enumerate(value):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app2 = QApplication(sys.argv)
    ex2 = Program()
    ex2.show()
    app2.exec_()
