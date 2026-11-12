import util

class Student:
    def __init__(self, navn: str, alder: int, karakter: int) -> None:
        self.navn = navn
        self.alder = alder
        self.karakter = karakter
        pass

    def vis_info(self):
        print(f"Navn: {self.navn}")
        print(f"Alder: {self.alder}")
        print(f"Karakter: {self.karakter}")


studenter: list[Student] = []

options = [
    "Registrer student",
    "Vis alle studenter",
    "Søk etter student",
    "Fjern student",
    "Beregn gjennomsnittskarakter",
    "Finn student med høyest karakter",
    "Avslutt"
]

# Hjelper funksjon for å finne studenter
def find_student(name: str) -> Student | None:
    global studenter

    for s in studenter:
        if s.navn.lower() == name.lower():
            return s

    return None

#
# 1. Registrer student
#
def register_student():
    global studenter

    util.clear()
    print("--- REGISTRER STUDENT ---")
    name = input("Navn: ")

    if find_student(name):
        print(f"'{name}' er allerede registrert")
        input("Press enter for å returnere: ")
        return

    age = util.get_int("Alder: ")

    grade = 0

    while True:
        grade = util.get_int("Karakter: ")

        if grade < 1 or grade > 6:
            print("Karakter må være mellom 1 og 6")
            continue

        break

    student = Student(name, age, grade)
    print(f"Student: {student.navn} lagt til")
    studenter.append(student)
    input("Press enter for å returnere: ")
    
#
# 2. Vis alle studenter
#

def show_students():
    global studenter

    util.clear()
    print("--- VIS ALLE STUDENTER ---")
    print()

    if len(studenter) == 0:
        print("Ingen studenter registrert")

    for s in studenter:
        s.vis_info()
        print("---")
    input("Press enter for å returnere: ")

#
# 3. Søk etter student
#
def search_for_student():
    global studenter
    util.header("--- SØK ETTER STUDENT ---")

    name = input("Navn: ")

    count = 0
    for s in studenter:
        s_name = s.navn.lower()

        if s_name.startswith(name.lower()):
            count += 1
            s.vis_info()
            print("---")

    if count == 0:
        print(f"Ingen student med navnet '{name}' funnet")

    input("Press enter for å returnere")

#
# 4. Fjern student
#
def remove_student():
    global studenter
    util.header("--- FJERN STUDENT ---")

    if len(studenter) == 0:
        print("Ingen studenter registrert")
        input("Press enter for å returnere: ")
        return

    student_names = []
    for s in studenter:
        student_names.append(s.navn)

    choice = util.menu(student_names)

    student: Student
    for s in studenter:
        if s.navn == student_names[choice]:
            student = s

    print(f"{student.navn} fjernet")
    studenter.remove(student)
    input("Press enter for å returnere: ")

#
# 5. Beregn gjennomsnittskarakter
#
def average_grade():
    global studenter

    util.header("--- GJENNOMSNITTSKARAKTER ---")

    if len(studenter) == 0:
        print("Ingen studenter registrert")
        input("Press enter for å returnere: ")
        return

    total_grades = 0

    for s in studenter:
        total_grades += s.karakter

    avg_grade = total_grades / len(studenter)

    print(f"snitt karakter = {avg_grade}")
    input("Press enter for å returnere: ")
    
#
# 6. Finn studenten med høyeste karakter
#       printer student med høyeste karakter.
#       Om det er flere studenter med lik karakter
#       printes alle.
#
def highest_grade():
    global studenter

    util.header("--- STUDENT MED HØYESTE KARAKTER ---")

    if len(studenter) == 0:
        print("Ingen studenter registrert")
        input("Press enter for å returnere: ")
        return
    
    karakter = 0

    for s in studenter:
        if s.karakter > karakter:
            karakter = s.karakter

    for s in studenter:
        if s.karakter == karakter:
            s.vis_info()
            print("---")

    input("Press enter for å returnere: ")

while True:

    util.clear()
    print("--- STUDENTADMINISTRASJON ---")
    choice = util.menu(options)

    if   options[choice] == "Registrer student":
        register_student()

    elif options[choice] == "Vis alle studenter":
        show_students()

    elif options[choice] == "Søk etter student":
        search_for_student()

    elif options[choice] == "Fjern student":
        remove_student()

    elif options[choice] == "Beregn gjennomsnittskarakter":
        average_grade()

    elif options[choice] == "Finn student med høyest karakter":
        highest_grade()

    elif options[choice] == "Avslutt":
        break