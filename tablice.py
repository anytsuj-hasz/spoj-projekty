# https://pl.spoj.com/problems/PP0502B/


def odwroc_elementy():
    lista = []
    liczby = input().split()
    iloscElementow = int(liczby[0])
    if not len(liczby) - 1 == iloscElementow:
        raise Exception
    for liczba in liczby[1:]:
        liczbaInt = int(liczba)
        lista.append(liczbaInt)
    lista.reverse()
    return lista


iloscList = int(input())
wyniki = []

for _ in range(iloscList):
    wynik = odwroc_elementy()
    wyniki.append(wynik)

for wynik in wyniki:
    print(" ".join(map(lambda x: str(x), wynik)))
