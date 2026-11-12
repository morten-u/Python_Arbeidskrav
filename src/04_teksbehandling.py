
fname = input("Fornavn: ")
lname = input("Etternavn: ")

full_name = f"{fname} {lname}"

print(f"Fullt navn: {full_name}")
print(f"Store bokstaver: {full_name.upper()}")

# Bruker loop over len(), da jeg ikke vet hvor mange navn brukeren skriver inn
# Eksempel: Ole Eriksen eller Ole Christian Eriksen
char_count = 0
for c in full_name:
    if c == " ":
        continue
    char_count += 1

print(f"Antall bokstaver i navn: {char_count}")

print(f"Tre første bokstaver i fornavn: {fname[:3]}")