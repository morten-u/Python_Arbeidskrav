
def finn_storste(tall_liste: list[int]) -> int:
    stor: int = tall_liste[0]

    for tall in tall_liste:
        if tall > stor:
            stor = tall
    return stor

def finn_minste(tall_liste: list[int]) -> int:
    minst: int = tall_liste[0]

    for tall in tall_liste:
        if tall < minst:
            minst = tall

    return minst


def test_func():

    STOR = 40000
    LITEN = -10

    tall_liste = [
        LITEN,
        12,
        22,
        52,
        200,
        STOR,
        12,
        500
    ]

    stor = finn_storste(tall_liste)
    liten = finn_minste(tall_liste)

    if stor != STOR and liten != LITEN:
        print("Feil")
    else:
        print("Suksess")

test_func()