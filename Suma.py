# https://pl.spoj.com/problems/SUMA/

lista = []
suma = 0


def is_castable_to_int(maybe_number):
    try:
        int(maybe_number)
        return True
    except ValueError:
        return False


liczba = input()
while is_castable_to_int(liczba):
    suma = suma + int(liczba)
    lista.append(suma)
    liczba = input()

for wynik in lista:
    print(wynik)
