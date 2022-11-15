# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from bson.objectid import ObjectId
import requests
import re
import pymongo


conn_string='mongodb+srv://mongo:1234@cluster0.9xrn6.mongodb.net/test'
client=pymongo.MongoClient(conn_string)

mydb=client['Products']
db=mydb.products


productsList=[]

for offset in range(0, 350*36, 36):
    url = f"https://makeup.sk/ajax/filter/?offset={offset}"
    r = requests.post(url=url, data={'categoryID': 2419})
    response = r.json()
    soup = BeautifulSoup(response['products'], 'html.parser')
    products = soup.find_all('li', class_= 'simple-slider-list__item')
    for p in products:
        try:
            if not soup.find('li', class_= 'out-of-stock'):
                brand = p.get("data-brand")
                
                name = p.find('a', attrs={'class':'simple-slider-list__name'}).text
                
                price = p.get("data-price")
                price = float(price)
                
                categorytmp = p.get('data-parent-category')
                categorytmp = re.sub('Make-up/', '', categorytmp)
                if not categorytmp is None or categorytmp!="":
                    category=categorytmp
                else:
                    category="nešpecifikovaná"
                
                url = f"https://makeup.sk/{p.find('a')['href']}"
                
                imageUrl = p.find('img').attrs['data-src-x2']
                
                obj={
                    'Brand': brand.capitalize(),
                    'Name':name.encode('ascii', 'ignore').decode('utf-8'),
                    'Price':price,
                    'Category':category.capitalize(),
                    'Url':url,
                    'Image':imageUrl,
                    "Eshop": "makeup"
                }
                productsList.append(obj)
            else:
                break
        except Exception as e:
            print(e)
            continue

# prvé vloženie dát do databázy
    # db.insert_many(productsList)

# aktualizácia dát v databáze
products=db.find({})

for p in products:
    db.update_one({"_id": ObjectId(p["_id"])}, 
                  { "$set":
                  {"Name": p["Name"],
                   "Brand": p["Brand"], 
                   "Price": p["Price"], 
                   "Category": p["Category"], 
                   "Url": p["Url"], 
                   "Image": p["Image"],
                   "Eshop": "makeup"}},
                  upsert=True)

     