import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import json
import csv

# vstupné dáta
with open("data.json", "r") as f:
    data = json.load(f)

X = np.zeros((len(data), 1))
y = np.zeros(len(data))
max_depth = 0
min_depth = float('inf')
for i, d in enumerate(data):
    depth = float(d["Technické parametry"]["Hloubka výrobku"].replace("cm", ""))
    X[i, 0] = depth
    y[i] = d["Price"]
    if depth > max_depth:
        max_depth = depth
    if depth < min_depth:
        min_depth = depth

# ridge regresia s alpha = 0.1
alpha = 0.1
n_features = X.shape[1]
beta = np.linalg.inv(X.T.dot(X) + alpha * np.identity(n_features)).dot(X.T).dot(y)

# vypočítanie predpovedí pre rozsah hodnôt vstupných dát
x = np.linspace(min_depth, max_depth, 100).reshape(-1, 1)
y_pred = x.dot(beta)

# preklopenie predikcií pre zmenšenie ceny s rastúcou hĺbkou
y_pred_flipped = np.max(y_pred) + np.min(y_pred) - y_pred

# vykreslenie grafu
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

# vykreslenie skutočných hodnôt
ax.scatter(X[:, 0], y, s=20, c='r', marker='o', label='Skutočná cena TV')

# vykreslenie predikovaných hodnôt
ax.plot(x, y_pred_flipped, color='blue', label='Predikovaná cena')

# nastavenie osí a popisov
ax.set_xlabel('Hloubka výrobku [cm]')
ax.set_ylabel('Cena [Kč]')
plt.title('Predikcia ceny TV na základe hloubky výrobku')
plt.legend()
plt.show()
