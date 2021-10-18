a = 1
b = 0
n = 0

while n < 1000:
    b = b + a
    a = a + 2
    n = n + 1
    if n == 1000:
        print("a : ",a, "b:",b, "n:", n)