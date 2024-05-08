import requests
from pprint import pprint

"""https://open.spotify.com/intl-fr"""


def requestLink(url, payload):
    r = requests.get(f'https://{url}/get')
    p = requests.post(f'https://{url}/post', payload)
    pprint(p)
    print("==" * 120)
    print("print usage")
    print(r.headers, r.text)


data = {"username": "Jordan", "Password": "98202400"}
link = input("Enter the URL: ")
requestLink(link, data)
