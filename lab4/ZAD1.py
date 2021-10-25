napis="alad ma kotA"
print(napis[0])
print(napis[2])
print(napis[1:3])
print(napis[1::3]) #np od indeksu 1 (drugi wyraz) do końca (bo pusta jest druga wartość, i printujemy co 3 wyrazy ( trzecia wartosc)
print(napis[::]) # printuje wszystko
print(len(napis))
print(napis.lower())
print(napis.count(" ")) # ile jest spacji w zdaniu (lub innego znaku wpisanego)

lista1=[1,2,3,4,5,6]
lista2=[1,3,4,5,9]
print(lista1,lista2)
lista3=[lista1,lista2]
lista4=lista1+lista2
print(lista3)
print(lista4)

lista1=[1,2,3,4,5,6] #iteracja po elementach listy po kolei
for i in lista1:
    print(i)

list = [1, 2, 3, 4]
x = list[0:1]+ list[3::1]
print(x)
