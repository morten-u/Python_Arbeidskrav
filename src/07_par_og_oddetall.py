import util

numb: int = 0

while True:

    numb = util.getInt("Skriv inn ett positivt heltall: ")

    if numb < 0:
        print("Tallet må være positivt.")
        continue

    break
    
count = 0
total = 0
for i in range(1, numb):

    if i % 2 == 0:
        count += 1
        total += i
        
print(f"Antall partall: {count}")
print(f"summen av disse = {total}")