import socket
import time
from threading import Thread

from MyDataBaseManager import MyDataBaseManager


class TCPManager(Thread):


    def run(self) -> None:
        super().run()
        self.start_colecting_data()

    def __init__(self,sensor_ip_adress,databaseManager:MyDataBaseManager) -> None:
        super().__init__()
        self.sensor_ip_adress=sensor_ip_adress
        self.databaseManager=databaseManager


    def start_colecting_data(self):
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


            server_address = (self.sensor_ip_adress, 23)
            # print('connecting to {} port {}'.format(*server_address))
            s.connect(server_address)

            data = s.recv(16)

            dust_value=float(data.decode("utf-8"))
            self.databaseManager.add_record(dust_value,int(round(time.time() * 1000)))
            time.sleep(30)

# Look for the response




