from MyDataBaseManager import MyDataBaseManager
from TCPManager import TCPManager

if __name__ == '__main__':
    dbManager=MyDataBaseManager("./dust.db")
    tcpManager=TCPManager('192.168.0.102',dbManager)
    tcpManager.start_colecting_data()