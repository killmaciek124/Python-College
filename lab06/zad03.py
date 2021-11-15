def SumOfList(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma
list1 = [1.5, 1.5, 3.45]
x = SumOfList(list1)
print(x)
