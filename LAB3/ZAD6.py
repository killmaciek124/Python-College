n = 12
const = n
licznik = 0
while (n > 0):
    if (const%n == 0):
        licznik = licznik + 1
        n = n - 1
    else:
        n = n - 1

print("Ilosc dzielnikow: ", licznik)