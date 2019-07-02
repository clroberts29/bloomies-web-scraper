import os
import requests
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import time
import csv
import OpenSSL





header = {'user-agent': 'Mozilla/5.0'}

x=3388848

while x < 3388860:
    try:

        
        x = str(x)


        website = 'https://www.bloomingdales.com/shop/product/?ID=' + x




        raw_html = requests.get(website, headers=header)

        html = raw_html.content


        soup = BeautifulSoup(html, 'html.parser')


        pricing = soup.find("div",{'class':'final-price'})

        price_only = pricing.text

        price_only = price_only.strip()

        print("item " + x + " price: " + price_only)

        title = soup.find("div",{'class':'product-title'})

        brand = (title.a.text).strip()

        product_name = (title.h1.text).strip()


        print("item " + x + " brand: " + brand)
        print("item " + x + " product name: " + product_name)



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

        #for p in coo:
        #    if "Made in" in p:
        #        coo = p


        for p in coo:
            if ("Made in" in p or "imported" in p):
                coo = p

        print("item " + x + " coo: " + coo)
        
        prod_dim = ''

        for g in attributes:
            if g.find("W x ") > 0:
                prod_dim = g

        prod_dim = prod_dim.partition("\n")
        prod_dim = prod_dim[2].split("\n")
        prod_dim = prod_dim[0]


        print(prod_dim)

        content =  ''

        for k in attributes:
                if ("silk" in k or "cotton" in k or "wool" in k or "poly" in k or "modal" in k or "viscose" in k or "rayon" in k):
                        content = k
        
        content = content.text

        print("item " + x + " content: " + content)
        
        
        csv_file_path = "C:\\Users\\croberts\\Documents\\GitHub\\bloomies-web-scraper\\data\data.csv"
        

        csv_headers = ["item_number", "brand", "product_name", "price", "coo", "prod_dim"]
        #       csv_row = [x, brand, product_name, price_only, coo, prod_dim]

        csv_row = ["323456", "Burberry", "test style", "349.99", "Made In China", "27 x 27"]


        #with open(csv_file_path, 'w') as csv_file:     
        #    writer = csv.writer(csv_file, fieldnames=csv_headers)
        #    writer.writerow(csv_row)
        #csv_file.close()

        with open(csv_file_path, "w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
            writer.writerow({
                "item_number": x,
                "brand": brand,
                "product_name": product_name,
                "price": price_only,
                "coo": coo,
                "prod_dim": prod_dim     
        })     



        x = int(x)

        x = x+1




    except AttributeError:
          x = int(x)

          x = x + 1

#csv_file_path = "C:\\Users\\croberts\\Documents\\GitHub\\bloomies-web-scraper\\data\data.csv"
#
#
#breakpoint()


