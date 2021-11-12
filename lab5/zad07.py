x = 1

list = []
revlist = []
for i in range(x, x+20):
    list.append(i)

for i in range(0,len(list)):
    revlist.append(len(list)-i)

wynik = []

wynik.append(list)
wynik.append(revlist)

print(wynik)