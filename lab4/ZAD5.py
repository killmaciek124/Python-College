lista1=[-10, 100,-20,3]
currentnum = 0
bignum = lista1[0]
for i in range(len(lista1)-1):
    currentnum = lista1[i+1]
    if currentnum > bignum:
        bignum = currentnum


print(bignum)