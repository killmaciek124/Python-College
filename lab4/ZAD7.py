lista1=[-1, 2,  3 ,4]
y = lista1
currentnum = 0
bignum = lista1[0]
x = 0
for i in range(len(lista1)-1):
    currentnum = lista1[i+1]
    if bignum > currentnum:
        bignum = currentnum
        x = lista1.index(bignum)


lista1 = lista1[0:x]+ lista1[x+1:]

for i in range(len(lista1) - 1):
    bignum=lista1[0]
    currentnum = lista1[i+1]
    if bignum < currentnum:
        bignum = currentnum
        x = lista1.index(bignum)

print("Element z listy index: ", x, "i ten numer: ", bignum)

#DOKONCZ W DOMU!!!!!!!