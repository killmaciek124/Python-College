list = [1,2,3 ]
list2 = [23,23]
licznik = 0

for i in range(len(list)):
    for j in range(len(list2)):
        if list[i]== list2[j]:
           licznik += 1


if licznik > 0:
    print("TAK")
else:
    print("NIE")