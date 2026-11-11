import util

class Produkt:
    def __init__(self, navn: str, pris: float, antall: int) -> None:
        self.navn = navn
        self.pris = pris
        self.antall = antall

    def selg(self, antall: int) -> float:

        if antall > self.antall:
            print(f"Kan ikke selge mer enn {self.antall} stk")
            return 0


        self.antall -= antall
        return self.pris * antall

    def fyll_paa(self, antall: int):
        if antall < 0:
            print("antall må være positivt tall")
            return

        self.antall += antall

    def vis_info(self):
        print(f"Navn: {self.navn}\nPris: {self.pris}\nAntall: {self.antall}")

    def verdi(self) -> float:
        return self.pris * self.antall

produkter = [
    Produkt("Melk", 22, 5),
    Produkt("Pølser", 45, 10),
    Produkt("Brød", 39.90, 15),
    Produkt("Kjøttdeig", 75.50, 8)
]

def beregn_lagerverdi(produkter: list[Produkt]) -> float:
    total: float = 0
    for produkt in produkter:
        total += produkt.verdi()

    return total


options = [
    "Vis produkter",
    "Selg produkt",
    "Fyll på lager",
    "Beregn lagerverdi",
    "Avslutt"
]

def show_products():
    global produkter

    util.clear()
    print("--- VIS PRODUKTER ---")
    for p in produkter:
        p.vis_info()
        print("---")
    input("Press enter for å returnere: ")

def get_product(navn: str) -> Produkt | None:
    global produkter

    for p in produkter:
        if p.navn.lower() == navn.lower():
            return p

    return None


def sell_product():
    global produkter

    print("--- TILGJENGELIGE PRODUKTER ---")
    for p in produkter:
        if p.antall <= 0:
            continue
        print(f"{p.navn:<10} - pris: {p.pris},-")  # :<10 gjør at p.navn tar opp 10 plasser (justify right)

    navn = input("Skriv navnet på produktet du ønsker å selge: ")
    produkt = get_product(navn)

    if not produkt:
        print(f"'{navn}' ikke funnet på lager")
        input("Press enter for å returnere: ")
        return

    antall = util.getInt("Skriv inn antall som skal selges: ")

    if antall < 0:
        print("Kan ikke selge negativt")
        input("Press enter for å returnere: ")
        return

    if antall > produkt.antall:
        print(f"Maks antall er {produkt.antall}")
        if util.confirm(f"Selg {produkt.antall}?"):
            produkt.antall -= produkt.antall
            return

    produkt.antall -= antall

def fill_storage():
    global produkter

    util.clear()
    print("--- FYLL PÅ LAGER ---")
    for p in produkter:
        print(f"{p.navn:<10} - Antall: {p.antall}")
        print("---")
    navn = input("Skriv navn på varen du skal fylle på: ")

    produkt = get_product(navn)
    if not produkt:
        print(f"'{navn}' Ikke funnet på lager")
        input("Press enter for å returnere: ")
        return

    antall = util.getInt("Skriv antall du ønsker å fylle på: ")
    if antall < 0:
        print("antall må være mer en 0")
        input("Press enter for å returnere: ")
        return

    produkt.antall += antall


def storage_value():
    global inventory
    util.clear()
    print("--- BEREGN LAGERVERDI ---")

    total: float = 0

    for p in produkter:
        total += p.verdi()

    print(f"Total verdi av lager: {total},-")
    input("Press enter for å returnere: ")
    

while True:

    util.clear()
    print("--- LAGERSTYRING ---")
    choice = util.menu(options)

    if options[choice] == "Vis produkter":
        show_products()
    elif options[choice] == "Selg produkt":
        sell_product()
    elif options[choice] == "Fyll på lager":
        fill_storage()
    elif options[choice] == "Beregn lagerverdi":
        storage_value()
    elif options[choice] == "Avslutt":
        break