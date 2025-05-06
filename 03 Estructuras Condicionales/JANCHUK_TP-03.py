# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

# edad = int(input("Ingrese su edad: "))
# 
# if edad >= 18:
#     print("Es mayor de edad.")
# else:
#     print("No es mayor de edad.")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
# mensaje “Desaprobado”. 

# nota = int(input("Ingrese su nota: "))
# mensaje = "Usted esta "
# if nota >=  6:
#     mensaje += "Aprobado."
# else:
#     mensaje += "Desaprobado."
# 
# print(mensaje)

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
# operador de módulo (%) en Python para evaluar si un número es par o impar. 

# numero = int(input("Ingrese un numero par: "))
# 
# if numero % 2 == 0:
#     mensaje = "Ha ingresado un numero par."
# else:
#     mensaje = "Por favor, ingrese un numero par."
# 
# print(mensaje)

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
# siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

# edad = int(input("Ingrese su edad: "))
# mensaje = "Usted se encuentra en la categoria: "
# if edad < 12:
#     mensaje += "niño."
# elif edad < 18:
#     mensaje += "adolescente."
# elif edad < 30:
#     mensaje += "adulto joven."
# else:
#     mensaje += "adulto mayor."
# 
# print(mensaje)

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
# como una lista o un string.

# contraseña = input("Ingrese una contraseña entre 8 y 14 caracteres por favor: ")
# largo_contraseña = len(contraseña)
# 
# if largo_contraseña >= 8 and largo_contraseña <= 14:
#     mensaje = "La contraseña fue ingresada correctamente. "
# else:
#     mensaje ="Por favor, ingrese una contraseña de entre 8 y 14 caracteres"
# 
# print(mensaje)

# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números 
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el 
# siguiente: 
# from statistics import mode, median, mean 
# mi_lista = [1,2,5,5,3] 
# mean(mi_lista) 
# En la documentación oficial se puede encontrar más información sobre este paquete: 
# https://docs.python.org/es/3.8/library/statistics.html.  
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se 
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la 
# mediana es mayor que la moda. 
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
# la mediana es menor que la moda. 
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales. 
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
# Definir la lista numeros_aleatorios de la siguiente forma: 
# import random 
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de 
# forma aleatoria. 


# import random
# import statistics
# 
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# 
# mediana = statistics.median(numeros_aleatorios)
# moda = statistics.mode(numeros_aleatorios)
# media = statistics.mean(numeros_aleatorios)
# 
# mensaje = "El sesgo de la lista aleatoria es: "
# 
# if media > mediana and mediana > moda:
#     mensaje += "positivo"
# elif media < mediana and mediana < moda:
#     mensaje += "negativo"
# elif media == mediana and media == moda:
#     mensaje += "ninguno, debido a que el valor de la media, mediana y moda, son iguales."
# else:
#     mensaje = "La lista proporcianada no es de sesgo positiv0, negativo o (ninguna)."
# 
# print(mensaje)


# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
# pantalla. 

# frase = input("Ingrese una frase: ")
# 
# ultima_letra = frase[-1]
# 
# if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
#     ultima_letra += "!"
# 
# print(ultima_letra)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# nombre = input("Ingrese su nombre: ")
# opcion = int(input("Ingrese 1 si desea su nombre en mayuscula, 2 para minuscula o 3 para la primera letra mayuscula."))
# 
# if opcion == 1:
#     nombre = nombre.upper()
# elif opcion == 2:
#     nombre = nombre.lower()
# elif opcion == 3:
#     nombre = nombre.title()
# else:
#     print("Por favor, ingrese 1, 2 o 3 para las opciones.")
# 
# print(nombre)

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
# por pantalla: 
# ● Menor que 3: "Muy leve" (imperceptible). 
# ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
# ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
# generalmente no causa daños). 
# ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
# débiles). 
# ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 

# opcion = int(input(
# """
# Lamentamos el terremoto.
# 
# Clasifique segun la escala de ritcher.
# 
# - Menor que 3: "Muy leve" (imperceptible).
# 
# - Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
# 
# - Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
#   generalmente no causa daños). 
# 
# - Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
#   débiles). 
# 
# - Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
# 
# - Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
# """))
# mensaje = "Terremoto de nivel "
# 
# if opcion < 3:
#     mensaje += "muy leve."
# elif opcion < 4:
#     mensaje += "leve."
# elif opcion < 5:
#     mensaje += "moderado."
# elif opcion < 6:
#     mensaje += "fuerte."
# elif opcion < 7:
#     mensaje += "muy fuerte."
# else:
#     mensaje += "extremo."
# 
# print(mensaje)

# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año 
# Periodo del año 
# Desde el 21 de diciembre hasta el 20 de 
# marzo (incluidos) 
# Estación en el 
# hemisferio norte 
# Invierno 
# Estación en el 
# hemisferio sur 
# Desde el 21 de marzo hasta el 20 de junio 
# (incluidos) 
# Desde el 21 de junio hasta el 20 de 
# septiembre (incluidos) 
# Desde el 21 de septiembre hasta el 20 de 
# diciembre (incluidos) 
# Primavera 
# Verano 
# Otoño 
# Verano 
# Otoño 
# Invierno 
# Primavera 

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = int(input("Ingrese un 1 si se encuentra en el Hemisferio norte o 2 si en Hemisferio sur "))
mes = input("Ingrese el mes actual: ")
numero_dia = int(input("Ingrese el numero del dia en que se encuentra: "))
mensaje = "Usted se encuentra en la estacion "

mes_correcto = True
dia_correcto = True
hemisferio_correcto = True


if (mes != "enero" and mes != "febrero" and mes != "marzo" and mes != "abril" and mes != "mayo" and mes != "junio" and
    mes != "julio" and mes != "agosto" and mes != "septiembre" and mes != "octubre" and mes != "noviembre" and mes != "diciembre"):
    mes_correcto = False
if (hemisferio != 1 and hemisferio != 2):
    hemisferio_correcto = False
if (numero_dia < 1 or numero_dia > 31):
    dia_correcto = False


if not mes_correcto and not dia_correcto and not hemisferio_correcto:
    mensaje = "El mes ingresado, día y hemisferio fueron ingresados incorrectamente. Por favor, vuelva a ejecutar el programa y lea atentamente."
elif not mes_correcto and not dia_correcto:
    mensaje = "El mes y el número del día ingresados son incorrectos.  "
elif not mes_correcto and not hemisferio_correcto:
    mensaje = "El mes y el hemisferio ingresados son incorrectos.  "
elif not dia_correcto and not hemisferio_correcto:
    mensaje = "El número del día y el hemisferio ingresados son incorrectos.  "
elif not mes_correcto:
    mensaje = "El mes ingresado es incorrecto.  "
elif not dia_correcto:
    mensaje = "El número del día ingresado es incorrecto. Debe estar entre 1 y 31."
elif not hemisferio_correcto:
    mensaje = "El hemisferio ingresado es incorrecto. Ingrese 1 para el norte o 2 para el sur."
elif (mes_correcto and dia_correcto and hemisferio_correcto):
    if (mes == "diciembre" and numero_dia >= 21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and numero_dia <= 20):
        if hemisferio == 1:
            print("Estas en la opcion 1")
            mensaje += "de inviero"
        elif hemisferio == 2:
            mensaje += "de verano"
    elif (mes == "marzo" and numero_dia >= 21) or mes == "abril" or mes == "mayo" or (mes == "junio" and numero_dia <= 20):
        if hemisferio == 1:
            mensaje += "de primavera"
        elif hemisferio == 2:
            mensaje += "de otoño"
    elif (mes == "junio" and numero_dia >= 21) or mes == "julio" or mes == "agosto" or (mes == "septiembre" and numero_dia <= 20):
        if hemisferio == 1:
            mensaje += "de verano"
        elif hemisferio == 2:
            mensaje += "de invierno"
    elif (mes == "septiembre" and numero_dia >= 21) or mes == "octubre" or mes == "noviembre" or (mes == "diciembre" and numero_dia <= 20):    
        if hemisferio == 1:
            mensaje += "de otoño"
        elif hemisferio == 2:
            mensaje += "de primavera"

print(mensaje)