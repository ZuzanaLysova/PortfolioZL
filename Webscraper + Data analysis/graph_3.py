import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Načítanie dát z JSON súboru
with open("data.json", "r") as f:
    data = json.load(f)

widths = []
heights = []
depths = []
prices = []

# Extrahovanie údajov z dát
for d in data:
    try:
        width = float(d["Technické parametry"]["Šířka výrobku"].replace("cm", ""))
        height = float(d["Technické parametry"]["Výška výrobku"].replace("cm", ""))
        depth = float(d["Technické parametry"]["Hloubka výrobku"].replace("cm", ""))
        price = float(d["Price"])
    except ValueError:
        continue  # Preskočenie záznamu, kde sú chýbajúce údaje

    widths.append(width)
    heights.append(height)
    depths.append(depth)
    prices.append(price)

# Vytvorenie 3D grafu
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(widths, heights, depths, c=prices, cmap='cool')

# Nastavenie titulku a popisov osí
ax.set_title('Cena TV na základe rozmerov')
ax.set_xlabel('Šírka [cm]')
ax.set_ylabel('Výška [cm]')
ax.set_zlabel('Hĺbka [cm]')
cbar = fig.colorbar(ax.scatter(widths, heights, depths, c=prices, cmap='cool'))
cbar.ax.set_ylabel('Cena [Kč]')

# Nastavenie vlastností popisu osí
ax.tick_params(axis='both', labelsize=10)

# Zobrazenie grafu
plt.show()
