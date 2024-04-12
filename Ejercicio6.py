"""Ejercicio 6: Verificación de Palíndromo
Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda)."""

def es_palindromo(palabra):
  palabra_invertida = palabra[::-1]
  if palabra == palabra_invertida:
    return True
  else:
    return False

palabra = input("Introduce una palabra: ")

if es_palindromo(palabra):
  print("Es palindromo")
else:
  print("No es palindromo")

