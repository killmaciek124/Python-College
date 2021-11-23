x = 5

def binarysearch(list,liczba):
    print(list[int(len(list)/2)])
    print(list)
    if liczba == list[int(len(list)/2)] or liczba == list[int(len(list)/2)-1]:
        return True
    elif len(list) == 1:
        return False
    elif liczba > list[int(len(list)/2)]:
        newlist = list[int(len(list)/2):]
        return binarysearch(newlist,x)
    elif liczba < list[int(len(list) / 2)]:
        newlist = list[:int(len(list)/2)]
        return binarysearch(newlist, x)

    else:
        return False





y = binarysearch([1,2,3,4,5,6],x)
print(y)