import socket
import subprocess
import time
from threading import Thread

from PyQt5.QtCore import QThread, pyqtSignal

from MyDataBaseManager import MyDataBaseManager


class TCPManager(QThread):
    lab_info_signal = pyqtSignal(str)
    update_progress_signal=pyqtSignal(float)
    ip_search_end_signal=pyqtSignal()
    def run(self) -> None:
        self.start_colecting_data()

    def __init__(self,sensor_network_adress,databaseManager:MyDataBaseManager) -> None:
        super().__init__()
        self.sensor_network_adress=sensor_network_adress
        self.sensor_ip_adress=self.get_last_sensor_ip()
        self.databaseManager=databaseManager


    def start_colecting_data(self):
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


                server_address = (self.sensor_ip_adress, 23)
                # print('connecting to {} port {}'.format(*server_address))
                s.connect(server_address)

                data = s.recv(16)

                dust_value=float(data.decode("utf-8"))
                print(dust_value)
                self.databaseManager.add_record(dust_value,int(round(time.time() * 1000)))
                self.lab_info_signal.emit("Ostatnia odczytana wartość: "+str(dust_value))
                time.sleep(30)
            except Exception:
                try:
                    self.lab_info_signal.emit("Wyszukiwanie czujnika w sieci...")
                    self.sensor_ip_adress=self.get_sensor_ip_addres()
                    self.lab_info_signal.emit("Znaleziono czujnik w sieci!")
                    self.ip_search_end_signal.emit()
                    time.sleep(2)
                except Exception:
                    self.lab_info_signal.emit("Nie wykryto czujnika w sieci")


    def get_sensor_ip_addres(self):
        result_adress=self.sensor_network_adress+str(0)

        print("start to search ip adress of dust sensor")

        for i in range(0,256):
            try:

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                server_address = (self.sensor_network_adress+str(i), 23)
                # print('connecting to {} port {}'.format(*server_address))
                print(str((i / 256.0) * 100) + "%")
                self.update_progress_signal.emit((i / 256.0) * 100)
                s.connect(server_address)
                result_adress=self.sensor_network_adress+str(i)
                # save new addr
                file = open("lastIp.txt", "w")
                file.write(result_adress)
                file.close()

                return result_adress
            except Exception:
                pass

        raise Exception("no dust sensor detected in network")

    def get_last_sensor_ip(self):
        file=open("lastIp.txt","r")
        ip=file.readline()
        file.close()
        return ip

# Look for the response




