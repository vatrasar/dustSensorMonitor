import socket
import time

from MyDataBaseManager import MyDataBaseManager


class TCPManager():

    def __init__(self,sensor_ip_adress,databaseManager:MyDataBaseManager) -> None:
        super().__init__()
        self.sensor_ip_adress=sensor_ip_adress
        self.databaseManager=databaseManager


    def start_colecting_data(self):
        #make connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        amount_received = 0
        amount_expected = len("test")
        server_address = (self.sensor_ip_adress, 23)
        print('connecting to {} port {}'.format(*server_address))
        s.connect(server_address)
        while True:
            data = s.recv(16)
            amount_received += len(data)
            print(data.decode("utf-8"))
            # time.sleep(2)

# Look for the response




