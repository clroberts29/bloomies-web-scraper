import requests
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

header = {'user-agent': 'Mozilla/5.0'}

website = 'https://www.bloomingdales.com/shop/product/burberry-icon-stripe-gauze-scarf?ID=3388848&CategoryID=1005369#fn=ppp%3Dundefined%26sp%3DNULL%26rId%3DNULL%26spc%3D366%26spp%3D2%26pn%3D1%7C4%7C2%7C366%26rsid%3Dundefined%26smp%3DmatchNone'

#website = "https://www.google.com"



raw_html = requests.get(website, headers=header)

html = raw_html.content

print(html)

