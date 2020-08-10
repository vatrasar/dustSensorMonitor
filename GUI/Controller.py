import time
from datetime import datetime, timedelta

from PyQt5.QtGui import QPixmap

import Utils
from GUI.mainWindow import Ui_MainWindow
from MyDataBaseManager import MyDataBaseManager
import matplotlib.pyplot as plt

class Controller:

    def __init__(self,mainWindow:Ui_MainWindow,dbManager:MyDataBaseManager) -> None:
        super().__init__()
        mainWindow.btnHoursGraph.clicked.connect(self.showHoursGraph)
        self.dbManager=dbManager
        self.mainWindow=mainWindow

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
