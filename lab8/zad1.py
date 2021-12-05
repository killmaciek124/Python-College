wynik = 1
def silnia(x):
    global wynik
    if x < 0:
        return "Error"
    elif x == 0:
        return wynik
    else:
        wynik *= x
        return silnia(x-1)


y = silnia(-1)
print(y)
