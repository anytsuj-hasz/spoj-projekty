# https://pl.spoj.com/problems/JSZYCER/

klucz = 3
firstLetterIndex = 65
lettersAmount = 26

def szyfruj(tekst):
    zaszyfrowany = ""
    for i in range(len(tekst)):
        if (ord(tekst[i]) < 88 and ord(tekst[i]) > 64):
            zaszyfrowany = zaszyfrowany + chr(ord(tekst[i]) + klucz)
        elif (ord(tekst[i]) > 87 and ord(tekst[i]) < 91):
            zaszyfrowany = zaszyfrowany + chr(ord(tekst[i]) + klucz - 26)
        else:
            zaszyfrowany = zaszyfrowany + tekst[i]
    return zaszyfrowany

def szyfruj2(tekst):
    zaszyfrowany = ""
    for i in range(len(tekst)):
        litera = tekst[i]
        literaIndex = ord(litera)
        if firstLetterIndex <= literaIndex < firstLetterIndex + lettersAmount:
            x1 = literaIndex - firstLetterIndex
            x2 = x1 + klucz
            x3 = x2 % lettersAmount
            x4 = x3 + firstLetterIndex
            x5 = chr(x4)
            zaszyfrowany += x5
        else:
            zaszyfrowany += litera
    return zaszyfrowany


tekst = input("Podaj tekst: ")
print(szyfruj2(tekst))
