def check(list, x):
    n = len(list)-1
    while n >= 0:
        print(n,x,list)
        if list[n] == x:
            return n
        else:
            n-=1

y = check([1,2,3,4,5,6,7,8], 4)
print("Index:",y)