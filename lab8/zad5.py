start = 0
counter = 0
parzysta = 2
def sum(n):
    global start, counter, parzysta
    if parzysta == n:
        return start
    elif parzysta == n-1:
        return start
    elif n < 1:
        return "Error"
    else:
        counter +=1
        parzysta = counter*2
        start += parzysta
        print(start, counter)


        return sum(n)

y = sum(12)
print(y)