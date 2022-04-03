# https://pl.spoj.com/problems/RNO_DOD/


def sumuj_liste():
    lista = []
    iloscElementow = int(input())
    liczby = input().split()
    if not len(liczby) == iloscElementow:
        raise Exception
    for liczba in liczby:
        liczbaInt = int(liczba)
        lista.append(liczbaInt)
    wynik = (sum(lista))
    return wynik


iloscList = int(input())
wyniki = []

for _ in range(iloscList):
    wynik = sumuj_liste()
    wyniki.append(wynik)

for wynik in wyniki:
    print(wynik)

