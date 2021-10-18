w=30
p=2
x=1

while (w > 0):
    if (w%2 == 0):
        w=w//2
        p=p*p
    else:
        w=w-1
        x=x*p
    if (w == 0):
        print(w,p,x)