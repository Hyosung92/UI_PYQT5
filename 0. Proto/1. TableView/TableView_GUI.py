import sys

#####################################
# Only for GUI development
from PyQt5 import uic
#####################################

#####################################
# Use .ui file to convert .py file for distribution GUI using code below
# from Side_Bar import Ui_MainWindow
#####################################

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTableView
from PyQt5.QtCore import Qt

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self.setHorizontalHeaderLabels(["Name", "Image", "Color"])
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("TableView.ui", self)

        self.init_func()

    def init_func(self):
        '''
        1. Tableview에 Plot될 데이터를 json 파일로 저장
        2. GUI가 시작되면 json 파일을 read해서 model에 저장
        3. Model에 저장된 data를 plot
        '''
        self.table = QTableView()

        # 아래의 data 부분을 외부에서 read
        data = [
          [4, 9, 2],
          [1, 0, 0],
          [3, 5, 0],
          [3, 3, 2],
          [7, 8, 9],
        ]

        self.model = TableModel(data)
        
        self.table.setModel(self.model)

        # self.setCentralWidget(self.table)
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())