list = [1,2,3,4,5,6,7]
def zmiana(list,liczba1,liczba2):
    list[liczba1], list[liczba2] = list[liczba2], list[liczba1]
    return list
x = zmiana(list,2,5)
print(x)

