# https://pl.spoj.com/problems/PP0604A/


def licz_sredniaArytm(tablica):
    suma = sum(tablica)
    sredniaArytmetyczna = suma / len(tablica)
    return sredniaArytmetyczna


def licz_odleglosc(element, srednia):
    return abs(element - srednia)


lista = input().split()
tablica = []

for element in lista:
    elementInt = int(element)
    tablica.append(elementInt)

srednia = licz_sredniaArytm(tablica)

najlepszyElement = tablica[0]

for element in tablica:
    if licz_odleglosc(element, srednia) < licz_odleglosc(najlepszyElement, srednia):
        najlepszyElement = element

print(najlepszyElement)

