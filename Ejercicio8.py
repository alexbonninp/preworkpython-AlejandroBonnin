"""Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona."""

def calcular_imc(peso, altura):
  imc = peso / (altura ** 2)
  return imc

peso = float(input("introduce el peso en kg: "))
altura = float(input("introduce la altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"El indice de masa corporal es: {imc:.2f}")
