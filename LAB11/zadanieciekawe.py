def rozloz(n):
    czynniki = []
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            czynniki.append(k)
        k += 1
    
    return czynniki
y=(rozloz(15))
print(y)