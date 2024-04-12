"""Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos."""

def convertir_a_horas_y_minutos(minutos):
  horas = minutos // 60
  minutos_restantes = minutos % 60
  return horas, minutos_restantes

minutos = int(input("Introduce la cantidad de minutos: "))
horas, minutos_restantes = convertir_a_horas_y_minutos(minutos)

print(f"{minutos}minutos son {horas} horas y {minutos_restantes} minutos")

