from numpy import random

def losowe(list, n):
    n -= 1
    pomoc = 0
    while n > 0:
        x = random.randint(1000)
        if len(list) == 0:
            list.append(x)
        elif list[pomoc] < x:
            list.append(x)
            if pomoc < n:
                pomoc +=1
            n -= 1
    return list

x = losowe([], 3)
print(x)