dzielnik = 1
wynik = 1
def NWD(a,b):
    global dzielnik, wynik
    if (dzielnik >abs(a)) or (dzielnik >abs(b)):
        return wynik
    elif (a%dzielnik==0) and (b%dzielnik==0):
        wynik = dzielnik
        dzielnik +=1
        return NWD(a,b)
    else:
        dzielnik +=1
        return NWD(a,b)

y = NWD(100,-20)
print(y)

