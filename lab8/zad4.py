wynik = 0
def mnozenie(n):
    global wynik
    if n == 0:
        return 0
    elif wynik/n==abs(n):
        return abs(wynik)
    else:
        wynik += n
        return mnozenie(n)

y = mnozenie(-3)
print(y)