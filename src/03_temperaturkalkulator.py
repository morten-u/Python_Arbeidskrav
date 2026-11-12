import util

def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * (9 / 5) + 32

def celsius_to_kelvin(celsius: float) -> float:
    return celsius + 273.15


temp = util.get_float("Skriv inn Celsius: ")


fahrenheit = celsius_to_fahrenheit(temp)
kelvin = celsius_to_kelvin(temp)

print(f"{'Fahrenheit':<11}: {fahrenheit}")
print(f"{'Kelvin':<11}: {kelvin}")