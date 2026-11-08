import util

class Bankkonto:
    def __init__(self, eier: str, saldo: float) -> None:
        self.eier = eier
        self.saldo = saldo

    def sett_inn(self, belop: float):
        if belop < 0:
            print("Error: beløp kan ikke være negativt")
            return

        self.saldo += belop
        print()
        print(f"Beløp lagt til: {belop}\nNy saldo: {self.saldo}")

    def ta_ut(self, belop: float):
        if belop > self.saldo:
            print(f"Error: kan ikke ta ut mer enn {self.saldo}")
            return

        self.saldo -= belop
        print()
        print(f"Tatt ut {belop}\nNy saldo: {self.saldo}")

    def vis_saldo(self):
        print()
        print(f"Eier : {self.eier}")
        print(f"Saldo: {self.saldo}")

options = [
    "Sett inn penger",
    "Ta ut penger",
    "Vis saldo",
    "Avslutt"
]

name = input("Navn: ")
account = Bankkonto(name, 1000)

while True:

    util.clear()
    print(f"--- KONTO {account.eier} ---")
    choice = util.menu(options)

    if options[choice] == "Sett inn penger":
        amount = util.getFloat("Beløp: ")
        account.sett_inn(amount)
        input("Press enter for å fortsette")
        continue
    elif options[choice] == "Ta ut penger":
        amount = util.getFloat("Beløp: ")
        account.ta_ut(amount)
        input("Press enter for å fortsette")
        continue
    elif options[choice] == "Vis saldo":
        account.vis_saldo()
        input("Press enter for å fortsette")
        continue
    elif options[choice] == "Avslutt":
        break