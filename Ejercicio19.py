"""Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
no."""

def es_bisiesto(anyo):
  if (anyo % 4 == 0 and anyo % 100 !=0) or anyo % 400 == 0:
    return True
  return False

anyo = int(input("Introduce un año: "))
if es_bisiesto(anyo):
  print(f"EL {anyo} es un año bisiesto.")
else:
  print(f"El {anyo} no es un año bisiesto.")