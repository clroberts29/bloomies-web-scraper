import os
import requests
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import time




header = {'user-agent': 'Mozilla/5.0'}

x=3388848

while x < 3388850:

 
    x = str(x)


    website = 'https://www.bloomingdales.com/shop/product/burberry-icon-stripe-gauze-scarf?ID=' + x + '&CategoryID=1005369#fn=ppp%3Dundefined%26sp%3DNULL%26rId%3DNULL%26spc%3D366%26spp%3D2%26pn%3D1%7C4%7C2%7C366%26rsid%3Dundefined%26smp%3DmatchNone'




    raw_html = requests.get(website, headers=header)

    html = raw_html.content


    soup = BeautifulSoup(html, 'html.parser')


    pricing = soup.find("div",{'class':'final-price'})

    price_only = pricing.text
    print(price_only)

    title = soup.find("div",{'class':'product-title'})

    brand = (title.a.text).strip()

    product_name = (title.h1.text).strip()


    print(brand)
    print(product_name)



    prod_attr = soup.find_all("div",{"class":"accordion-body"})

    attributes = []
    for p in prod_attr:
            attribute = p.ul.text
            attributes.append(attribute)


    coo = ""


    for p in attributes:
            if p.find("Made in") > 0:
                    coo = p

    coo = coo.partition("\n")
    coo = coo[2].split("\n")

    for p in coo:
            if "Made in" in p:
                    coo = p

    print(coo)

    x = int(x)

    x = x+1

breakpoint()








