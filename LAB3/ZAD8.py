n = 5
suma = 0
m = 0

while (suma < n):
    m = m + 1
    suma = suma + m

    # print(m, suma)
    if (suma > n):
        print((m-1), (suma-m))
    elif (suma==n):
        print(m, suma)