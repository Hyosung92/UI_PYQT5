import sys

#####################################
# Only for GUI development
from PyQt5 import uic
# import icons
#####################################

#####################################
# Use .ui file to convert .py file for distribution GUI using code below
# from Side_Bar import Ui_MainWindow
#####################################

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        #####################################
        # Only for GUI development
        super().__init__()
        uic.loadUi("Side_Bar.ui", self)

        self.icon_menu_widget.hide()
        self.stackedWidget.setCurrentIndex(0)
        self.btn_home_R.setChecked(True)
        #####################################
        
        #####################################
        # Use .ui file to convert .py file for distribution GUI using code below
        # super(MainWindow, self).__init__()
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)

        # self.ui.icon_menu_widget.hide()
        # self.ui.stackedWidget.setCurrentIndex(0)
        # self.ui.btn_home_R.setChecked(True)
        #####################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())