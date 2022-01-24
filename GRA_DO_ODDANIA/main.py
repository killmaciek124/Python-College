from tabulate import tabulate
from numpy import random
from time import sleep
from gamelog import gamelog_add, print_ranking

LETTER_TO_NUMBER = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
}

NUMBER_TO_LETTER = ('a', 'b', 'c', 'd')

MAX_TRIES = 3

def print_grid(secret=None):
    grid = (
        ['', '1', '2', '3', '4'],
        ['A', '', '', '', ''],
        ['B', '', '', '', ''],
        ['C', '', '', '', ''],
        ['D', '', '', '', ''],
    )

    if secret is not None:
        row = LETTER_TO_NUMBER[secret[1]] + 1
        col = int(secret[0])
        grid[row][col] = 'X'

    print(tabulate(grid, tablefmt='fancy_grid',))



def random_yx():
    x = random.randint(1, 5)
    y = random.randint(1, 5)
    return [str(x), NUMBER_TO_LETTER[y-1]]


def check_guess(column, row, num_tries, secret):
    guess = [column, row]
    if guess == secret:
        print("ZGADLES!!! TWÓJ KRZYŻYK !!!! : ")
        print("Ilość prób : ", num_tries)
        print_grid(secret)
        return True
    else:
        print("NIE ZGADłeś!!!!")
        return False


def read_yx():
    while True:
        y = input("Podaj numer kolumny: ")
        if y in ['1', '2', '3', '4']:
            break
        print("Nieprawidłowy numer kolumny!!!")
        sleep(1)
 
    while True:
        x = input("Podaj numer wiersza: ")
        if x in ['a', 'b', 'c', 'd']:
            break
        print("Nieprawidłowy numer wiersza!!!")
        sleep(1)

    return y, x



def print_hint(guess, secret):
    hints = []

    if guess[0] < secret[0]:
        hints.append('prawiej')
    elif guess[0] > secret[0]:
        hints.append('lewiej')

    if guess[1] < secret[1]:
        hints.append('niżej')
    elif guess[1] > secret[1]:
        hints.append('wyżej')

    print(' i '.join(hints).capitalize() + '.')


def main():
    print("Witaj graczu!\nMusisz znaleźć ukryty 'X' podając koordynaty pól.\n"
          "Jeśli trafisz wygrywasz, jeśli nie, dam ci podpowiedzi.\n"
          "Poniżej jest podana tabela i jej oznaczenia. Aby zgadywać, wpisz znak kolumny i wiersza,\n"
          "np. 3 i b\nPOWODZENIA!")

    player = input("Twoj nick: ")
    
    secret=None
    print_grid(secret)
    secret = random_yx()
    num_tries = 0

    while num_tries < MAX_TRIES:
        num_tries += 1
    
        y, x = read_yx()
        
        hit = check_guess(y, x, num_tries, secret)
        if hit:
            gamelog_add('gamelog.txt', player, True)
            print_ranking('gamelog.txt')
            return

        print_hint([y, x], secret)

    print("Przegrałeś: %d prób wykorzystanch" % MAX_TRIES)
    gamelog_add('gamelog.txt', player, False)
    print_ranking('gamelog.txt')



if __name__ == "__main__":
	main()
