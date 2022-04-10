from kalulator import Dodawanie, Odejmowanie, Mnozenie, Dzielenie, Modulo

iloscOperacji = int(input())
lista = []

for i in range(iloscOperacji):
    operacja, a, b = input().split()
    if operacja == "+":
        op = Dodawanie()
        wynik = op.licz_sume(int(a), int(b))
    elif operacja == "-":
        op = Odejmowanie()
        wynik = op.licz_roznice(int(a), int(b))
    elif operacja == "*":
        op = Mnozenie()
        wynik = op.licz_iloczyn(int(a), int(b))
    elif operacja == "/":
        op = Dzielenie()
        wynik = op.licz_iloraz(int(a), int(b))
    elif operacja == "%":
        op = Modulo()
        wynik = op.licz_modulo(int(a), int(b))
    else:
        print("Wprowadzileś zły znak")
    lista.append(wynik)

for wynik in lista:
    print(wynik)


