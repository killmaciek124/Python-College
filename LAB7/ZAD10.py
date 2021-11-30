def bubblesort(list):
    n = len(list)
    while n > 1:
        zamien = False
        x = 0
        while x < len(list)-1:
            if list[x] > list[x+1]:
                list[x], list[x+1] = list[x+1], list[x]
                zamien = True
            x +=1
        if zamien == False: break
        n -=1
        print(list)
    return list


y = bubblesort([5,4,1212,4,1,3,5,7,9,1,5555,2,1])
print(y)

