import util

name = input("Ditt navn: ")
age = util.get_int("Din alder: ")
city = input("Ditt bosted: ")

print(f"Navn: {name}, Alder: {age}, Bosted: {city}")
print(f"Du er {age + 5} år gammel om 5 år")