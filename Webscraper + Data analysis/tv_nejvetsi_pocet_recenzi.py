import pandas as pd
import json
import matplotlib.pyplot as plt

# Načtení dat z json souboru
with open('data.json') as f:
    data = json.load(f)

# Převedení dat na pandas DataFrame
df = pd.DataFrame(data)

# Konverze počtu recenzí na numerickou hodnotu
df['Number of reviews'] = pd.to_numeric(df['Number of reviews'])

# Seřazení televizí podle počtu recenzí sestupně a výběr prvních 10
top_10 = df.sort_values('Number of reviews', ascending=False).head(10)

# Vytvoření grafu s názvy televizí na ose x
plt.bar(top_10['Name'], top_10['Number of reviews'])
plt.xticks(rotation=45, ha='right')

plt.xlabel('Názvy televizí')
plt.ylabel('Počet recenzí')
plt.title('10 televizí s největším počtem recenzí')
plt.show()