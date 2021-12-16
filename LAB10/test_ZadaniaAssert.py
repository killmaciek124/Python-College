def occur(list,x):
    list.sort()
    for i in range(len(list)):
        if list[i] == x:
            return True

    return False

def najwiekszy_element(list):
    listmax = 0
    for i in range(len(list)):
        if list[i] > listmax:
            listmax = list[i]

    return listmax

def sortowanie_przez_wybor(list,max):
    for i in range(len(list)):
        list[i], najwiekszy_element(list) = najwiekszy_element(list) , list[i]



def test_occur():
    assert occur([1,2,3,4,5],1)

print(sortowanie_przez_wybor([4,3,2,1,59,4]))