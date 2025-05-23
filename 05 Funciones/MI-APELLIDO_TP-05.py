#1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

"""def imprimir_hola_mundo():
    mensaje = "Hola Mundo!"
    print(mensaje)

def main():
    imprimir_hola_mundo()

main()"""
# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
#volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.
"""
def saludar_usuario(nombre):
    mensaje = f"Hola {nombre}!"
    print(mensaje)

def main():
    saludar_usuario("Marcos")

main()
"""
# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
#dir los datos al usuario y llamar a esta función con los valores in
#gresados.

"""def informacion_personal(nombre, apellido, edad, residencia):
    mensaje = f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"
    return mensaje

def main():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))
    residencia = input("Ingrese su residencia: ")
    mensaje = informacion_personal(nombre, apellido, edad, residencia)
    print(mensaje)

main()"""

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
# dio como parámetro y devuelva el área del círculo. calcular_peri
# metro_circulo(radio) que reciba el radio como parámetro y devuel
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am
# bas funciones para mostrar los resultados.

"""def calcular_area_circulo(radio):
    area_circulo = 3.14 * (radio ** 2)
    return area_circulo

def calcular_perimetro_circulo(radio):
    perimetro_circulo = 2 * 3.14 * radio
    return perimetro_circulo

def main():
    radio = float(input("Ingrese el radio del circulo: "))
    area_circulo = calcular_area_circulo(radio)
    perimetro_circulo = calcular_perimetro_circulo(radio)
    mensaje = f"El perimetro es: {perimetro_circulo} y el area del circulo es: {area_circulo}"

    print(mensaje)

main()
"""
#  5. Crear una función llamada segundos_a_horas(segundos) que reciba
#  una cantidad de segundos como parámetro y devuelva la cantidad
#  de horas correspondientes. Solicitar al usuario los segundos y mos
# trar el resultado usando esta función.
"""
def segundos_a_horas(segundos):
    horas = (segundos / 60) / 60
    return horas

def main():
    segundos = float(input("Ingrese una cantidad de segundos: "))
    horas = segundos_a_horas(segundos)

    print(horas)

main()
"""
#  6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#  número como parámetro y imprima la tabla de multiplicar de ese
#  número del 1 al 10. Pedir al usuario el número y llamar a la fun
# ción.

"""def tabla_multiplicar(numero):
    lista_tabla_multiplicar = []
    for i in range(1,11,1):
        resultado = numero * i
        lista_tabla_multiplicar.append(resultado)
    return lista_tabla_multiplicar

def mostrar_lista(lista):
    for elemnto in lista:
        print(elemnto)

def main():
    numero = int(input("Ingrese un numero: "))
    mostrar_lista(tabla_multiplicar(numero))

main()
"""
#  7. Crear una función llamada operaciones_basicas(a, b) que reciba
#  dos números como parámetros y devuelva una tupla con el resulta
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
# sultados de forma clara.
"""
def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    producto = a * b
    division = a / b

    resultados = (('Suma ', suma), ('Resta' , resta), ('Producto' ,producto), ('Division' , division))
    return resultados

def main():
    numero_a = float(input("Ingresa un numero: "))
    numero_b = float(input("Ingresa otro numero: "))
    resultado = operaciones_basicas(numero_a,numero_b)
    print(resultado)

main()
"""
#  8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#  peso en kilogramos y la altura en metros, y devuelva el índice de
#  masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
# ción para mostrar el resultado con dos decimales.
"""
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def main():
    peso = float(input("Ingrese su peso en KG: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Tu IMC es de: {imc}")
main()"""

#  9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#  una temperatura en grados Celsius y devuelva su equivalente en
#  Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#  resultado usando la función.
"""
def celcius_a_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

def main():
    celcius = float(input("Ingrese los grados celcius: "))
    grados_fahrenheit = celcius_a_fahrenheit(celcius)
    print(grados_fahrenheit)

main()"""

#  10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#  tres números como parámetros y devuelva el promedio de ellos.
#  Solicitar los números al usuario y mostrar el resultado usando esta
#  función.

def calcular_promedio(a,b,c):
    promedio = (a+b+c) / 3
    return promedio

def main():
    a = int(input("Ingrese un entero: "))
    b = int(input("Ingrese otro entero: "))
    c = int(input("Ingrese otro entero: "))
    promedio = calcular_promedio(a,b,c)
    print(promedio)

main()