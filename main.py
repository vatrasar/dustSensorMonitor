import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from GUI.Controller import Controller
from GUI.mainWindow import Ui_MainWindow
from MyDataBaseManager import MyDataBaseManager
from TCPManager import TCPManager

if __name__ == '__main__':
    dbManager=MyDataBaseManager("./dust.db")
    tcpManager=TCPManager('192.168.0.102',dbManager)
    tcpManager.start()

    app = QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    controller= Controller(ui,dbManager)
    window.show()
    sys.exit(app.exec_())