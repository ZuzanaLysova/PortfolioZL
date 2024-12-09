import json
import matplotlib.pyplot as plt

# Načtení dat ze souboru JSON
with open('data.json', 'r') as file:
    data = json.load(file)

# Vybrání 10 nejdražších televizí
most_expensive = sorted(data, key=lambda x: x['Price'], reverse=False)[:10]

# Rozdělení dat na dvě seznamy - ceny a názvy
prices = [item['Price'] for item in most_expensive]
names = [item['Name'] for item in most_expensive]

# Vytvoření sloupcového grafu
plt.bar(range(len(prices)), prices)

# Nastavení popisků os a názvu grafu
plt.xlabel('Name')
plt.ylabel('Price')
plt.title('Top 10 Most Cheapest Televisions')

# Zalomení názvů na ose X
plt.xticks(range(len(names)), names, rotation=45, ha='right')

# Zobrazení grafu
plt.show()