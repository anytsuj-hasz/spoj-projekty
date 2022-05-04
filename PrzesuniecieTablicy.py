# https://pl.spoj.com/problems/PP0602D/

lista = []
liczby = input().split()
for liczba in liczby:
    liczbaInt = int(liczba)
    lista.append(liczbaInt)

print(lista)

przesuniecie = int(input())

for i in range(int(przesuniecie)):
    lista.append(lista.pop(0))

print(lista)

