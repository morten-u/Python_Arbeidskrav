import util

def addisjon(n1: float, n2: float) -> float:
    return n1 + n2

def subtraksjon(n1: float, n2: float) -> float:
    return n1 - n2

def multiplikasjon(n1: float, n2: float) -> float:
    return n1 * n2

def divisjon(n1: float, n2: float) -> float:
    return n1 / n2

numb1 = util.get_float("Skriv inn første tall: ")
numb2 = util.get_float("Skriv inn andre tall: ")

options = [
    "Addisjon",
    "Subtraksjon",
    "Multiplikasjon",
    "Divisjon"
]

choice = util.menu(options)

res = 0

if choice == 0:
    print(f"{numb1} + {numb2} = {addisjon(numb1, numb2)}")
elif choice == 1:
    print(f"{numb1} - {numb2} = {subtraksjon(numb1, numb2)}")
elif choice == 2:
    print(f"{numb1} * {numb2} = {multiplikasjon(numb1, numb2)}")
elif choice == 3:
    res = 0
    try:
        res = divisjon(numb1, numb2)
        print(f"{numb1} / {numb2} = {res}")
    except ZeroDivisionError:
        print("Kan ikke dele på null")
