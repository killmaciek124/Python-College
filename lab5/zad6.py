WholeList = [[1,2,4,6],[2,3,4,5],[12,3,4,5]]
x = 3

for i in range(len(WholeList)):
       for j in range(len(WholeList[i])):
              WholeList[i][j] *= x
print(WholeList)