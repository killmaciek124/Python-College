wynik = 1
licznik = 0
def potegowanie(a,b):
    global licznik, wynik
    if licznik == b:
        return wynik
    else:
        wynik *= a
        licznik +=1
        return potegowanie(a,b)

y = potegowanie(-2,3)
print(y)
