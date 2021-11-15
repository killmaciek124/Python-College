list = [1,2,3,4,5, 5.6, 6, 8.25,10]

def PrintEven(list):
    for i in range(len(list)):
        if list[i]%2==0:
            print(list[i])

PrintEven(list)
