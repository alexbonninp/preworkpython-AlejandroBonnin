"""Ejercicio 12: Calculadora de Área de un Rectángulo
Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la
longitud y el ancho del rectángulo."""

def calcular_area_de_un_rectangulo(longitud, ancho):
  area = longitud * ancho
  return area

longitud = float(input("Introduce la longitud del rectangulo: "))
ancho = float(input("Introduce el ancho del rectangulo: "))

area_rectangulo = calcular_area_de_un_rectangulo(longitud, ancho)
print(f"El area del ectangulo es: {area_rectangulo}")
