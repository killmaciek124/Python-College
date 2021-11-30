def max(list, x):
    n = 0
    while n < len(list):
        if list[n] == x:
            afterlist= list[n:]
            newlist = list[:n]
            newlist.sort()
            return newlist + afterlist
        n +=1

y = max([5,4,1,2,10,5,4,3,2,1,0], 10)
print(y)