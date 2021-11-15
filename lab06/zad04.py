def ProductOfList(lista):
    suma = 1
    for i in range(len(lista)):
        suma *= lista[i]
    return suma
list1 = [2.5, -2,5]
x = ProductOfList(list1)
print(x)