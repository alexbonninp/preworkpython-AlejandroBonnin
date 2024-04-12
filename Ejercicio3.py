"""Ejercicio 3: Verificación de Edad
Escribe un programa que solicite la edad de un usuario y determine si es mayor de
edad (mayor o igual a 18 años) o no."""

def verificar_edad(edad):
  if edad >= 18:
    return "Es mayor de edad" 
  else:
    return "Es menor de edad" 

edad = int(input("Introduce la edad: "))

mensaje = verificar_edad(edad)

print(mensaje)