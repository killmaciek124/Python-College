for i in range(2,800):
    p=i
    k=0
    for j in range(2,p-1):
        if(p%j==0):
            k=k+1
    if(k==0):
        print(p)