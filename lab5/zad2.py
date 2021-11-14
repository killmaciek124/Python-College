list = ["kot","alex","orange"]
partlista = []
exitlista = []
for i in range(len(list)):
    partlista.append(list[i])
    x = str(len(list[i]))
    partlista.append(x)
    exitlista.append(partlista)
print(exitlista)