import requests

from bs4 import BeautifulSoup
from requests import Response


def getRequest(URL):
    r1: Response = requests.get(URL)
    bs = BeautifulSoup(r1.text, "html.parser")
    print(r1.text)
    print(bs)
    return bs


link1 = input('Enter first link: ')
getRequest(link1)
