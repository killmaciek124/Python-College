x=1
y=2
n=0

while n < 10:
    x=x+y
    y=x+x
    n=n+1

    if n == 10:
        print(x,y,n)