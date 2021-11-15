import copy

m = 3
n = 4
WholeList = []
for j in range(0,n):
    list = []
    WholeList.append(list)

    for i in range(0,m):
        list.append(5*i)

    newlist = list.copy()
    list.reverse()
print(WholeList)

