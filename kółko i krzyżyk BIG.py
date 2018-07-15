# coding=UTF-8
# Kółko i krzyżyk - wersja BIG
# gra toczy się na planszy 10x10
# a żeby wygrać trzeba ustawić pięć znaków
# w jednej linii prostej, bądź skośnej
#
# pseudokod
# 
# utwórz pustą planszę - zrobione
# ustal pierwszy ruch (zmienna ruch='czlowiek' albo 'komputer')
# dopóki <nie wygrana> albo <nie ma więcej pól>:
#   wyświetl planszę
#   wprowadź ruch
# napisy końcowe
#
# koniec pseudokodu

import random # potrzebne na razie do funkcji RuchKomputera()


def UtworzPustaPlansze (rozmiar):
    """Tworzy pustą planszę w formie kwadratu o rozmiarze <rozmiar>- zwraca []"""
    tablica=[0]*rozmiar # najpierw tworzymy listę z <wierszy> elementów
                        # elementy listy mogą być dowolne
    for i in range (rozmiar):
        tablica[i]=[" "]*rozmiar
    return tablica
    
    
def TakLubNie (pytanie, domyslnie=True):
    """Zadaje pytanie i zwraca odpowiedź użytkownika"""
    odpowiedz=None
    while odpowiedz not in ("t", "n", ""):
        print (pytanie, end=" ")
        if domyslnie:
            print ("(T/n)", end=" ")
        else:
            print ("(t/N)", end=" ")
        odpowiedz = input().lower()
        if odpowiedz == "t":
            return True
        if odpowiedz == "n":
            return False
        if odpowiedz == "":
            return domyslnie

def Wygrana():
    """zwraca X, O, albo False"""
    for x in range (0, ROZMIAR_PLANSZY):
        for y in range (0, ROZMIAR_PLANSZY):
            for kierunek in ("poziom", "pion", "skos prawy", "skos lewy"):
                iksy, kolka = SprawdzLinie ((x, y), kierunek)
                if iksy == 5:
                    return X
                if kolka == 5:
                    return O
    return False 
    
def WszystkieZajete():
    """zwraca True, jeśli wszystkie pola są zajęte, a False, jeśli jest choć jedno wolne"""
    for i in plansza:
        if PUSTY in i:
            return False
    return True
        
def WyswietlPlansze():
    """Wyświetla planszę na ekranie"""
    print (CLS)
    print ("-" * (ROZMIAR_PLANSZY * 4+1)) 
    for rząd in plansza:
        print ("| ", end="")
        for element in rząd:
            print (element, end=" | ")
        print("") # nowy wiersz
        print ("-" * (ROZMIAR_PLANSZY * 4+1)) 

def WyswietlMape(plansza):
    """Wyświetla mapę wartości pól na ekranie - dla testów tylko!!!"""
    print (CLS)
    print ("-" * (ROZMIAR_PLANSZY * 4+1)) 
    for rząd in plansza:
        print ("| ", end="")
        for element in rząd:
            print (str(element), end=" | ")
        print("") # nowy wiersz
        print ("-" * (ROZMIAR_PLANSZY * 4+1)) 

def WprowadzRuch (gracz):
    """Wprowadza ruch komputera lub człowieka do tablicy plansza[]"""
    if gracz == 'człowiek':
        return RuchCzlowieka()  # RuchCzlowieka() zwraca False, jeśli gracz chce
                                # wyjść wpisując 'q'
    else:
        RuchKomputera()
        return True             

def RuchCzlowieka():
    """Człowiek wybiera pole, albo qpisuje 'q' i wychodzi. Zwraca False, jeśli gracz wybrał 'q' albo True, jeśli postawił znak"""
    while True: # wieczna pętla, dopóki gracz nie wpisze czegoś sensownego
        x=None
        y=None
        while x not in range (0, ROZMIAR_PLANSZY) or y not in range (0, ROZMIAR_PLANSZY):
            x=input ("x=")
            if x == 'q':
                return False
            y=input ("y=")
            x=int(x)-1
            y=int(y)-1
        pole=(x, y)
        if plansza[y][x] == PUSTY:
            plansza[y][x]=człowiek # wstawiamy ruch do planszy
            return True             # i wychodzimy z funkcji
        else:
            print ("To pole jest zajęte!")
        # koniec pętli
    # koniec pętli

def RuchKomputera():
    """Komputer wybiera pole, na którym postawi znak"""
    # definiujemy współczynniki dla linii zawierających ileśtam znaków
    LINIAPUSTA = 1
    
    JEDENZNAK_PRO = 2
    DWAZNAKI_PRO = 8
    TRZYZNAKI_PRO = 50
    CZTERYZNAKI_PRO = 1000
    
    JEDENZNAK_KONTRA = -1
    DWAZNAKI_KONTRA = -1
    TRZYZNAKI_KONTRA = 100
    CZTERYZNAKI_KONTRA = 900
    
    
    # tworzymy pustą mapę wartości pól
    mapa=[0]*ROZMIAR_PLANSZY     # najpierw tworzymy listę z <wierszy> elementów
                                    # elementy listy mogą być dowolne
    for i in range (ROZMIAR_PLANSZY):
        mapa[i]=[0]*ROZMIAR_PLANSZY
    
    # wypełniamy wartościami
    for i in DozwoloneRuchy():
        wartosc=0
        for kierunek in ("poziom", "pion", "skos prawy", "skos lewy"):
            for j in UtworzPunktyDoSprawdzenia (i, kierunek):
                iksy, kolka = SprawdzLinie(j, kierunek)
                if komputer == X:
                    if iksy == 0 and kolka == 0: wartosc += LINIAPUSTA   
                    if iksy == 1 and kolka == 0: wartosc += JEDENZNAK_PRO  
                    if iksy == 2 and kolka == 0: wartosc += DWAZNAKI_PRO   
                    if iksy == 3 and kolka == 0: wartosc += TRZYZNAKI_PRO  
                    if iksy == 4 and kolka == 0: wartosc += CZTERYZNAKI_PRO 
                    # teraz przeszkadzamy przeciwnikowi
                    if iksy == 0 and kolka == 1: wartosc += JEDENZNAK_KONTRA
                    if iksy == 0 and kolka == 2: wartosc += DWAZNAKI_KONTRA
                    if iksy == 0 and kolka == 3: wartosc += TRZYZNAKI_KONTRA  
                    if iksy == 0 and kolka == 4: wartosc += CZTERYZNAKI_KONTRA
                if komputer == O:
                    if kolka == 0 and iksy == 0: wartosc += LINIAPUSTA
                    if kolka == 1 and iksy == 0: wartosc += JEDENZNAK_PRO
                    if kolka == 2 and iksy == 0: wartosc += DWAZNAKI_PRO
                    if kolka == 3 and iksy == 0: wartosc += TRZYZNAKI_PRO
                    if kolka == 4 and iksy == 0: wartosc += CZTERYZNAKI_PRO
                    # teraz przeszkadzamy przeciwnikowi
                    if kolka == 0 and iksy == 1: wartosc += JEDENZNAK_KONTRA
                    if kolka == 0 and iksy == 2: wartosc += DWAZNAKI_KONTRA
                    if kolka == 0 and iksy == 3: wartosc += TRZYZNAKI_KONTRA
                    if kolka == 0 and iksy == 4: wartosc += CZTERYZNAKI_KONTRA
            
        mapa[i[1]][i[0]]=wartosc
        # koniec pętli for kierunek
    # koniec pętli for i
    # WyswietlMape (mapa)
    
    # szukamy wartości maksymalnej
    maksimum=0
    for x in range (ROZMIAR_PLANSZY):
        for y in range (ROZMIAR_PLANSZY):
            if mapa[y][x] > maksimum:
                maksimum = mapa[y][x]
    # i tworzymy z pól o takiej wartości krotkę
    pola_do_ruchu = ()
    for x in range (ROZMIAR_PLANSZY):
        for y in range (ROZMIAR_PLANSZY):
            if mapa[y][x] == maksimum:
                pola_do_ruchu += ((x, y), )
    # a z tej krotki wybieramy losowo jedno pole
    ruch=random.choice (pola_do_ruchu)
    plansza[ruch[1]][ruch[0]]=komputer
    


def ZamienGracza (gracz):
    """zamienia strony gry czyli zawartość zmiennej 'gracz'"""
    if gracz == 'człowiek':
        return 'komputer'
    else:
        return 'człowiek'
        
def SprawdzLinie (pole, kierunek):
    """Sprawdza linię od pola <pole> w podanym kierunku - 'poziom', 'pion', 'skos prawy' albo 'skos lewy'
       Zwraca <None, None>, jeśli linii nie da się utworzyć, albo ilość X i O jako dwie zmienne"""
    iksy=0
    kolka=0
    if kierunek == 'poziom': #linia pozioma w prawo
        for x in range (pole[0], pole[0]+5):
            if x > ROZMIAR_PLANSZY-1:
                return None, None     #pole poza planszą
            if plansza[pole[1]][x] == X:
                iksy += 1
            if plansza[pole[1]][x] == O:
                kolka += 1
    if kierunek == 'pion': #linia pionowa w dół
        for y in range (pole[1], pole[1]+5):
            if y > ROZMIAR_PLANSZY-1:
                return None, None     #pole poza planszą
            if plansza[y][pole[0]] == X:
                iksy += 1
            if plansza[y][pole[0]] == O:
                kolka += 1
    if kierunek == 'skos prawy': #linia skośna w dół w prawo
        for xy in range (0, 5):
            x=pole[0]+xy; y=pole[1]+xy
            if x > ROZMIAR_PLANSZY-1 or y > ROZMIAR_PLANSZY-1:
                return None, None     #pole poza planszą
            if plansza[y][x] == X:
                iksy += 1
            if plansza[y][x] == O:
                kolka += 1
    if kierunek == 'skos lewy':
        for xy in range (0, 5):
            x=pole[0]-xy; y=pole[1]+xy
            if x < 0 or y > ROZMIAR_PLANSZY-1:
                return None, None
            if plansza[y][x] == X:
                iksy += 1
            if plansza[y][x] == O:
                kolka += 1
    return iksy, kolka    

def UtworzPunktyDoSprawdzenia (xy, kierunek):
    """Dla punktu <x, y> zwraca krotkę zawierającą współrzędne pól, od których utworzona linia przechodzi przez punkt <x, y>
    kierunek to 'poziom', 'skos prawy', 'skos lewy' lub 'pion'""" 
    x=xy[0]; y=xy[1]    # punkt <x, y> jest dostarczany do funkcji w postaci krotki, a tu 
                        # przeliczamy go na zmienne x i y
    punkty=()
    if kierunek == 'poziom':
        for i in range (x-4, x+1):
            if i >= 0:
                punkty += ((i, y), )    # taki dziwny zapis umożliwia dodanie krotki 
                                        # do wnętrza innej krotki
    if kierunek == "pion":
        for i in range (y-4, y+1):
            if i>=0:
                punkty += ((x, i), )
    
    if kierunek == "skos prawy":
        x=x-4
        for i in range (y-4, y+1):
            if x >= 0 and i >= 0:
                punkty += ((x, i), )
            x += 1
    
    if kierunek == "skos lewy":
        x=x+4  
        for i in range (y-4, y+1):
            if i >= 0 and x < ROZMIAR_PLANSZY:
                punkty += ((x, i), )
            x -= 1
    
    return punkty
    
def DozwoloneRuchy():
    """zwraca krotkę krotek zawierającą wszystkie dozwolone ruchy (czyli puste pola)"""
    krotka=()
    for x in range (0, ROZMIAR_PLANSZY):
        for y in range (0, ROZMIAR_PLANSZY):
            if plansza[y][x] == PUSTY:
                krotka += ((x, y), )
    return krotka



# Deklaracja stałych

CLS="\033[H\033[2J"
X='X'
O='O'
PUSTY=' '
ROZMIAR_PLANSZY=10

# Główny program zaczyna się tutaj ->

#zmienne globalne
plansza=UtworzPustaPlansze(ROZMIAR_PLANSZY) # tworzymy tablicę - planszę do gry
człowiek=None # czym gra człowiek X czy O
komputer=None # czym gra komputer
                                            
if TakLubNie("Czy chcesz mieć pierwszy ruch?"): # ustalamy, kto rusza się pierwszy
    czyj_ruch='człowiek'                             # czyli, kto gra X
    człowiek=X
    komputer=O
else:
    czyj_ruch='komputer'
    człowiek=O
    komputer=X

while not Wygrana () and not WszystkieZajete ():
    WyswietlPlansze ()
    if not WprowadzRuch (czyj_ruch): # Funkcja WprowadzRuch (ruch) zwraca False, jeśli 
        break                   # gracz wybierze 'q' zamiast współrzędnych pola.
                                # Umożliwia to 
                                # wyjście z pętli gry przed końcem
    czyj_ruch=ZamienGracza (czyj_ruch)
WyswietlPlansze()
if Wygrana():
    print("Wygrana: " + Wygrana())



    
    
    

    


