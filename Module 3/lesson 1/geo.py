while 1:
    g = int(input("Городское: "))
    s = int(input("Сельское: "))
    p = int(input("Площадь: "))

    nasel = (g + s) / 1000000
    nasel = round(nasel, 1)

    plotnost = (g + s) / p
    plotnost = round(plotnost, 1)

    urban = g / (g + s) * 100
    urban = round(urban, 1)

    print()
    print("Численность населения: ", nasel)
    print("Плотность населения: ", plotnost)
    print("Уровень урбанизации", urban, end="\n-------------------------------\n\n")
