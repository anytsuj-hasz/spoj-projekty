# https://pl.spoj.com/problems/PP0602A/

class Wynik:
    def __init__(self, parzyste, nieparzyste):
        self.parzyste = parzyste
        self.nieparzyste = nieparzyste


def split_by_parity(liczby):
    parzyste = []
    nieparzyste = []
    for liczba in liczby:
        liczbaInt = int(liczba)
        if liczbaInt % 2 == 0:
            parzyste.append(liczbaInt)
        else:
            nieparzyste.append(liczbaInt)
    return Wynik(parzyste, nieparzyste)


liczby = input().split()
splited = split_by_parity(liczby)

print("Liczby parzyste: ", splited.parzyste)
print("Liczby nieparzyste: ", splited.nieparzyste)
