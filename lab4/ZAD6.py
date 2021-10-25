lista1=[-1000, -100, 100,0 ,-300000]
currentnum = 0
bignum = lista1[0]
x = 0
for i in range(len(lista1)-1):
    currentnum = lista1[i+1]
    if bignum > currentnum:
        bignum = currentnum
        x = lista1.index(bignum)

print("Element z listy index: ", x, "i ten numer: ", bignum)