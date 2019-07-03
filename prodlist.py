import os
import requests
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import time
import csv

header = {'user-agent': 'Mozilla/5.0'}

website = input("Enter your web address:")

#website = "https://www.bloomingdales.com/shop/jewelry-accessories/womens-scarves-wraps?id=1005369&cm_sp=NAVIGATION-_-TOP_NAV-_-1005369-Accessories-Scarves-%26-Wraps"


raw_html = requests.get(website, headers=header)

html = raw_html.content

soup = BeautifulSoup(html, 'html.parser')

prodlist = []
for idnums in soup.find_all('div'):
    try:
        idnumber = int(idnums.get('id'))
        prodlist.append(idnumber)
    
    except:
        pass




breakpoint()
