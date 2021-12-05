i = 0
def sort(x, list):
    global i
    if x == list[i]:
        return "TAK"
    elif i == len(list)-1:
        return "NIE"
    else:
        i+=1
        return sort(x,list)

y = sort(5,[1,2,3,4,6])
print(y)

