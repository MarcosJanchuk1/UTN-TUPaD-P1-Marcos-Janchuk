# TRABAJO LISTAS - Marcos Janchuk #

# (1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función 
# range.
"""
# Creamos la lista vacia.
lista_numeros = []

# Creamos un bucle for con la funcion range.
for i in range(2,101,2):
    # Controlamos que i sea multiplo de 4 utilizando la operacion resto.
    if i % 4 == 0:
        # Si la condicion es verdadera, agregamos el numero a la lista.
        lista_numeros.append(i)
# Imprimimos la lista final.
print(lista_numeros)
"""
# (2)  Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el 
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el 
# indexing con números negativos! 
"""
# Creamos una lista de 5 elementos.
Lista_random = [True, False, 7, "San Juan 3:16", ["Marcos", "Janchuk"]]
# Guardamos en una variable el penultimo elemento de la lista.
penultimo_elemento_lista_random = [Lista_random[-2]]
# Mostramos por pantalla el penultimo elemento de la lista
print(penultimo_elemento_lista_random)
"""
# (3)  Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por 
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por 
# ejemplo: 
"""
# Creamos una lista vacia
lista_vacia = []
palabra = ""
# Creamos el ciclo for para que itere 3 veces utilizando la funcion range.
for i in range(3):
    palabra = input("Ingrese una palabra: ")
    # Agregamos con append las palabras ingresadas por el usuario a la lista vacia.
    lista_vacia.append(palabra)
# Imprimimos por pantalla la lista.
print(lista_vacia)
"""
# (4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, 
# respectivamente.  Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra 
# en los videos o bien investigar cómo funciona el indexing con números negativos! 
"""
# Creamos la lista animales.
animales = ["perro", "gato", "conejo", "pez"] 
# Reemplazamos el segundo elemento
animales[1] = "loro"
# Reemplazamos el ultimo elemento
animales[-1] = "oso"
# Mostramos por pantalla el resultado.
print(animales)
"""

# (5)  Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
# numeros = [8,15,3,22,7]
# numeros.remove(max(numeros))
# print(numeros)

# Explicacion del algoritmo con comentarios.
"""
# Se crea la lista numeros.
numeros = [8,15,3,22,7]
# Se utiliza el metodo remove para remover un elemento de la lista.
# El elemento a remover es el maximo de la lista, el cual se busca con la funcion max.
numeros.remove(max(numeros))
# Mostramos por pantalla como queda la lista luego de remover el numero mas grande de la lista.
print(numeros)
"""

# (6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por 
# pantalla los dos primeros. 
"""
# Creamos una lista vacia
lista_numeros = []
# Creamos un ciclo for para llenar la lista vacia de numeros.
for i in range(10,31,5):
    # Guardamos en la lista los numeros entre 10 al 30, incluido, con saltos 5 en 5.
    lista_numeros.append(i)
# Mostramos por pantalla la lista final.
print(lista_numeros)

"""

# (7)  Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores 
# cualesquiera.
"""
# Creamos la lista autos
autos = ["sedan", "polo", "suran", "gol"]

# Reemplazamos los valores en las posiciones 1 y 2
autos[1] = "mercedes"
autos[2] = "audi"
# Mostramos por pantalla la lista autos
print(autos)
"""

# (8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append 
# directamente. Imprimir la lista resultante por pantalla. 
"""
# Creamos una lista vacia segun la consigna.
dobles = []

for i in range(5,16,5):
    # Guardamos en una variable el doble del numero.
    doble_numero = i * 2
    # Guardamos el doble en la lista dobles.
    dobles.append(doble_numero)
# Mostramos la lista dobles.
print(dobles)
"""

# (9) Dada la lista “compras”, cuyos elementos representan los productos comprados por 
# diferentes clientes: 
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 
# a) Agregar "jugo" a la lista del tercer cliente usando append. 
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
# c) Eliminar "pan" de la lista del primer cliente.  
# d) Imprimir la lista resultante por pantalla 

# Creamos la lista compras.
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 
"""
# Creamos un ciclo for para nuestro algoritmo.
for i in range(len(compras)):
    # Preguntamos, si i es igual a 0, para averiguar si estamos en el primer cliente.
    if i == 0:
        # removemos pan con .remove
        compras[i].remove("pan")
    elif i == 1:
        # reemplazamos fideos por tallarines.
        compras[i][1] = "tallarines"
    elif i == 2:
        compras[i].append("jugo")
# Mostramos por pantalla la lista compras final.
print(compras)
"""

# (10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
# ● Posición lista_anidada[0]: 15 
# ● Posición lista_anidada[1]: True 
# ● Posición lista_anidada[2][0]: 25.5 
# ● Posición lista_anidada[2][1]: 57.9 
# ● Posición lista_anidada[2][2]: 30.6 
# ● Posición lista_anidada[3]: False 
# Imprimir la lista resultante por pantalla.
"""
lista_anidada = [15,True,[25.5,57.9,30.6],False]

print(lista_anidada)
"""