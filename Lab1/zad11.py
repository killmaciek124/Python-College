x = 890

jednosci = x%10
dziesiatki = (x%100) - jednosci
setki = (x%1000) - dziesiatki - jednosci

print("Cyfra jedności : ", jednosci)
print("Cyfra dziesiątek : ", int(dziesiatki/10))
print("Cyfra setek: ", int(setki/100))