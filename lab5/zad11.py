list = [2,3,4,5,60]
bignum = list[0]

for i in range(len(list)):
    if list[i] > bignum:
        bignum = list[i]


list.remove(bignum)
bignum = list[0]
for i in range(len(list)):
    if list[i] > bignum:
        bignum = list[i]

print(bignum)
