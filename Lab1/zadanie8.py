a = 3
b = 100
c = 100
if (a>b) & (b>c):
    print(a,b,c)
elif (b>a) & (a>c):
    print(b, c, a)
elif (c>b) & (b>a):
    print(c,b,a)
elif (b>c) & (c>a):
    print(b,c,a)
else:
    print("=")