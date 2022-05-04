# https://pl.spoj.com/problems/JROWLIN/

def ile_rozwiazan(a, b, c):
    if a != 0:
        return (c-b)/a
    elif a == 0 and b == c:
        return "NWR"
    else:
        return "BR"


wspA, wspB, wspC = input().split()
wynik = ile_rozwiazan(float(wspA), float(wspB), float(wspC))
print(round(wynik, 2))