"""Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un
descuento del 20%."""

def calcular_precio_final(precio):
  descuento = consumo * 0.2
  total = consumo - descuento
  return total

consumo = float(input("Introduce el precio del articulo: "))
precio_descuento = calcular_precio_final(consumo)

print(f"El total a pagar con el descuento es: {precio_descuento}")
