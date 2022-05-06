import ast

class Ksiazka:
    def __init__ (self, tytul, autor):
        self.tytul = tytul
        self.autor = autor

class Egzemplarz():
    def __init__ (self, tytul, autor, rok_wyd):
        self.tytul = tytul
        self.autor = autor
        self.rok_wyd = rok_wyd

def sortowanie(Ksiazka):
    return Ksiazka.tytul

def czyjestwliscie(ksiazki, tytul, autor):
    for i in range(len(ksiazki)):
        ks = ksiazki[i]
        if tytul == ks.tytul and autor == ks.autor:
            return True
    return False
    
ksiazki = []
egzemplarze = []

n = input()
for i in range(0, int(n)):
    k=0
    temp = eval(input())
    if not ksiazki:
        ksiazki.append(Ksiazka(temp[0], temp[1]))
    else:
        czyjuzjest = czyjestwliscie(ksiazki, temp[0], temp[1])
        if czyjuzjest is False:
            ksiazki.append(Ksiazka(temp[0], temp[1]))
    egzemplarze.append(Egzemplarz(temp[0], temp[1], temp[2]))

ksiazki.sort(key=sortowanie)

for i in range(len(ksiazki)):
    licznik = 0
    temp = ksiazki[i]
    for i in range(len(egzemplarze)):
        eg = egzemplarze[i]
        if temp.tytul == eg.tytul and temp.autor == eg.autor:
            licznik = licznik + 1
    licznik = str(licznik)
    print("('"+temp.tytul+"',","'"+temp.autor+"',",licznik+")")