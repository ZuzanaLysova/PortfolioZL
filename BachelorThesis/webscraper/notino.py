# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import pymongo
from bson.objectid import ObjectId

conn_string='mongodb+srv://mongo:1234@cluster0.9xrn6.mongodb.net/test'
client=pymongo.MongoClient(conn_string)

mydb=client['Products']
db=mydb.products

def getLastPage():
   url="https://www.notino.sk/api/navigation/special-page/notino.sk?seourl=kozmetika/dekorativna-kozmetika&"
   r=requests.get(url, headers={'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'})
   data = r.json()
   lp = data['listing']['numberOfPages']
   return lp

def getCategory(url):
    r=requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    cat = soup.find('a', attrs={'data-order':"3"}).text
    return cat

productsList1=[]
url="https://www.notino.sk/api/navigation/special-page/notino.sk?seourl=kozmetika/dekorativna-kozmetika&"
r=requests.get(url, headers={'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'})
firstpagedata = r.json()
for p in firstpagedata['listing']['products']:
    try:
        brand = p['brandName']
        name = p['name']
        price = p['priceInformation']['price']
        url1 = p['url'] 
        url = "https://www.notino.sk" + url1
        category = getCategory(url)
        img1 = p['imageUrl']
        img = "https://cdn.notinoimg.com/detail_thumb/" + img1
        obj = {
            'Brand': brand.strip().capitalize(),
            'Name': name.encode('ascii', 'ignore').decode('utf-8'),
            'Price': price,
            'Category': category.capitalize(),
            'Url': url,
            'Image': img,
            'Eshop': "notino"
        }
        productsList1.append(obj)

    except Exception as e:
        print(e)
        continue

lp=getLastPage()
productsList2=[]

for page in range(2, lp+1): 
# for page in range(2, 5):
    url=f"https://www.notino.sk/api/navigation/special-page/notino.sk?seourl=kozmetika/dekorativna-kozmetika&f={page}-2-2-3644"
    r=requests.get(url, headers={'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'})
    data = r.json()
    for p in data['listing']['products']:
        try:
            brand = p['brandName']
            name = p['name']
            price = p['priceInformation']['price']
            url1 = p['url']
            url = "https://www.notino.sk" + url1
            category = getCategory(url)
            img1 = p['imageUrl']
            img = "https://cdn.notinoimg.com/detail_thumb/" + img1
            obj = {
                'Brand': brand.strip().capitalize(),
                'Name': name.encode('ascii', 'ignore').decode('utf-8'),
                'Price': price,
                'Category': category.capitalize(),
                'Url': url,
                'Image': img,
                'Eshop': "notino"
            }
            productsList2.append(obj)

        except Exception as e:
            print(e)
            continue

productsList=productsList1+productsList2

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
                    "Eshop": "notino"}},
                  upsert=True)