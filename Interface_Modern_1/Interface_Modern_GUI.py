import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Interface_Modern.ui", self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())