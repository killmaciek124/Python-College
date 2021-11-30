def check(list, x):
    ListOfX = []
    ListofBigger = []
    ListofSmaller = []
    n = len(list)-1
    while n >= 0:
        if list[n] == x:
            ListOfX.append(list[n])
        elif list[n] < x:
            ListofSmaller.append(list[n])
        else:
            ListofBigger.append(list[n])
        n -=1
    return len(ListOfX), len(ListofSmaller), len(ListofBigger)
y = check([1,2,3,4,4,4,5,1,3], 4)
print("Result: ", y)