from pprint import pprint

import requests


class NBU():
    URL : str
    DATA : list
python  
    def __init__(self,url):
        self.URL = url


    def connect(self):
        try:
            req = requests.get(self.URL)
        except  Exception as ex:
            print(ex)

        try:
            info = req.json()
        except Exception as exe:
            print(exe)
        self.DATA = info
    def get_data(self):
        pprint(self.DATA)



