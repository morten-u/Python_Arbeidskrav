import util

def beregn_snitt(poeng: list[float]) -> float:
    return sum(poeng) / len(poeng)

def finn_beste(navn: list[str], poeng: list[float]) -> str:

    largest: float = poeng[0]
    idx: int = 0

    for i, p in enumerate(poeng):
        if p > largest:
            largest = p
            idx = i

    return navn[idx]

name_list: list[str] = []
score_list: list[float] = []

for i in range(5):
    name_list.append(input("Navn: "))
    score_list.append(util.getFloat("Poeng: "))

print(f"Snitt: {beregn_snitt(score_list)}")
print(f"Beste elev: {finn_beste(name_list, score_list)}")