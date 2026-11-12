

def get_int(prompt: str) -> int:

    while True:

        inn = input(prompt)
        try:

            number = int(inn)
            return number
        except ValueError:
            print(f"Error: '{inn}' er ikke et gyldig heltall")

def get_float(prompt: str) -> float:

    while True:

        inn = input(prompt)
        try:

            number = float(inn)
            return number

        except ValueError:
            print(f"Error: '{inn}' er ikke et gyldig tall")

# Tøm terminalen: \esc[H  = sender markøren til start
#                 \esc[2J = tømmer terminalen
def clear():
    print("\x1b[H\x1b[2J")

# Returnerer indexen til valget
def menu(options: list[str]) -> int:

    while True:

        for i, opt in enumerate(options):
            print(f"{i + 1}. {opt}")

        choice = get_int(f"Velg (1 - {len(options)}): ")

        if choice <= 0 or choice > len(options):
            print(f"Valg må være mellom 1 og {len(options)}")
            continue

        return choice - 1

def confirm(prompt: str) -> bool:
    answer = input(f"{prompt} [J/n]: ")

    if len(answer) == 0 or answer.lower().startswith("j"):
        return True

    return False


def header(title: str):
    clear()
    print(title)
    print()