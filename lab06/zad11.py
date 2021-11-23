def czyWLiscie(lista,x):
    for i in range (0,len(lista)):
        if x==lista[i]:
            return True
    return False

def czyPangram (list):
    alfabet=[]
    for i in range (97,97+26):
        alfabet.append(chr(i))
    pomoc=[]
    for i in range (0,len(list)):
        if czyWLiscie(alfabet,list[i]):
            if not czyWLiscie(pomoc,list[i]):
                pomoc.append(list[i])
    pomoc.sort()
    return alfabet==pomoc




lista="the quick brown fox jumps over a lazy dog."
print(czyPangram(lista))

