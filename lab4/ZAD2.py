word = "slowo"
samogloski = 0
for i in range(len(word)):
    if (word[i] ==  "a" or "e" or "ę" or "ą" or "i"):
        samogloski = samogloski + 1
        print(samogloski)
print(samogloski)

# DO POPRAWY 