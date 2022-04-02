n = int(input())


lista=[]


def czy_pierwsza(n):
    if n <= 1:
        return False

    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True


for _ in range(n):
    liczba = int(input())
    if czy_pierwsza(liczba):
        lista.append("TAK")
    else:
        lista.append("NIE")

for wynik in lista:
    print(wynik)
