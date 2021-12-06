def IsEmpty(list):
    if len(list)==0:
        return True


def tail(list):
    if IsEmpty(list)==True:
        return "Lista pusta"
    list.remove(list[0])
    return list

y = tail([1,2,3,4,5])
print(y)

