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
    return False # na razie zwraca po prostu False
    
def WszystkieZajete():
    """zwraca True, jeśli wszystkie pola są zajęte, a False, jeśli jest choć jedno wolne"""
    for i in plansza:
        if PUSTY in i:
            return False
    return True
        
    #for x in range (ROZMIAR_PLANSZY):
    #    for y in range (ROZMIAR_PLANSZY):
    #        if plansza[x][y] == PUSTY:
    #            return False
    #return True
    
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
        while x not in range (0, ROZMIAR_PLANSZY-1) or y not in range (0, ROZMIAR_PLANSZY-1):
            x=input ("x=")
            if x == 'q':
                return False
            y=input ("y=")
            x=int(x)-1
            y=int(y)-1
        pole=(x, y)
        if plansza[x][y] == PUSTY:
            plansza[x][y]=człowiek # wstawiamy ruch do planszy
            return True             # i wychodzimy z funkcji
        else:
            print ("To pole jest zajęte!")
        # koniec pętli
    # koniec pętli

def RuchKomputera():
    """Komputer wybiara pole, na którym postawi znak"""
    # na razie wybór będzie absolutnie losowy
    x=random.randint (0, ROZMIAR_PLANSZY)
    y=random.randint (0, ROZMIAR_PLANSZY)
    plansza[x][y]=komputer
    


def ZamienGracza (gracz):
    """zamienia strony gry czyli zawartość zmiennej 'gracz'"""
    if gracz == 'człowiek':
        return 'komputer'
    else:
        return 'człowiek'
        




# Deklaracja stałych

CLS='\033[H\033[2J'
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
    

    
    
    

    


