import json
import re
import requests
from bs4 import BeautifulSoup

url_tmp = 'https://www.datart.cz/televize/filter/o:3'

response_tmp = requests.get(url_tmp)
soup_tmp = BeautifulSoup(response_tmp.content, 'html.parser')

products_count_span = soup_tmp.find('div', class_ = 'category-content box-shadow').find('h1').find('span').text
products_count = int(re.sub('[^0-9]+', '', products_count_span))
# products_count = 16
# print(products_count)

url = f'https://www.datart.cz/televize/filter/o:3?showPage&page=1&limit={products_count}'


response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

productsList=[]
products = soup.find_all('div', class_= 'product-box')


for p in products:
    try:
        name = p.find('div', class_= 'product-box-top-side').find('div', attrs={'class':'item-title-holder'}).find('h3', attrs={'class':'item-title'}).find('a').get('data-lb-name').split(" - ")[0]
        brand = p.find('div', class_= 'product-box-top-side').find('div', attrs={'class':'item-title-holder'}).find('h3', attrs={'class':'item-title'}).find('a').get('data-lb-name').split(" ")[1]
        price = p.find('div', class_= 'product-box-info').find('div', class_= 'item-price').get('data-product-price')
        rating = p.find('div', class_ = 'item-rating').find('span', class_ = 'bold')
        rating_count = p.find('div', class_ = 'item-rating').find('span', class_ = 'underlined')
        rating_count_none = p.find('span', class_ = 'item-rating-info underlined')
        url_part = p.find('div', class_= 'product-box-top-side').find('h3', attrs={'class': 'item-title'}).find('a').get('href')
        p_url = f"https://www.datart.cz/{url_part}"
        
        if rating == None:
            rating = 0
        else:
            rating = rating.text.strip()

        if rating_count_none:
            rating_count = 0
        else:
            rating_count = rating_count.text.strip()

        p_response = requests.get(p_url)
        p_soup = BeautifulSoup(p_response.content, 'html.parser')
        p_parameters = p_soup.find('div', class_ = "product-property").find('table')
        technical_params = {}
        try:
            for tr in p_parameters.find_all("tbody"):
                for row in tr.find_all("tr"):
                    key = row.find("th").find("span").text.strip()
                    value = row.find("td").text.strip()
                    technical_params[key] = value
        except Exception as e:
            print(p_url + e)
            continue
        obj={
            'Name':name,
            'Brand':brand,
            'Price': int(price),
            'Rating': float(rating),
            'Number of reviews': int(rating_count),
            'Url': p_url,
            'Technické parametry': technical_params
        }
        productsList.append(obj)
    except Exception as e:
            print(e)
            continue

output_file = './data/data.json'
with open(output_file, 'w', encoding="utf-8") as file:
    # for product in productsList:
    json.dump(productsList, file, indent=4, ensure_ascii=False)
