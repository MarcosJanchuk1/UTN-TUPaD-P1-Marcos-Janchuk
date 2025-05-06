# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

# for i in range(101):
#     print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene. 

# numero = int(input("Ingresá un número entero: "))
# contador = 1
# while(numero >= 10):
#     numero = numero // 10
#     contador = contador + 1
# print(f"La cantidad de digitos es {contador}")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores. 

# n1 = int(input("Primer número: "))
# n2 = int(input("Segundo número: "))
# acumulador = 0
# 
# for i in range(n1, n2, 1):
#     acumulador = acumulador + i
# 
# print(f"La suma de los números es {acumulador}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0. 

# acumulador = 0
# numero = int(input("Ingresá un número (0 para terminar): "))
# while numero != 0:
#     numero = int(input("Ingresá un número (0 para terminar): "))
#     acumulador += numero
# 
# print("Suma total:", acumulador)


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# import random
# 
# numero_secreto = random.randint(0, 9)
# contador_intentos = 0
# 
# numero_usuario = int(input("Adiviná el número (0 a 9): "))
# 
# while numero_secreto != numero_usuario:
#     if contador_intentos != 0:
#         numero_usuario = int(input("Adiviná el número (0 a 9): "))
#         
#     contador_intentos += 1
#     if numero_usuario == numero_secreto:
#         print("Adivinaste en", contador_intentos, "intentos.")
#     else:
#         print("Incorrecto. Intenta de nuevo.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente. 

# for i in range(2, 101, 2):
#     print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario.


# while True:
#     numero_positivo = int(input("Ingrese un numero positivo: "))
#     if numero_positivo > 0:
#         break
# 
# acumulador = 0
# 
# for i in range(0, numero_positivo, 1):
#     acumulador = acumulador + i
# 
# print(f"La suma es: {acumulador}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

# contador_par = 0
# contador_impar = 0
# contador_negativo = 0
# contador_positivo = 0
# 
# for i in range(10):
#     numero = int(input("Ingrese un numero: "))
#     if numero % 2 == 0:
#         contador_par += 1
#     else:
#         contador_impar += 1
#     if numero > 0:
#         contador_positivo += 1
#     else:
#         contador_negativo += 1
# print(f"Pares: {contador_par}\nImpares: {contador_impar}\nNegativos: {contador_negativo}\nPositivo: {contador_positivo}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor). 

# promedio = 0
# acumulador = 0
# cantidad_numeros = 100
# for i in range(cantidad_numeros):
#     numero = int(input("Ingrese un numero: "))
#     acumulador = acumulador + numero
# 
# promedio = acumulador / cantidad_numeros
# 
# print(f"Se ingresaron {cantidad_numeros} numeros y el promedio es : {promedio}.")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 

numero = int(input("Ingrese un numero: "))
copia_numero = numero

texto_numero = ""
contador_digitos = 1
while(copia_numero >= 10):
    copia_numero = copia_numero // 10
    contador_digitos = contador_digitos + 1

for i in range(contador_digitos):
    resto = numero % 10
    texto_numero += str(resto)
    numero = int(numero / 10)

print(texto_numero)