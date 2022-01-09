from tabulate import tabulate
from numpy import random
from time import sleep

info = [['', '1', '2', '3', '4'], ['A', '', '', '',''], ['B', '', '', '',''], ['C', '', '', '',''],
            ['D', '', '', '','']]
# WSZYSTKIE PODFUNKCJE :
def randomsign():

    x = random.randint(1,5)
    y = random.randint(1,5) # random cyfra do indeksu litery
    info[x][y] = 'X'

#def checkguess(column, row):







# FUNKCJA MAIN !!!!!
def main():

    randomsign()
    print("Witaj graczu!\nMusisz znaleźć ukryty 'X' podając koordynaty pól.\n"
          "Jeśli trafisz wygrywasz, jeśli nie, powiem ci, jak daleko jest ukryty znak.\n"
          "Poniżej jest podana tabela i jej oznaczenia. Aby zgadywać, wpisz znak kolumny i wiersza,\n"
          "np. b3\nPOWODZENIA!")
    print(tabulate(info, tablefmt='fancy_grid',))
    guesscolumn = input("Podaj numer kolumny: ")
    guessrow = input("Podaj numer wiersza: ")

main()
