"""Ejercicio 18: Contador de Palabras
Ejercicios Introducción a Python: Enunciados 3
Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario."""

def contar_palabras(frase):
  palabras = frase.split()
  cantidad_palabras = len(palabras)
  return cantidad_palabras

frase = input("Introduce una frase: ")
cantidad_palabras = contar_palabras(frase)
print(f"La frase tiene {cantidad_palabras} palabras.")