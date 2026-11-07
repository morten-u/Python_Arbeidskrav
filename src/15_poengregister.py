
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def vis_info(self):
        print(f"Navn: {self.name}\nAlder: {self.age}")

person_list = [
    Person("Ole", 12),
    Person("Fredrik", 22),
    Person("Frida", 24),
    Person("Aleksander", 34),
    Person("Helene", 17)
]

for p in person_list:
    p.vis_info()
    if p.age > 18:
        print("Myndig")
    else:
        print("Ikke myndig")
    print()