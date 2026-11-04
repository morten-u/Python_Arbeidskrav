

def getInt(prompt: str) -> int:

    while True:

        inn = input(prompt)
        try:

            number = int(inn)
            return number
        except ValueError:
            print(f"Error: '{inn}' er ikke et gyldig heltall")

def getFloat(prompt: str) -> float:

    while True:

        inn = input(prompt)
        try:

            number = float(inn)
            return number

        except ValueError:
            print(f"Error: '{inn}' er ikke et gyldig tall")