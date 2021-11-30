from numpy import random

def losowe(list, n):
    while n > 0:
        list.append(random.randint(1000))
        n -= 1
    return list
x = losowe([],4)
print(x)