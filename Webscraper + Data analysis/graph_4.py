import json
import matplotlib.pyplot as plt

with open('data.json') as f:
    data = json.load(f)

brand_prices = {}

for tv in data:
    brand = tv['Brand']
    price = tv['Price']
    if brand in brand_prices:
        brand_prices[brand].append(price)
    else:
        brand_prices[brand] = [price]

# Vytvoríme dáta pre graf
brands = list(brand_prices.keys())
avg_prices = [sum(brand_prices[brand])/len(brand_prices[brand]) for brand in brands]

# Vykreslíme stĺpcový graf
plt.figure(figsize=(15, 8))
plt.bar(brands, avg_prices)
plt.title('Priemerná cena televízorov podľa značiek')
plt.xlabel('Značka')
plt.ylabel('Priemerná cena [Kč]')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.subplots_adjust(bottom=0.2)
plt.show()
