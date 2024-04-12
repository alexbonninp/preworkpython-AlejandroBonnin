"""Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario."""

def suma(a, b):
  return a + b

def resta(a, b):
  return a - b

def multiplicacion(a, b):
  return a * b

def division(a, b):
  if b != 0:
    return a / b
  else:
    return("Error matematico")

print("Operaciones disponibles: ")
print("1. Suma")
print("2. Resta ")
print("3. Multiplicacion ")
print("4. Division ")

opcion = int(input("selecciona una operacion (1,2,3,4): "))
num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))

if opcion == 1:
  resultado = suma(num1, num2)
elif opcion == 2:
  resultado = resta(num1, num2)
elif opcion == 3:
  resultado = multiplicacion(num1, num2)
elif opcion == 4:
  resultado = division(num1, num2)
else:
  resultado = "Operacion no valida"
print(f"Resultado: {resultado}")