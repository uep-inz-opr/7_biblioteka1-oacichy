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

k = 0
ksiazki = []
egzemplarze = []

n = input()
for i in range(0, int(n)):
    temp = eval(input())
    if not ksiazki:
        ksiazki.append(Ksiazka(temp[0], temp[1]))
    else:
        for i in range(len(ksiazki)):
            ks = ksiazki[i]
            if temp[0] != ks.tytul and temp[1] != ks.autor:
                k=1
    if k == 1:
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
    print("('"+temp.tytul+"',"+"'"+temp.autor+"',"+licznik)