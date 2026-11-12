import util

score = 0

while True:

    score = util.get_float("Skriv inn din poengsum: ")

    if score < 0 or score > 100:
        print("Poengsum må være mellom 0 - 100")
        continue

    break


if score >= 90:
    print("Karakter A")
elif score >= 80:
    print("Karakter B")
elif score >= 70:
    print("Karakter C")
elif score >= 60:
    print("Karakter D")
elif score >= 50:
    print("Karakter E")
else:
    print("Karakter F")
