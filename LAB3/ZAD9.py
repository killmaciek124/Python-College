a=11110
help=0
wynik=0
b=1
while a>0:
    help=a%10
    a=a//10
    wynik=wynik+help*b
    b=b*2 #Ciekawy sposób na potęgi bez potęg
print(wynik)