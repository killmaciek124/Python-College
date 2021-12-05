firstN = 0
secondN = 1
counter = 2
def fib(x):
    global firstN, secondN, counter
    if x==1:
        return 0
    elif x ==2:
        return 1
    elif counter == x:
        return secondN
    else:
        counter +=1
        firstN, secondN = secondN, (firstN + secondN)
        return fib(x)

z = fib(3)
print(z)





