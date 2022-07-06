# https://pl.spoj.com/problems/JPESEL/


def split(word):
    return [char for char in word]


# licz_sume powinno przyjmować 'lista' jako argument. Teraz bazuje na tym, że taka zmienna po prostu istnieje globalnie przed wywołaniem
def licz_sume(lista):
    iloczyn = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
    wynik = []
    for i in range(len(lista)):
        wynik.append(lista[i] * iloczyn[i])
    suma = sum(wynik)
    return suma


pesel = split(input())
lista = []
for znak in pesel:
    znakInt = int(znak)
    lista.append(znakInt)

suma = licz_sume(lista)

if suma % 10 == 0:
    print("D")
else:
    print("N")
