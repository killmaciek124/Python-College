def replace(d,v,e):
    for key in d.keys():
        if d[key] == v:
            d[key] = e

slownik = {"Kot":2,"Pies":2,"Świnia":3}
print(slownik)
replace(slownik,2,3)

print(slownik)