WholeList = []
list1 =  [1,2,3]
list2 = [1,1,1,1,1,20]
list3 = [5,4,600]

WholeList.append(list2)
WholeList.append(list3)
WholeList.append(list1)
BigSum = 0
Sum = 0
for i in range(len(WholeList)):
    for j in range(len(WholeList[i])):
        Sum += (WholeList[i])[j]


    if Sum > BigSum:
        BigSum = Sum

        Sum = 0
print("najwieksza suma:", BigSum)

#NAJMNIEJSZA SUMA W LISCIE :
SmallSum=0
for j in range(len(WholeList[0])):
    SmallSum += (WholeList[0])[j]



for i in range(len(WholeList)):
    Sum = 0
    for j in range(len(WholeList[i])):
        Sum += (WholeList[i])[j]

    if Sum < SmallSum:
        SmallSum = Sum


print("najmniejsza suma:", SmallSum)

