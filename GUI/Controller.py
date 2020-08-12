import time
from datetime import datetime, timedelta

from PyQt5.QtGui import QPixmap

import Utils
from GUI.mainWindow import Ui_MainWindow
from MyDataBaseManager import MyDataBaseManager
import matplotlib.pyplot as plt

from TCPManager import TCPManager


class Controller:

    def __init__(self,mainWindow:Ui_MainWindow,dbManager:MyDataBaseManager,tcpManager:TCPManager) -> None:
        super().__init__()
        mainWindow.btnHoursGraph.clicked.connect(self.showHoursGraph)
        mainWindow.progressBar.setVisible(False)
        self.dbManager=dbManager
        self.mainWindow=mainWindow
        tcpManager.lab_info_signal.connect(self.update_lab_info)
        tcpManager.update_progress_signal.connect(self.update_progress)
        tcpManager.ip_search_end_signal.connect(self.hide_progress)

    def hide_progress(self):
        self.mainWindow.progressBar.setVisible(False)

    def update_progress(self,progress:float):
        if not(self.mainWindow.progressBar.isVisible()):
            self.mainWindow.progressBar.setVisible(True)
        self.mainWindow.progressBar.setValue(int(progress))

    def update_lab_info(self,new_info:str):
        self.mainWindow.labInfo.setText(new_info)

    def showHoursGraph(self):
        now=datetime.now()
        today=datetime(now.year,now.month,now.day,0,0,0,0)
        hoursList=[]

        for i in range(0,24):
            nextHour=today+timedelta(hours=1)
            records = self.dbManager.get_dust_for_range(int(round(today.timestamp() * 1000)),int(round(nextHour.timestamp() * 1000)))
            hoursList.append(records)
            today=nextHour




        averageForHoursList=list(map(lambda x:Utils.averageFromList(x),hoursList))

        plt.plot(averageForHoursList)

        plt.savefig('result.svg')

        self.mainWindow.graphView.setPixmap(QPixmap("result.svg"))
