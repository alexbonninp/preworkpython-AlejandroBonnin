"""Ejercicio 9: Conversor de Divisas
Ejercicios Introducción a Python: Enunciados 2
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros."""

def dolares_a_euros(dolares):
  euros = dolares * 0.85
  return euros
cantidad_dolares = float(input("introduce la cantidad de dolares: "))
cantidad_euros = dolares_a_euros(cantidad_dolares)

print(f"La cantidad de euros es: {cantidad_euros}")
