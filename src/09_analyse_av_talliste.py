
numbers = [
    20,
    45,
    0,
    -25,
    99,
    45,
    0,
    -33,
    8,
    4,
    -12
]

neg = 0
pos = 0
zero = 0
total = 0
avg = 0

for numb in numbers:
    if numb > 0:
        pos += 1
    elif numb < 0:
        neg += 1
    else:
        zero += 1

    total += numb

avg = total / len(numbers)

print(f"Positive verdier    : {pos}")
print(f"Negative verdier    : {neg}")
print(f"Nullverdier verdier : {zero}")
print(f"Summen              : {total}")
print(f"Gjennomsnittet      : {avg}")

