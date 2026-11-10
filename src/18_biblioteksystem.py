from enum import Enum
import util

class Opt(Enum):
    VIS_ALLE_BØKER = 0
    LÅN_EN_BOK = 1
    LEVER_TILBAKE = 2
    VIS_TILGJENGELIG = 3
    AVSLUTT = 4

options = [
    "Vis alle bøker",
    "Lån en bok",
    "Lever tilbake en bok",
    "Vis tilgjengelige bøker",
    "Avslutt"
]

class Book:
    def __init__(self, name: str, author: str) -> None:
        self.name = name
        self.author = author
        self.available = True
        pass

    def toString(self) -> str:
        available_str = "Ja"
        if not self.available:
            available_str = "Nei"

        return f"Navn: {self.name}\nForfatter: {self.author}\nTilgjengelig: {available_str}"

    def borrowBook(self):
        self.available = False

    def returnBook(self):
        self.available = True

inventory = [
    Book("Snømannen", "Jo Nesbø"),
    Book("Drep ikke en sangfugl", "Harper Lee"),
    Book("Den fremmede", "Albert Camus"),
    Book("Brødrene Løvehjerte", "Astrid Lindgren"),
    Book("The catcher in the rye", "J.D Salinger"),
    Book("Krig og fred", "Lev Tolstoj")
]

def findBook(book_name: str) -> Book | None:
    global inventory

    for book in inventory:
        if book.name == book_name:
            return book

    return None


def showAll():
    global inventory

    util.clear()
    for book in inventory:
        print(book.toString())
        print("---")
    input("Press enter for å gå tilbake")

def borrowBook():
    global inventory
    util.clear()

    print("--- LÅN BOK ---")
    available_count = 0
    for book in inventory:
        if book.available:
            print(book.name)
            available_count += 1
    print()

    if available_count == 0:
        print("Ingen bøker tilgjengelig for utlån")
        input("Press enter for å gå tilbake: ")
        return

    name = input("Skriv navnet på boken du ønsker å låne: ")

    book = findBook(name)

    if not book:
        print(f"{name}: ikke funnet")
        input("Press enter for å gå tilbake")
        return

    if not book.available:
        print(f"{name} er ikke tilgjengelig")
        input("Press enter for å returnere")
        return

    if util.confirm(f"Låne {book.name}?"):
        book.available = False
        print(f"{book.name} utlånt")

    input("Press enter for å gå tilbake")

def returnBook():
    global inventory

    util.clear()

    print("--- LEVER BOK ---")
    borrow_count = 0
    for book in inventory:
        if not book.available:
            print(book.name)
            borrow_count += 1
    print()

    if borrow_count == 0:
        print("Ingen bøker er lånt ut")
        input("Press enter for å gå tilbake")
        return

    name = input("Skriv navnet på boken du skal returnere: ")

    book = findBook(name)

    if not book:
        print(f"{name}: ikke funnet")
        input("Press enter for å gå tilbake")
        return

    if book.available:
        print(f"{name} er ikke lånt ut")
        input("Press enter for å gå tilbake")
        return

    if util.confirm(f"Lever {book.name} tilbake?"):
        print(f"{book.name} Levert")
        book.available = True
        return

def showAvailable():
    global inventory

    util.clear()
    print("--- VIS TILGJENGELIGE BØKER ---")
    for book in inventory:
        
        if book.available:
            print(book.toString())
            print("---")
    print()
    input("Press enter for å gå tilbake")


while True:

    util.clear()
    print("--- BIBLIOTEK ---")
    choice = Opt(util.menu(options))

    if choice == Opt.VIS_ALLE_BØKER:
        showAll()
    elif choice == Opt.LÅN_EN_BOK:
        borrowBook()
    elif choice == Opt.LEVER_TILBAKE:
        returnBook()
    elif choice == Opt.VIS_TILGJENGELIG:
        showAvailable()
    elif choice == Opt.AVSLUTT:
        break