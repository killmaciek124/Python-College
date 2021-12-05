wynik = 0
licznik = 0
def sum(n):
    global wynik,licznik
    n = str(n)
    if licznik == len(n):
        return wynik
    else:
        number = 0
        number = int(n[licznik])
        wynik += number
        licznik+=1
        return sum(n)


y = sum(1030)
print(y)
