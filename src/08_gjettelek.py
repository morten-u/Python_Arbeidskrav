import util
import random

secret_number = random.randrange(1, 100)

guess = util.getInt("Gjett hemmelig tall: ")

attempts = 1
while guess != secret_number:
    attempts += 1

    if guess < secret_number:
        guess = util.getInt("For lavt. Gjett igjenn: ")
    else:
        guess = util.getInt("For høyt. Gjett igjenn: ")

print("Riktig!")
print(f"Du brukte {attempts} forsøk.")