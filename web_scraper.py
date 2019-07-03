import os
import requests
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import time
import csv
import OpenSSL


header = {'user-agent': 'Mozilla/5.0'}

cat_id = input("Enter the Bloomingdale's category id number:")

cat_id = str(cat_id)

page = '1'

website = "https://www.bloomingdales.com/shop/?id=" + cat_id


raw_html_list = requests.get(website, headers=header)

html_list = raw_html_list.content

soup_list = BeautifulSoup(html_list, 'html.parser')

prodlist = []
for idnums in soup_list.find_all('div'):
    try:
        idnumber = int(idnums.get('id'))
        prodlist.append(idnumber)
    
    except:
        pass





csv_headers = ["item_number", "brand", "product_name", "price", "coo", "prod_dim", "content", "website", "category"]
csv_file_path = "data\data.csv"

with open(csv_file_path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        for x in prodlist:
            try:

                x = str(x)


                website = 'https://www.bloomingdales.com/shop/product/?ID=' + x




                raw_html = requests.get(website, headers=header)

                html = raw_html.content


                soup = BeautifulSoup(html, 'html.parser')

                pricing = soup.find("div",{'class':'final-price'})

                price_only = pricing.text

                price_only = price_only.strip()

                #print("item " + x + " price: " + price_only)

                title = soup.find("div",{'class':'product-title'})

                brand = (title.a.text).strip()

                product_name = (title.h1.text).strip()


                #print("item " + x + " brand: " + brand)
                #print("item " + x + " product name: " + product_name)



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

                #print("item " + x + " coo: " + coo)

                prod_dim = ''

                for g in attributes:
                    if g.find("W x ") > 0:
                        prod_dim = g

                prod_dim = prod_dim.partition("\n")
                prod_dim = prod_dim[2].split("\n")
                prod_dim = prod_dim[0]


                #print(prod_dim)

                content =  ''

                for k in attributes:
                        if k.find("silk") > 0 or k.find("cotton") > 0 or k.find("wool") > 0 or k.find("poly") > 0 or k.find("modal") > 0 or k.find("viscose") > 0 or k.find("rayon") > 0:
                                content = k



                content = content.partition("\n")
                content = content[2].split("\n")
                content = content[0].strip()



                #print("item " + x + " content: " + content)



                category_all = soup.find_all("div",{'class':'product-details-feature'})

                category = []

                for h in category_all:
                        category_text = h.a.text
                        category.append(category_text)

                category_string = category[0]

                category_string = category_string.split("\n")

                category_string = category_string[1]






                #       csv_row = [x, brand, product_name, price_only, coo, prod_dim]

                csv_row = ["323456", "Burberry", "test style", "349.99", "Made In China", "27 x 27"]


            


                writer.writerow({
                        "item_number": x,
                        "brand": brand,
                        "product_name": product_name,
                        "price": price_only,
                        "coo": coo,
                        "prod_dim": prod_dim,
                        "content": content,
                        "website": website,
                        "category": category_string  
                })     



                #x = int(x)

                #x = x+1

    





            except AttributeError:
                  #x = int(x)

                  #x = x + 1
                pass

        #csv_file_path = "C:\\Users\\croberts\\Documents\\GitHub\\bloomies-web-scraper\\data\data.csv"
        #
        #
        #breakpoint()


