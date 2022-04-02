n = int(input())

lista = []

for _ in range(n):
    liczbaA, liczbaB = input().split()
    wynik = int(liczbaA) ** int(liczbaB)
    wynikJednosci = wynik % 10
    lista.append(wynikJednosci)

for wynik in lista:
    print(wynik)
