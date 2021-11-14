#napisz program ktory z listy list wybierze liste o najmniejszej
# i najwiekszej sumie xd laura jest glupia i patrzy mi w monitor
WholeList = []
list1 =  [1,2,3,4,100]
list2 = [1,1,1,1,1,20]
list3 = [5,4,6]

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
SmallSum= 0
for i in range(len(WholeList)):
    Sum = 0
    for j in range(len(WholeList[i])):
        Sum += (WholeList[i])[j]
    print(Sum)
# do tego momentu jest dobrze !!!!
    if Sum < BigSum:
        SmallSum = Sum
        if Sum < SmallSum:
            SmallSum = Sum

print("najmniejsza suma:", SmallSum)
