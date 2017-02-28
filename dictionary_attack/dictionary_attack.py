import hashlib
import threading

global tablica_odczytanych
global tablica_zakodowanych_hasel
global tablica_odkodowanych_hasel
global slownik
global hasla
global lock
global rozmiar

#Dodaje wlasnie jakies zmiany do pliku
rozmiar=100
tablica_zakodowanych_hasel=[]
tablica_odkodowanych_hasel=[]
tablica_odczytanych=[]
lock=threading.Lock()

def koduj(arg1):
    zakodowany=hashlib.md5(arg1.encode('utf-8'))
    return zakodowany.hexdigest()

def odczytaj_z_pliku():
    plik=[]
    nazwa_pliku=input()
    for x in open(nazwa_pliku,'r'):
        x=x.strip()
        plik.append(x)
    return plik


def producent0():
    liczba=0
    for linia in slownik:
        for i in range(rozmiar):
            for j in range(rozmiar):
                slowo = linia.lower()
                i = str(i)
                j = str(j)
                slowo = i + slowo + j
                i = int(i)
                j = int(j)
                zakodowane_haslo = koduj(slowo)
                if zakodowane_haslo in hasla:
                    lock.acquire()
                    try:
                        hasla.remove(zakodowane_haslo)
                        tablica_zakodowanych_hasel.append(zakodowane_haslo)
                        tablica_odkodowanych_hasel.append(slowo)
                    finally:
                        lock.release()
    for linia in slownik:
        slowo = linia.lower()
        zakodowane_haslo = koduj(slowo)
        if zakodowane_haslo in hasla:
            lock.acquire()
            try:
                tablica_zakodowanych_hasel.append(zakodowane_haslo)
                tablica_odkodowanych_hasel.append(slowo)
                hasla.remove(zakodowane_haslo)
            finally:
                lock.release()

    while True:
        for linia in slownik:
            slowo = linia.lower()
            liczba=str(liczba)
            slowo=slowo+liczba
            liczba=int(liczba)
            zakodowane_haslo=koduj(slowo)
            if zakodowane_haslo in hasla:
                lock.acquire()
                try:
                    tablica_zakodowanych_hasel.append(zakodowane_haslo)
                    tablica_odkodowanych_hasel.append(slowo)
                    hasla.remove(zakodowane_haslo)
                finally:
                    lock.release()
        for linia in slownik:
            slowo = linia.lower()
            liczba=str(liczba)
            slowo=slowo+liczba
            liczba=int(liczba)
            zakodowane_haslo=koduj(slowo)
            if zakodowane_haslo in hasla:
                lock.acquire()
                try:
                    tablica_zakodowanych_hasel.append(zakodowane_haslo)
                    tablica_odkodowanych_hasel.append(slowo)
                    hasla.remove(zakodowane_haslo)
                finally:
                    lock.release()
        liczba+=1



def producent1():
    liczba=0
    for linia in slownik:
        for i in range(rozmiar):
            for j in range(rozmiar):
                slowo = linia[0].upper() + linia[1:].lower()
                i = str(i)
                j = str(j)
                slowo = i + slowo + j
                i = int(i)
                j = int(j)
                zakodowane_haslo = koduj(slowo)
                if zakodowane_haslo in hasla:
                    lock.acquire()
                    try:
                        hasla.remove(zakodowane_haslo)
                        tablica_zakodowanych_hasel.append(zakodowane_haslo)
                        tablica_odkodowanych_hasel.append(slowo)
                    finally:
                        lock.release()

    for linia in slownik:
        slowo = linia[0].upper() + linia[1:].lower()
        zakodowane_haslo = koduj(slowo)
        if zakodowane_haslo in hasla:
            lock.acquire()
            try:
                tablica_zakodowanych_hasel.append(zakodowane_haslo)
                tablica_odkodowanych_hasel.append(slowo)
                hasla.remove(zakodowane_haslo)
            finally:
                lock.release()

    while True:
        for linia in slownik:
            slowo = linia[0].upper()+linia[1:].lower()
            liczba=str(liczba)
            slowo=slowo+liczba
            liczba=int(liczba)
            zakodowane_haslo=koduj(slowo)
            if zakodowane_haslo in hasla:
                lock.acquire()
                try:
                    hasla.remove(zakodowane_haslo)
                    tablica_zakodowanych_hasel.append(zakodowane_haslo)
                    tablica_odkodowanych_hasel.append(slowo)
                finally:
                    lock.release()
        for linia in slownik:
            slowo = linia[0].upper()+linia[1:].lower()
            liczba=str(liczba)
            slowo=liczba+slowo
            liczba=int(liczba)
            zakodowane_haslo=koduj(slowo)
            if zakodowane_haslo in hasla:
                lock.acquire()
                try:
                    hasla.remove(zakodowane_haslo)
                    tablica_zakodowanych_hasel.append(zakodowane_haslo)
                    tablica_odkodowanych_hasel.append(slowo)
                finally:
                    lock.release()
        liczba+=1


def producent2():
    liczba=0

    for linia in slownik:
        for i in range(rozmiar):
            for j in range(rozmiar):
                slowo = linia.upper()
                i = str(i)
                j = str(j)
                slowo = i + slowo + j
                i = int(i)
                j = int(j)
                zakodowane_haslo = koduj(slowo)
                if zakodowane_haslo in hasla:
                    lock.acquire()
                    try:
                        hasla.remove(zakodowane_haslo)
                        tablica_zakodowanych_hasel.append(zakodowane_haslo)
                        tablica_odkodowanych_hasel.append(slowo)
                    finally:
                        lock.release()

    for linia in slownik:
        slowo = linia.upper()
        zakodowane_haslo = koduj(slowo)
        if zakodowane_haslo in hasla:
            lock.acquire()
            try:
                tablica_zakodowanych_hasel.append(zakodowane_haslo)
                tablica_odkodowanych_hasel.append(slowo)
                hasla.remove(zakodowane_haslo)
            finally:
                lock.release()

    while True:
        for linia in slownik:
            slowo = linia.upper()
            liczba=str(liczba)
            slowo=slowo+liczba
            liczba=int(liczba)
            zakodowane_haslo=koduj(slowo)
            if zakodowane_haslo in hasla:
                lock.acquire()
                try:
                    hasla.remove(zakodowane_haslo)
                    tablica_zakodowanych_hasel.append(zakodowane_haslo)
                    tablica_odkodowanych_hasel.append(slowo)
                finally:
                    lock.release()
        for linia in slownik:
            slowo = linia.upper()
            liczba=str(liczba)
            slowo=slowo+liczba
            liczba=int(liczba)
            zakodowane_haslo=koduj(slowo)
            if zakodowane_haslo in hasla:
                lock.acquire()
                try:
                    hasla.remove(zakodowane_haslo)
                    tablica_zakodowanych_hasel.append(zakodowane_haslo)
                    tablica_odkodowanych_hasel.append(slowo)
                finally:
                    lock.release()
        liczba+=1

def producent3():
    liczba=0

    for linia1 in slownik:
        for linia2 in slownik:
            slowo=linia1.lower()+linia2.lower()
            zakodowane_haslo=koduj(slowo)
            if zakodowane_haslo in hasla:
                lock.acquire()
                try:
                    hasla.remove(zakodowane_haslo)
                    tablica_zakodowanych_hasel.append(zakodowane_haslo)
                    tablica_odkodowanych_hasel.append(slowo)
                finally:
                    lock.release()

    while True:
        for linia1 in slownik:
            for linia2 in slownik:
                slowo = linia1.lower() + linia2.lower()
                liczba=str(liczba)
                slowo=slowo+liczba
                zakodowane_haslo=koduj(slowo)
                if zakodowane_haslo in hasla:
                    lock.acquire()
                    try:
                        hasla.remove(zakodowane_haslo)
                        tablica_zakodowanych_hasel.append(zakodowane_haslo)
                        tablica_odkodowanych_hasel.append(slowo)
                    finally:
                        lock.release()
                slowo=linia1.lower()+linia2.lower()
                slowo=liczba+slowo
                zakodowane_haslo=koduj(slowo)
                if zakodowane_haslo in hasla:
                    lock.acquire()
                    try:
                        hasla.remove(zakodowane_haslo)
                        tablica_zakodowanych_hasel.append(zakodowane_haslo)
                        tablica_odkodowanych_hasel.append(slowo)
                    finally:
                        lock.release()
                liczba=int(liczba)
        liczba += 1

def producent4():
    liczba=0

    for linia1 in slownik:
        for linia2 in slownik:
            slowo=linia1.upper()+linia2.upper()
            zakodowane_haslo=koduj(slowo)
            if zakodowane_haslo in hasla:
                lock.acquire()
                try:
                    hasla.remove(zakodowane_haslo)
                    tablica_zakodowanych_hasel.append(zakodowane_haslo)
                    tablica_odkodowanych_hasel.append(slowo)
                finally:
                    lock.release()

    while True:
        for linia1 in slownik:
            for linia2 in slownik:
                slowo = linia1.upper() + linia2.upper()
                liczba=str(liczba)
                slowo=slowo+liczba
                zakodowane_haslo=koduj(slowo)
                if zakodowane_haslo in hasla:
                    lock.acquire()
                    try:
                        hasla.remove(zakodowane_haslo)
                        tablica_zakodowanych_hasel.append(zakodowane_haslo)
                        tablica_odkodowanych_hasel.append(slowo)
                    finally:
                        lock.release()
                slowo=linia1.upper()+linia2.upper()
                slowo=liczba+slowo
                zakodowane_haslo=koduj(slowo)
                if zakodowane_haslo in hasla:
                    lock.acquire()
                    try:
                        hasla.remove(zakodowane_haslo)
                        tablica_zakodowanych_hasel.append(zakodowane_haslo)
                        tablica_odkodowanych_hasel.append(slowo)
                    finally:
                        lock.release()
                liczba=int(liczba)
        liczba += 1
def producent5():
    liczba=0
    znaki=[".","_","@","-","&"]

    while liczba<5:
        for linia1 in slownik:
            for linia2 in slownik:
                for x in znaki:
                    liczba=str(liczba)
                    slowo=linia1.lower()+linia2.lower()+x+liczba
                    zakodowane_haslo=koduj(slowo)
                    liczba=int(liczba)
                    if zakodowane_haslo in hasla:
                        lock.acquire()
                        try:
                            hasla.remove(zakodowane_haslo)
                            tablica_zakodowanych_hasel.append(zakodowane_haslo)
                            tablica_odkodowanych_hasel.append(slowo)
                        finally:
                            lock.release()
        liczba+=1

def producent6():
    while True:
        print("Podaj haslo do sprawdzenia: ('T' konczy prace programu)")
        x=input()
        if x=="T":
            exit(0)
        zakodowane_haslo=koduj(x)
        if zakodowane_haslo in hasla:
            lock.acquire()
            try:
                hasla.remove(zakodowane_haslo)
                tablica_zakodowanych_hasel.append(zakodowane_haslo)
                tablica_odkodowanych_hasel.append(slowo)
                print("zakodowane haslo: ", x)
            finally:
                lock.release()
        else:
            print("Nie ma takiego hasła")

def konsument():

    dlugosc=0
    while(True):
        if dlugosc<len(tablica_zakodowanych_hasel):
            lock.acquire()
            try:
                print("odgadniete haslo1: ", tablica_odkodowanych_hasel[dlugosc])
                dlugosc+=1
            finally:
                lock.release()



slownik=[]
hasla=[]

slownik=odczytaj_z_pliku()
hasla=odczytaj_z_pliku()



watek0=threading.Thread(target=producent0)
watek1=threading.Thread(target=producent1)
watek2=threading.Thread(target=producent2)
watek3=threading.Thread(target=producent3)
watek4=threading.Thread(target=producent4)
watek5=threading.Thread(target=producent5)
watek6=threading.Thread(target=producent6)
watek7=threading.Thread(target=konsument)

#print("watek 7 startuje")
watek7.start()

#print("watek 0 startuje")
watek0.start()
#print("watek 1 startuje")
watek1.start()
#print("watek 2 startuje")
watek2.start()
#print("watek 3 startuje")
watek3.start()
#print("watek 4 startuje")
watek4.start()
#print("watek 5 startuje")
watek5.start()
#print("watek 6 startuje")
watek6.start()


