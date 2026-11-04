import util

numb1 = util.getFloat("Skriv inn første tall: ")
numb2 = util.getFloat("Skriv inn andre tall: ")

print(f"Summen:      {numb1 + numb2}")
print(f"Differansen: {numb1 - numb2}")
print(f"Produktet:   {numb1 * numb2}")

if numb2 == 0:
    print("Kan ikke dele på 0")
else:
    print(f"Divisjon:    {numb1 / numb2}")