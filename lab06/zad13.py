list = [2,4,6,1,2]
n = len(list)

while n > 1:
    zamien = False
    for i in range(0,len(list)-1):

        if list[i]>list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
            zamien = True

    n-=1
    print(list)
    if zamien == False: break



