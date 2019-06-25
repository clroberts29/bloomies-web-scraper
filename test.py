from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

header = {'user-agent': 'Mozilla/5.0'}


raw_html = get("http://www.bloomingdales.com", headers=header)

html = BeautifulSoup(raw_html, 'html.parser')


print(raw_html.status_code)

print(html.content)

