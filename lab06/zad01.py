def choosing(liczba1, liczba2):
    if liczba1 > liczba2:
        print("%d jest większa od liczby %d" % (liczba1,liczba2))
    elif liczba1==liczba2:
        print("LICZBY SA ROWNE")
    else:
        print("%d jest mniejsza od liczby %d" % (liczba1,liczba2))
    return

choosing(600,600)