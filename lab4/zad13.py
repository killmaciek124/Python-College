word = "tattarrattat"
ReversedWord = ""
length = len(word)-1
for i in range(len(word)):
    ReversedWord+=word[length-i]

if word==ReversedWord:
    print("TO JEST PALINDROM")
else:
    print("TOo nie jest palindornme")