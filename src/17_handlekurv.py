
class Produkt:
    def __init__(self, navn: str, pris: float, antall: int) -> None:
        self.navn = navn
        self.pris = pris
        self.antall = antall

    def vis_info(self):
        print(f"Navn:   {self.navn}")
        print(f"Pris:   {self.pris}")
        print(f"Antall: {self.antall}")

    def beregn_verdi(self) -> float:
        return self.pris * self.antall


def beregn_total(produkter: list[Produkt]) -> float:
    total = 0
    for p in produkter:
        total += p.beregn_verdi()

    return total

handlekurv = [
    Produkt("Melk", 20, 2),
    Produkt("Brød", 34, 4),
    Produkt("Kaffe", 50, 1),
    Produkt("Ost", 80, 2),
    Produkt("Eple", 40, 6)
]

for produkt in handlekurv:
    produkt.vis_info()

print()
print(f"Total pris: {beregn_total(handlekurv)}")