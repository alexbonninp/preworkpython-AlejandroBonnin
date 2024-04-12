"""Ejercicio 11: Calculadora de Edad
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual."""

def calculadora_edad(anyo):
  anyo_actual = 2024
  edad = anyo_actual - anyo_nacimiento
  return edad

anyo_nacimiento = int(input("Introduce el año de nacimiento"))
edad = calculadora_edad(anyo_nacimiento)

print(f"¡Tienes {edad} años!")


