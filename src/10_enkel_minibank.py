import util

options = [
    "Vis saldo",
    "Sett inn penger",
    "Ta ut penger",
    "Avslutt"
]

balance: float = 1000

def showBalance():
    util.clear()
    print("--- VIS SALDO ---")
    print(f"Saldo: {balance}")
    input("Press enter for å returnere")

def addToBalance():
    global balance
    util.clear()
    print("--- SETT INN PENGER ---")

    while True:
        add = util.getFloat("Sum: ")

        if add < 0:
            print("Sum kan ikke være negativ.")
            continue

        balance += add
        break

def withdrawFromBalance():
    global balance
    util.clear()
    print("--- TA UT PENGER ---")

    while True:
        sub = util.getFloat("Sum: ")
        if sub > balance:
            print(f"Kan ikke ta ut mer en {balance}")
            continue
        elif sub < 0:
            print("Kan ikke ta ut negativt beløp")
            continue

        balance -= sub
        break

while True:

    util.clear()
    print("--- MINIBANK ---")
    choice = util.menu(options)
    match choice:
        case 0: # Vis saldo
            showBalance()
        case 1: # Sett inn penger
            addToBalance()
        case 2: # Ta ut penger
            withdrawFromBalance()
        case 3: # Avslutt
            break