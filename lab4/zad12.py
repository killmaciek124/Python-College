slowo="rabarbar"
wzorzec="ab"
help=0
for i in range (0,len(slowo)):
    if slowo[i:len(wzorzec)+i]==wzorzec:
        help=1
if help==1:
    print("tak")



