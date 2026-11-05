
# Det enkleste her hadde vært en egen input for fornavn og etternavn
# Men usikker på om det var tillat så gjennomfører det slik som her


full_name = input("Skriv inn ditt fulle navn: ")

print(f"Fult navn: {full_name}")
print(f"Store bokstaver: {full_name.upper()}")


# Bruker loop over len(), da jeg ikke vet hvor mange navn brukeren skriver inn
# Eksempel: Ole Eriksen eller Ole Christian Eriksen
char_count = 0
for c in full_name:
    if c == " ":
        continue
    char_count += 1


print(f"Antall bokstaver i navn: {char_count}")

print(f"{full_name[:3]}")