def ispermutation(list1,list2):
    list1.sort()
    list2.sort()
    if list1==list2:
        return True
    else:
        return False

y = ispermutation([1,2,3,3,4,5],[3,3,4,5,1,2])
print(y)