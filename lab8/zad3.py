wynik = 0
k = 1
def sum(n):
    global wynik, k
    if n == 0:
        return wynik
    else:
        wynik += 1/k
        k +=1
        n -=1
        return sum(n)

y = sum(4)
print(y)


