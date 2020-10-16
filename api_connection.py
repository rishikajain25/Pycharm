import requests

class ConnectApi:
    def __init__(self,urladd):
        self.url = urladd

    def connection(self):
        response = requests.request("GET",self.url)
        return response
api= ConnectApi("http://api.open-notify.org/astros.json")
apiData=api.connection()
print(apiData.json())

