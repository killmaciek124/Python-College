n = 6

print("Rozmiar :", n)
for i in range(0,n+1):
    print(int(n-i/2)*" ", end="")
    print(i*" *")
    print(int(n-i/2)*" ", end="")

print("       |___|    ")