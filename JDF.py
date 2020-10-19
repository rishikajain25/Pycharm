import abc
import requests


class DataConnect(metaclass=abc.ABCMeta):

    def __init__(self, url):
        super().__init__(url)
        self.urladd = url

    @abc.abstractmethod
    def connect(self):
        pass


class DataApi(DataConnect):

    def connect(self):
        response = requests.request("GET", self.urladd)
        return response