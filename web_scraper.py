import os
import requests
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import time
import csv
import OpenSSL

# re-establish header
header = {'user-agent': 'Mozilla/5.0'}

# define function
def clean_up(product_data):
    product_data = product_data.partition("\n")
    product_data = product_data[2].split("\n")
    product_data = product_data[0]
    return product_data

# call and define target category page
cat_id = input("Enter the Bloomingdale's category id number:")

cat_id = str(cat_id)

website = "https://www.bloomingdales.com/shop/?id=" + cat_id

# convert website into souped HTML
raw_html_list = requests.get(website, headers=header)

html_list = raw_html_list.content

soup_list = BeautifulSoup(html_list, 'html.parser')

# convert soup into list of target products
prodlist = []
for idnums in soup_list.find_all('div'):
    try:
        idnumber = int(idnums.get('id'))
        prodlist.append(idnumber)
    
    except:
        pass


# define csv headers, file path and open file
csv_headers = ["item_number", "brand", "product_name", "price", "coo", "prod_dim", "content", "website", "category"]
csv_file_path = "data\data.csv"

with open(csv_file_path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)

# loop through list
        for x in prodlist:

# error handling            
            try:

                x = str(x)

# select the product page and return the 'souped' html
                website = 'https://www.bloomingdales.com/shop/product/?ID=' + x

                raw_html = requests.get(website, headers=header)

                html = raw_html.content

                soup = BeautifulSoup(html, 'html.parser')

# return the pricing variable
                pricing = soup.find("div",{'class':'final-price'})

                price_only = pricing.text

                price_only = price_only.strip()

# return the brand variable
                title = soup.find("div",{'class':'product-title'})

                brand = (title.a.text).strip()

# return the product name variable
                product_name = (title.h1.text).strip()

                prod_attr = soup.find_all("div",{"class":"accordion-body"})

# return the country of origin variable
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
                    if ("Made in" in p or "imported" in p):
                        coo = p

# return the product dimensions
                prod_dim = ''

                for g in attributes:
                    if g.find("W x ") > 0:
                        prod_dim = g

                prod_dim = clean_up(prod_dim)

# return the content
                content =  ''

                for k in attributes:
                        if k.find("silk") > 0 or k.find("cotton") > 0 or k.find("wool") > 0 or k.find("poly") > 0 or k.find("modal") > 0 or k.find("viscose") > 0 or k.find("rayon") > 0:
                                content = k

                content = clean_up(content)

# return the category
                category_all = soup.find_all("div",{'class':'product-details-feature'})

                category = []

                for h in category_all:
                        category_text = h.a.text
                        category.append(category_text)

                category_string = category[0]

                category_string = category_string.split("\n")

                category_string = category_string[1]

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

            except AttributeError:

                pass



