# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import pymongo
from bson.objectid import ObjectId


conn_string='mongodb+srv://mongo:1234@cluster0.9xrn6.mongodb.net/test'
client=pymongo.MongoClient(conn_string)

mydb=client['Products']
db=mydb.products

r=requests.get("https://www.pinkpanda.sk")  
soup = BeautifulSoup(r.content, 'html.parser')

# ziskam url vsetkych kategorii a potom produkty v jednotlivych kategoriach 
def getCatUrl():
  categoriesList=['Oči','Tvár', 'Pery', 'Nechty', 'Štetce a hubičky', 'Doplnky']
  categoriesUrlList=[]
  for catName in categoriesList:
    if soup.find_all('a', text=catName):
      urlPattern=soup.find('a', text=catName).get('href')
      if re.match('/\w+/\w+', urlPattern.strip()):
        url = f"https://www.pinkpanda.sk{urlPattern}"
        categoriesUrlList.append(url)
  return categoriesUrlList

categoriesUrlList = getCatUrl()

def getLastPage(url):
    r = requests.post(url=urlPink, data={ 'params[offset]': 1, 'view_type': 'all', 'category_id': category_id})
    soup = BeautifulSoup(r.json()['num_word'], 'html.parser')
    page = soup.find('div', {'class': 'pagination'})
    lastPage = int(page.find('strong', {'id': 'pagination-max-page'}).text)
    return lastPage

def getCategory(url): 
    r=requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    cat = soup.find_all('ul', class_='categories-listing')
    for c in cat:
        try:
            category = c.find('a', attrs={'class':'selected'}).text
            return category
        except Exception as e:
            continue
        
# prva strana 
productsList1=[]
for catUrl in categoriesUrlList:
    url = f'{catUrl}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    products = soup.find_all('div', class_='single-product-no-borders')
    for p in products:
        try:
            brand = p.find('a',attrs={'class':'sp-brand'}).text
            
            name = p.find('a', attrs={'class':'sp-title'}).text
            
            if p.find('div', attrs={'class': 'old-price'}):
              priceInt = p.find('div', class_='price').find('strong').contents[0]
              priceFloat = p.find('div', class_='price').find('sup').text
            
            else:
              priceInt = p.find('div', class_='price').find('span').contents[0]
              priceFloat = p.find('div', class_='price').find('sup').text
            
            price = priceInt + '.' + priceFloat
            price = float(price)
            
            url = f"https://www.pinkpanda.sk{p.find('a')['href']}"
            
            categorytmp = getCategory(url)
            if not categorytmp is None:
                category=categorytmp
            else:
                category="nešpecifikovaná"
            
            imageUrl = p.find('img').attrs['data-src']
            
            obj={
                  'Brand': brand.capitalize(),
                  'Name':name,
                  'Price':price,
                  'Category': category.capitalize(),
                  'Url':url,
                  'Image':imageUrl,
                  'Eshop': "pinkpanda"
            }
            
            productsList1.append(obj)
        except Exception as e:
            print(e)
            continue


urlPink = 'https://www.pinkpanda.sk/filter-products'
categoriesList = {
    'oci': 474,
    'tvar': 484,
    'pery': 493,
    'nechty': 505,
    'stetce a hubicky': 500,
    'doplnky': 509
}

productsList2=[]

for category, category_id in categoriesList.items():
  r = requests.post(url=urlPink, data={ 'params[offset]': 0, 'view_type': 'all', 'category_id': category_id})
  lp = (r.json()['all_num'] // 21) + 1
  for page in range(1, lp+1):
  # for page in range(1, 2):
    r = requests.post(url=urlPink, data={ 'params[offset]': page, 'view_type': 'all', 'category_id': category_id})
    soup = BeautifulSoup(r.json()['data'], 'html.parser')
    products = soup.find_all('div', class_='single-product-no-borders')
    for p in products:
        try:
            brand = p.find('a',attrs={'class':'sp-brand'}).text
            
            name = p.find('a', attrs={'class':'sp-title'}).text
            
            if p.find('div', attrs={'class': 'old-price'}):
              priceInt = p.find('div', class_='price').find('strong').contents[0]
              priceFloat = p.find('div', class_='price').find('sup').text
            
            else:
              priceInt = p.find('div', class_='price').find('span').contents[0]
              priceFloat = p.find('div', class_='price').find('sup').text
            
            price = priceInt + '.' + priceFloat
            price = float(price)
            
            url = f"https://www.pinkpanda.sk{p.find('a')['href']}"
            
            categorytmp = getCategory(url)
            if not categorytmp is None:
                category=categorytmp
            else:
                category="nešpecifikovaná"
            
            imageUrl = p.find('img').attrs['data-src']
            
            obj={
                  'Brand': brand.capitalize(),
                  'Name':name,
                  'Price':price,
                  'Category': category.capitalize(),
                  'Url':url,
                  'Image':imageUrl,
                  'Eshop': "pinkpanda"
            }
            
            productsList2.append(obj)
        except Exception as e:
            print(e)
            continue
        
productsList = productsList1+productsList2        
    
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
                  "Eshop": "pinkpanda"}},
                  upsert=True)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    