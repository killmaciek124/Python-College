def check(list, x):
    n = len(list)-1
    while n >= 0:
        print(n,x,list)
        if list[n] == x:
            return n
        else:
            n-=1

y = check([4,1,3,2,5,6], 4)
print("Index:",y)


