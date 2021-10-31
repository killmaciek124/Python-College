x = 111
y= str(111)
ListSetki = ["sto", "dwiescie","dziewiecset",  "trzysta", "czterysta", "piecset", "szescset", "siedemset", "osiemset", "dziewiecset"]
ListDziesiatki = ["dziesiec", "dwadziescia", "trzydziesci", "czterdziesci", "piecdziesiat", "szescdziesiat","siedemdziesiat",
                  "osiemdziesiat", "dziewiecdziesiat"]
ListaNastki = ["jedenascie", "dwanascie", "trzynascie", "czternascie", "pietnascie", "szesnascie"
               , "siedemnascie", "osiemnascie", "dziewietnascie"]
ListaJednosci = ["jeden", "dwa", "trzy", "cztery", "piec", "szesc", "siedem", "oseim"
    , "dziewiec"]
ODP = []
if x < 1000 and x > 0:
    for i in range(len(y)+1):
        if i == 1:
             ODP.append(ListSetki[10-int(y[i])]

        elif i == 2:
            ODP.append(ListaNastki[10-int(y[i])]
            break
        elif i == 2 and y[i]!=1:
            ODP.append(ListDziesiatki[10-int(y[i])]
        elif i == 3:
            ODP.append(ListaJednosci[10-i])

print(ODP)
