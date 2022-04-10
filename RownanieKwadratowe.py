# https://pl.spoj.com/problems/ROWNANIE/

lista = []


def ile_pierwiastkow_rzeczywistych(a, b, c):
    delta = float(b) ** 2 - (4 * float(a) * float(c))
    if delta > 0:
        return 2
    elif delta == 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    for i in range(3):
        wspA, wspB, wspC = input().split()
        ilosc = ile_pierwiastkow_rzeczywistych(wspA, wspB, wspC)
        lista.append(ilosc)

    for wynik in lista:
        print(wynik)
