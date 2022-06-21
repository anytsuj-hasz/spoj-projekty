# https://pl.spoj.com/problems/PP0501A/


def nwd(liczbaA, liczbaB):
    while liczbaB > 0:
        reszta = liczbaA % liczbaB
        liczbaA = liczbaB
        liczbaB = reszta
    return liczbaA


liczbaA = int(input("Podaj pierwszą liczbę: "))
liczbaB = int(input("Podaj drugą liczbę: "))

print(nwd(liczbaA, liczbaB))
