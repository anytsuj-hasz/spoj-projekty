# https://pl.spoj.com/problems/VSR/

n = int(input())
lista = []

for _ in range(n):
    pociagA, pociagB = input().split()
    sredniaPredkosc = (2 * int(pociagA) * int(pociagB)) / (int(pociagA) + int(pociagB))
    lista.append(int(sredniaPredkosc))

for wynik in lista:
    print(wynik)
