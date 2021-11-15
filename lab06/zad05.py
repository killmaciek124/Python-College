def Reversator(slowo):
    NoweSlowo = ""
    for i in range(len(slowo)):
        x = (len(slowo)-1)-i
        NoweSlowo += slowo[x]
    return NoweSlowo

print(Reversator("dupa123"))



