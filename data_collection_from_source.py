from abc import ABC, abstractmethod
import requests
import urllib.request


class SourceData(ABC):
    def __init__(self, *args):
        pass

    @abstractmethod
    def getData(self):
        pass


class UrlData(SourceData):
    def __init__(self, connect):
        super().__init__(connect)
        self.connect_string = connect

    def getData(self):
        web_url = urllib.request.urlopen(self.connect_string)
        result = web_url.read()
        return result


class ApiData(SourceData):
    def __init__(self, connect):
        super().__init__(connect)
        self.connect_string = connect

    def getData(self):
        response = requests.request("GET", self.connect_string)
        return response


class DatabaseData(SourceData):
    def __init__(self, connect, table):
        super().__init__(connect)
        self.connect_string = connect
        self.table_name = table

    def getData(self):
        query = f"""
            SELECT *
            FROM {self.table_name}
        """
        print(query)
        my_cursor = self.connect_string.cursor()
        my_cursor.execute(query)
        my_result = my_cursor.fetchall()
        for x in my_result:
            return x
