import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import json
import csv

# vstupní data
with open("data.json", "r") as f:
    data = json.load(f)

X = np.zeros((len(data), 2))
y = np.zeros(len(data))
max_width = 0
min_width = float('inf')
max_height = 0
min_height = float('inf')
for i, d in enumerate(data):
    height = float(d["Technické parametry"]["Výška výrobku"].replace("cm", ""))
    width = float(d["Technické parametry"]["Šířka výrobku"].replace("cm", ""))
    X[i, 0] = height
    X[i, 1] = width
    y[i] = d["Price"]
    if width > max_width:
        max_width = width
    if width < min_width:
        min_width = width
    if height > max_height:
        max_height = height
    if height < min_height:
        min_height = height


# ridge regrese s alpha = 0.1
alpha = 0.1
n_features = X.shape[1]
beta = np.linalg.inv(X.T.dot(X) + alpha * np.identity(n_features)).dot(X.T).dot(y)

# vypočítání předpovědí pro rozsah hodnot vstupních dat
x1 = np.linspace(min_height, max_height, 100)
x2 = np.linspace(min_width, max_width, 100)
X_pred = np.array(np.meshgrid(x1, x2)).T.reshape(-1, 2)
y_pred = X_pred.dot(beta)


# vykreslení grafu
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# vykreslenie skutočných hodnôt
ax.scatter(X[:, 0], X[:, 1], y, s=20, c='r', marker='o', label='Skutočná cena TV')

# vykreslenie predikovaných hodnôt
#ax.scatter(X_pred[:, 0], X_pred[:, 1], y_pred, s=5, c=y_pred, cmap='cool', marker='o', label='Predikovaná cena')
ax.scatter(X_pred[:,0], X_pred[:,1], y_pred, s=8 , marker='o',  label='Predikovaná cena')

# nastavenie osí a popiskov
ax.set_xlabel('Výška [cm]')
ax.set_ylabel('Šírka [cm]')
ax.set_zlabel('Cena [Kč]')
plt.title('Predikcia ceny TV na základe šírky a výšky')
plt.legend(loc='upper center')
plt.show()
