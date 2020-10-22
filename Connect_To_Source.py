from abc import ABC, abstractmethod
import requests
import urllib.request
import mysql.connector


class ConnectToSource(ABC):
    @abstractmethod
    def __init__(self, conn):
        pass

    @abstractmethod
    def connect(self):
        pass


class ConnectToRemoteURL(ConnectToSource):
    def __init__(self, conn):
        super().__init__(conn)
        self.conn_string = conn

    def connect(self):
        try:
            web_url = urllib.request.urlopen(self.conn_string)
            conn_object = web_url.read()
            return conn_object
        except IOError:
            print("Error")


class ConnectToAPI(ConnectToSource):
    def __init__(self, conn):
        super().__init__(conn)
        self.conn_string = conn

    def connect(self):
        try:
            conn_object = requests.request("GET", self.conn_string)
            return conn_object
        except IOError:
            print("Error")


class ConnectToDatabase(ConnectToSource):
    def __init__(self, conn):
        super().__init__(conn)
        self.conn_string = conn

    def connect(self):
        try:
            conn_object = mysql.connector.connect(user=self.conn_string["user"],
                                                  password=self.conn_string["password"],
                                                  host=self.conn_string["hostname"],
                                                  database=self.conn_string["database"],
                                                  port=self.conn_string["port"])
            return conn_object
        except IOError:
            print("error")