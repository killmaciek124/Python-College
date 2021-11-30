# zakładamy wewnątrz funkcji że rozpatrujemy..
#.. funkcję w przedziale [0,3] , oraz omawiamy tutaj funkcję 3 stopnia
import sys
import numpy
def check(a,b,c,d):
    epsilon = sys.float_info.epsilon
    A = 0 #początek przedziału
    B=3 # KONIEC PRZEDZIALU
    #najpierw sprawdzamy ciągłość:
    if a*3*3*3+b*3*3+c*3+d>0:
        print("Funkcja jest ciągła.")
    else:
        return "Funkcja nie jest ciągła"
    # algorytm :
    if a*1.5*1.5*1.5+b*1.5*1.5+c*1.5+d ==0:
        return 1.5
    while abs(A - B) > epsilon:  # dopóki nie uzyskamy zadanej dokładności
        x1 = (A + B) / 2

        if abs(a*x1*x1*x1+b*x1*x1+c*x1+d) <= epsilon:  # jeżeli znaleźliśmy miejsce zerowe mniejsze bądź równe przybliżeniu zera
            break
        elif (a*x1*x1*x1+b*x1*x1+c*x1+d) * a*A*A*A+b*A*A+c*A+d < 0:
            B = x1  # nadpisywanie prawego krańca przedziału
        else:
            A = x1  # nadpisywanie lewego krańca przedziału

    return (A + B) / 2  # zwracanie znalezionego miejsca zerowego
y = check(1,-2,1,-7)
print("Result: ", y)