# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

conn_string='mongodb+srv://mongo:1234@cluster0.9xrn6.mongodb.net/test'
client=pymongo.MongoClient(conn_string)

mydb=client['Products']
db=mydb.products

def getLastPage():
    r = requests.get("https://www.douglas.sk/c/licenie-4003/")
    soup = BeautifulSoup(r.content, 'html.parser')

    page = soup.find('div', {'class': 'paging--container'}).find_all('span', {'class': 'paging--display'})
    lastPage = page[1].text
    lp = re.findall('[0-9]+', lastPage.strip())
    lp = int(lp[0])
    return lp

productsList=[]
brandsList=[]

price_pattern = re.compile('[0-9]+,[0-9]+')

lp=getLastPage()

for page in range(1, lp+1):
# for page in range(1, 5):    
    url=f'https://www.douglas.sk/widgets/listing/listingCount/sCategory/4003?p={page}&ffFollowSearch=9980&o=&n=48&min=1.1&max=237&loadProducts=1&loadFacets=1&dgBasePath=https%3A%2F%2Fwww.douglas.sk%2Fc%2Flicenie-4003%2F%3Fp%3D{page}%26ffFollowSearch%3D9980%26o%3D%26n%3D48%26min%3D1.1%26max%3D237'
    r = requests.get(url)
    response = r.json()
    soup = BeautifulSoup(response['listing'], 'html.parser')
    products = soup.find_all('div', class_= 'box--content')
    for p in products:
        try:
            brand =p.find('span',attrs={'class':'product--manufacturer'}).text
            name = p.find('span', attrs={'class':'product--title'}).text
            pricetmp = p.find('span', attrs={'class':'price--default'}).text
            pricetmp = price_pattern.findall(pricetmp)
            price=pricetmp[0]
            price =  float(str(price).replace(',', '.'))
            categorytmp = p.find('span', attrs={'class':'product--dg-classification'}).text
            
            if categorytmp!="":
                category=categorytmp
            else:
                category="nešpecifikovaná"
                
                
            url = p.find('a')['href']
            imageUrl = p.find('img').attrs['src']
            obj={
                'Brand': brand.strip().capitalize(),
                'Name':name.strip().encode('ascii', 'ignore').decode('utf-8'),
                'Price':price,
                'Category':category.strip().capitalize(),
                'Url':url,
                'Image': imageUrl,
                'Eshop': "douglas"
            }
            productsList.append(obj)
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
                  "Eshop": "douglas"}},
                  upsert=True) 