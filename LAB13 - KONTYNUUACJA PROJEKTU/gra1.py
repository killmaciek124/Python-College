from tabulate import tabulate
from numpy import random
from time import sleep

info = [['', '1', '2', '3', '4'], ['A', '', '', '',''], ['B', '', '', '',''], ['C', '', '', '',''],
            ['D', '', '', '','']]
# WSZYSTKIE PODFUNKCJE :
def randomsign():

    x = random.randint(1,5)
    y = random.randint(1,5) # random cyfra do indeksu litery
    info[y][x] = 'X'
    # X i Y zamieniony na string
    if y == 1:
        y='a'
    elif y == 2:
        y='b'
    elif y == 3:
        y = 'c'
    elif y == 4:
        y = 'd'
    if x == 1:
        x='1'
    elif x == 2:
        x='2'
    elif x == 3:
        x = '3'
    elif x == 4:
        x = '4'
    odp=[x,y]
    return odp

def checkguess(column, row):
    guess=[column,row]
    if guess == wynik:
        print("ZGADLES!!!")
    else:
       # MIEJSCE W KTÓRYM JEST PRZYPADEK NIEZGADNIECIA KORDÓW <-------------------
        print("NIE ZGADłeś!!!!")
        howfar(guess)


def pobierzliczby():
    guesscolumn = input("Podaj numer kolumny: ")
    if (guesscolumn != '1') and (guesscolumn != '2') and (guesscolumn != '3') and (guesscolumn != '4') :
        print("Nieprawidłowy numer kolumny!!!")
        sleep(1)
        pobierzliczby()
    else:


        guessrow = input("Podaj numer wiersza: ")
        if guessrow != 'a' and guessrow != 'b' and guessrow != 'c' and guessrow != 'd':
            print("Nieprawidłowy numer wiersza!!!")
            sleep(1)
            pobierzliczby()
        else:
            return checkguess(guesscolumn, guessrow)


# FUNKCJA KTÓRA SPRAWDZA JAK DALEKO UKRYTY 'X' JEST OD ZADANEGO POLA
def howfar(guess):
    #KORDY WYNIKU:
    wynikcolumn=wynik[0]
    wynikrow=wynik[1]
   # KORDY GUESSA
    guesscolumn=guess[0]
    guessrow=guess[1]
    #====================================
    # TUTAJ ZRÓB KONSTRUKCJĘ IF KTÓRA BEDZIE MOWIC CZY WYNIKCOLUMN JEST WIEKSZY LUB MNIEJSZY OD GUESS COLUMN I ZWRACA
    #... PRINTA ZE JEST WIEKSZY LUB MNIEJSZY (ALBO BARDZIEJ W PRAWO LUB W LEWO , W DÓL LUB W GÓRE, PRAWO I W DOL ITP)
    # TO BEDZIE FUNKCJA OD CIEPLEJ ZIMNIEJ
    #======================================
    # ZROB JESZCZE JEDNA FUNKCJE KTORA BEDZIE POKAZYWAC TABELE Z 'X' JAK ZGADNIEMY POPRAWNIE KORDY












# FUNKCJA MAIN !!!!!
def main():

   # randomsign()
    print("Witaj graczu!\nMusisz znaleźć ukryty 'X' podając koordynaty pól.\n"
          "Jeśli trafisz wygrywasz, jeśli nie, powiem ci, jak daleko jest ukryty znak.\n"
          "Poniżej jest podana tabela i jej oznaczenia. Aby zgadywać, wpisz znak kolumny i wiersza,\n"
          "np. b i 3\nPOWODZENIA!")


    global wynik
    wynik=(randomsign()) # W ZMIENNEJ WYNIK MAMY KOORDYNATY X

    print("Wynik :", wynik)

    print(tabulate(info, tablefmt='fancy_grid',))
    pobierzliczby()



main()
