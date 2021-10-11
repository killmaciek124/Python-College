a = 123
suma = 0
while (a > 0):
    suma += a % 10
    a = int(a / 10)

print(suma)