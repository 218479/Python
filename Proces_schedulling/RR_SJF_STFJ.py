from operator import attrgetter
from collections import deque
global liczba_procesorow

global liczba_procesow
global tmp
global plik

class Proces:
    def __init__(self,i,r,p):
        self.numer_procesu=i
        self.czas=r
        self.priorytet=p
    def dekrementuj(self):
        if self.czas>0:
            self.czas-=1
    def wypisz(self):
        print("numer: {} czas: {}  priorytet: {}".format(self.numer_procesu,self.czas,self.priorytet))


def SRTF():
    global liczba_procesow
    liczba_procesow=[]
    for line in plik:
        dane = deque(line.split())
        czas_dzialania = dane.popleft()
        print(czas_dzialania)
        while (len(dane) >= 3):  # wczytujemy procesy z jednej linii
            x = int(dane.popleft())
            y = int(dane.popleft())
            z = int(dane.popleft())
            liczba_procesow.append(Proces(x, y, z))

        liczba_procesow = sorted(liczba_procesow, key=attrgetter('czas', 'numer_procesu'))

        for i in range(liczba_procesorow):
            if len(liczba_procesow)>i:
                liczba_procesow[i].wypisz()

        for x in range(liczba_procesorow):
            if len(liczba_procesow) > x:
                liczba_procesow[x].dekrementuj()

        for i in range(len(liczba_procesow)):
            if len(liczba_procesow) > i and liczba_procesow[i].czas == 0:
                liczba_procesow.pop(i)

        for i in range(len(liczba_procesow)):
            if len(liczba_procesow) > i and liczba_procesow[i].czas == 0:
                liczba_procesow.pop(i)



def RR():
    global liczba_procesow
    liczba_procesow=[]

    for line in plik:
        dane = deque(line.split())
        czas_dzialania = dane.popleft()
        print(czas_dzialania)
        while (len(dane) >= 3):  # wczytujemy procesy z jednej linii
            x = int(dane.popleft())
            y = int(dane.popleft())
            z = int(dane.popleft())
            liczba_procesow.append(Proces(x, y, z))

        for i in range(liczba_procesorow):
            if len(liczba_procesow) > i:
                liczba_procesow[i].wypisz()

        for x in range(liczba_procesorow):
            if len(liczba_procesow)>x:
                liczba_procesow[0].dekrementuj()
                liczba_procesow.append(liczba_procesow.pop(0))

        for i in range(len(liczba_procesow)):
            if len(liczba_procesow) > i and liczba_procesow[i].czas == 0:
                liczba_procesow.pop(i)



def SJF():
    global liczba_procesow
    liczba_procesow = []

    for line in plik:
        dane = deque(line.split())
        czas_dzialania = dane.popleft()
        print(czas_dzialania)

        while (len(dane) >= 3):  # wczytujemy procesy z jednej linii
            x = int(dane.popleft())
            y = int(dane.popleft())
            z = int(dane.popleft())
            liczba_procesow.append(Proces(x, y, z))

        for x in range(liczba_procesorow):
            if len(liczba_procesow) > x:
                liczba_procesow[x].dekrementuj()
        for i in range(liczba_procesorow):
            if len(liczba_procesow) > i:
                liczba_procesow[i].wypisz()
        for x in range(liczba_procesorow):
            if len(liczba_procesow) > x and liczba_procesow[x].czas == 0:
                liczba_procesow.pop(x)


print("Podaje nazwa pliku: ")
nazwa_pliku=input()

print("Podaj liczbe procesorow: ")
liczba_procesorow=int(input())

plik=open(nazwa_pliku,'r')
print("Wybierz stategie: ")
print("1.RR\n2.SJF\n3.SRTF z wywlaszczaniem\n")

wybor=input()
wybor=int(wybor)
if wybor==1:
    RR()
if wybor==2:
    SJF()
if wybor==3:
    SRTF()
