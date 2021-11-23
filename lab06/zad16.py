def triangle(int1,int2,int3):
    if helper(int1, int2, int3) == False:
        return 0
    list = []
    list.append(int2)
    list.append(int3)
    list.append(int1)
    list.sort()
    if list[0]+list[1]>list[2]:
        return 1
    else:
        return 0


def helper(int1,int2,int3):
    if int1 <=0 or int2 <= 0 or int3 <= 0:
        print("podana liczba musi być większa od 0!!!")
        return False



x = triangle(3,2,3)
print(x)