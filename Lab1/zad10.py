a = 1
b = 21
c = 1

import math


delta = (b*b) - (4*a*c)
if delta==0:
    x0 = (-b)/(2*a)
    print("Funkcja ma jedno miejsce zerowe: ", x0)
elif delta >0:
    x1 = (-b-math.sqrt(delta))/(2*a)
    x2 = (-b+math.sqrt(delta))/(2*a)
    print("Funkcja ma dwa miejsca zerowe: " ,round(x1,2) ,"i" ,round(x2,2))
else:
    print("Delta mniesza od zera - brak rozwiązań")