import util

def celsiusToFahrenheit(celsius: float) -> float:
    return celsius * (9 / 5) + 32

def celsiusToKelvin(celsius: float) -> float:
    return celsius + 273.15


temp = util.getFloat("Skriv inn Celsius: ")


fahrenheit = celsiusToFahrenheit(temp)
kelvin = celsiusToKelvin(temp)

print(f"{'Fahrenheit':<11}: {fahrenheit}")
print(f"{'Kelvin':<11}: {kelvin}")