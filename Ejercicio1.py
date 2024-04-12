'''Conversor de Temperatura
Escribe un programa que convierta una temperatura de grados Celsius a grados
Fahrenheit.'''

def celsius_a_fahrenheit(celsius):
  return celsius * (9/5) + 32

temperatura_celsius = float(input("introduzca la temperatura(celsius) a convertir a Grados  fahrenheit: "))

temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)

print(f"La temperatura en Fahrenheit es: {temperatura_fahrenheit}")