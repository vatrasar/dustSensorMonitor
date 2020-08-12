import time
from datetime import datetime, timedelta

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog

import Utils
from GUI.hoursGraphSettingsDialog import Ui_Dialog
from GUI.mainWindow import Ui_MainWindow
from MyDataBaseManager import MyDataBaseManager
import matplotlib.pyplot as plt

from TCPManager import TCPManager


class Controller:

    def __init__(self,mainWindow:Ui_MainWindow,dbManager:MyDataBaseManager,tcpManager:TCPManager) -> None:
        super().__init__()
        mainWindow.btnHoursGraph.clicked.connect(self.showHoursGraph)
        mainWindow.btnDayGraph.clicked.connect(self.day_graph)
        mainWindow.progressBar.setVisible(False)
        self.dbManager=dbManager
        self.mainWindow=mainWindow
        tcpManager.lab_info_signal.connect(self.update_lab_info)
        tcpManager.update_progress_signal.connect(self.update_progress)
        tcpManager.ip_search_end_signal.connect(self.hide_progress)
        self.number_of_days=1

    def day_graph(self):
        window = QDialog()
        ui_settings = Ui_Dialog()
        ui_settings.setupUi(window)
        if (window.exec_()):
            self.number_of_days = ui_settings.spinNumberOfDays.value()

        now = datetime.now()
        today = datetime(now.year, now.month, now.day, 0, 0, 0, 0)
        daysList = []

        for day_index in range(0, self.number_of_days):

            nextDay = today + timedelta(days=1)
            records = self.dbManager.get_dust_for_range(int(round(today.timestamp() * 1000)),
                                                            int(round(nextDay.timestamp() * 1000)))

            averageForDay = Utils.averageFromList(records)
            daysList.append(averageForDay)
            today = today - timedelta(days=1)


        plt.close()

        #creating labels
        days_labels=[]
        for day_index,_ in enumerate(daysList):
            days_labels.append(str(-day_index))





        plt.bar(days_labels, daysList, color='maroon',
                width=0.4)

        plt.tight_layout()

        plt.savefig('result.svg')

        self.mainWindow.graphView.setPixmap(QPixmap("result.svg"))

    def hide_progress(self):
        self.mainWindow.progressBar.setVisible(False)

    def update_progress(self,progress:float):
        if not(self.mainWindow.progressBar.isVisible()):
            self.mainWindow.progressBar.setVisible(True)
        self.mainWindow.progressBar.setValue(int(progress))

    def update_lab_info(self,new_info:str):
        self.mainWindow.labInfo.setText(new_info)

    def showHoursGraph(self):

        window = QDialog()
        ui_settings = Ui_Dialog()
        ui_settings.setupUi(window)
        if (window.exec_()):
            self.number_of_days=ui_settings.spinNumberOfDays.value()

        now=datetime.now()
        today=datetime(now.year,now.month,now.day,0,0,0,0)
        daysList=[]

        for day_index in range(0,self.number_of_days):
            hoursList = []
            for i in range(0,24):
                nextHour=today+timedelta(hours=1)
                records = self.dbManager.get_dust_for_range(int(round(today.timestamp() * 1000)),int(round(nextHour.timestamp() * 1000)))
                hoursList.append(records)
                today=nextHour




            averageForHoursList=list(map(lambda x:Utils.averageFromList(x),hoursList))
            daysList.append(averageForHoursList)
            today = today - timedelta(days=2)

        legendList=[]
        plt.close()
        for index,day in enumerate(daysList):
            plt.plot(day)
            legendList.append("dzisiaj - "+str(index))
        plt.legend(legendList,loc='upper right',bbox_to_anchor=(1.3, 1.0))
        plt.tight_layout()

        plt.savefig('result.svg')

        self.mainWindow.graphView.setPixmap(QPixmap("result.svg"))
