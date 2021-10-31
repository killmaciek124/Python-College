lista1=[-1, 2,  3, 6]
OldList = list(lista1)
currentnum = 0
bignum = lista1[0]
x = 0
for i in range(len(lista1)-1):
    currentnum = lista1[i+1]
    if bignum < currentnum:
        bignum = currentnum

lista1.remove(bignum)
for i in range(len(lista1)-1):
    bignum=lista1[0]
    currentnum = lista1[i+1]
    if bignum < currentnum:
        bignum = currentnum
        x = OldList.index(bignum)

print("Element z listy index: ", x, "i ten numer: ", bignum)
