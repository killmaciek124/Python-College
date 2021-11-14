from numpy import random
x = random.randint(10)

list = []
liczba = 10
for i in range(0, x):
    list.append(random.randint(10)*i)
for i in range(len(list)):
    if list[i] == liczba:
        print("TAK!!!!")
print(list)

