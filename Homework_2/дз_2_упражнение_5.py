price = [57.8, 46.51, 97, 67.09, 67.04, 27.22, 26.12, 82.8, 73.41,
         36.8, 55.37, 65.09, 40.7, 26, 93.3, 29, 121, 61.5, 910.7]
kopecks = 0
rubles = 0
for i in price:
    kopecks = str(round((i % 1), 2))
    kopecks = kopecks[2:]
    rubles = int(i // 1)
    while len(kopecks) < 2:
        kopecks += "0"

    print(rubles, "руб", kopecks, "коп")