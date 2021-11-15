bigliczba=0
def choosing(liczba1, liczba2):
    if liczba1 > liczba2:
        print("%d jest większa od liczby %d" % (liczba1,liczba2))
        bigliczba = liczba1
    elif liczba1==liczba2:
        print("LICZBY SA ROWNE")
        bigliczba = liczba1
    else:
        print("%d jest mniejsza od liczby %d" % (liczba1,liczba2))
        bigliczba=liczba2
    return bigliczba

x = choosing(5,10)
choosing(x,8)

