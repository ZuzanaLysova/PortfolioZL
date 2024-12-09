import json
import matplotlib.pyplot as plt

with open('data.json', 'r') as f:
    data = json.load(f)

brand_reviews = {}

for item in data:
    brand = item['Brand']
    reviews = item['Number of reviews']
    
    if brand in brand_reviews:
        brand_reviews[brand] += reviews
    else:
        brand_reviews[brand] = reviews



x = brand_reviews.keys()
y = brand_reviews.values()

plt.bar(x, y)
plt.title('Počet recenzí podle značek')
plt.xlabel('Brand')
plt.ylabel('Number of reviews')
plt.xticks(rotation=45)
plt.show()