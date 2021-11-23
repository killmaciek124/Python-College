def czyjest(lista,x):
    for i in range (0,len(lista)):
        if lista[i]==x:
            return True
    return False


def bezduplikatow (lista):
    wynik=[]
    for i in range (0,len(lista)):
        if czyjest(wynik,lista[i])==0:
            wynik.append(lista[i])
    return wynik

lista=[1,2,3,4,1]
x=2
print(bezduplikatow(lista))