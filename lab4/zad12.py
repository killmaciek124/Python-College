word = "rabarbar"
wzorzec = "ra"
n = 0
print(word[0:2])
box = ""
i = 0
while 0 < len(word)-i:



    box.append(word[i])
    if len(box) == len(wzorzec) and box == word[n:i+1]:
        print("Jest wzorzec")
        n+=1
        i+=1
    elif len(box) == len(wzorzec):
        n+=1
        box = ""
        i+=1
    else:
        n+=1
        i+=1




