import abc
import urllib.request


class DataConnectUrl(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def connection(self):
        pass


class DataFetchUrl(DataConnectUrl):
    def __init__(self, urladd):
        self.url = urladd

    def connection(self):
        weburl = urllib.request.urlopen(self.url)
        result = weburl.read()
        return result


data = DataFetchUrl("http://python.org/")
urlData = data.connection()
print(urlData)