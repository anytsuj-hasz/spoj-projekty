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

# https://pl.spoj.com/problems/PTROL/

lista2 = []
liczby = input().split()
for liczba in liczby:
    liczbaInt = int(liczba)
    lista2.append(liczbaInt)

for i in range(1):
    lista2.append(lista2.pop(0))

print(lista2)

