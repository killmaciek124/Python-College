

def zmiana(lata):
    dni = lata*365
    godziny = dni*24
    minuty = godziny*60

    return minuty

x = zmiana(1)

print("Liczba minut : ", x)