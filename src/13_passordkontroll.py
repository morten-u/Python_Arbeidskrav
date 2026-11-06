
def sjekk_passord(passwd: str) -> bool:

    if len(passwd) < 8:
        return False

    has_upper = False
    has_digit = False

    for c in passwd:
        if str.isupper(c):
            has_upper = True

        if str.isdigit(c):
            has_digit = True

    if not has_upper or not has_digit:
        return False

    return True

while True:
    passwd = input("Skriv inn nytt passord: ")

    if sjekk_passord(passwd):
        print("Gyldig passord")
    else:
        print("Passord må være minimum 8 karakterer, inneholde 1 tall og 1 stor bokstav")