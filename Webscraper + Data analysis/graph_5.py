import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def main():
    # Načítanie dát z JSON súboru
    with open("data.json", "r") as f:
        data = json.load(f)

    widths = []
    energy_classes = []
    prices = []
    smart_tvs = []

    # Mapovanie retazcov energetických tried na čísla
    energy_class_mapping = {"D": 0, "E": 1, "F": 2, "G": 3}

    # Extrahovanie údajov z dát
    for d in data:
        try:
            width = float(d["Technické parametry"]["Úhlopříčka obrazovky"].split()[0])
            energy_class = d["Technické parametry"]["Energetická třída 2021"]
            energy_class_num = energy_class_mapping[energy_class]
            price = float(d["Price"])

            smart_tv_val = d["Technické parametry"].get("Smart TV") == "ano" if "Smart TV" in d["Technické parametry"] else False
            smart_tvs.append(smart_tv_val)

        except (ValueError, KeyError):
            continue  # Preskočenie záznamu, kde sú chýbajúce údaje

        widths.append(width)
        energy_classes.append(energy_class_num)
        prices.append(price)


    # Vytvorenie 3D grafu
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Farbenie bodov na základe hodnoty SMART TV
    colors = ['r' if s else 'b' for s in smart_tvs]
    ax.scatter(widths, energy_classes, prices, c=colors)

    # Vytvorenie legendy
    red_patch = plt.plot([], [], marker='o', ms=10, ls="", mec=None, color='r', label='Smart TV')
    blue_patch = plt.plot([], [], marker='o', ms=10, ls="", mec=None, color='b', label='Non-Smart TV')
    plt.legend(handles=[red_patch[0], blue_patch[0]])

    # Nastavenie titulku a popisov osí
    ax.set_title('Cena TV na základe úhlopriečky, energetickej triedy a SMART TV')
    ax.set_xlabel('Úhlopriečka [px]')
    ax.set_ylabel('Energetická trieda')
    ax.set_zlabel('Cena [Kč]')

    # Nastavenie vlastností popisu osí
    ax.tick_params(axis='both', labelsize=10)
    ax.set_yticks(list(energy_class_mapping.values()))
    ax.set_yticklabels(list(energy_class_mapping.keys()))

    # Zobrazenie grafu
    plt.show()


if __name__ == '__main__':
    main()
