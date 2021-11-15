def checking(lista, liczba):
    licznik = len(lista)
    for i in range(len(lista)):
        if lista[i] == liczba:
            print("Jest liczba na liście!")
        elif licznik == 1:
            print("Nie ma liczby na liście!")
        else:
            licznik -= 1

list1 = [1,2,3,4,5,6]

num1 = 6

checking(list1,num1)