# Ejercicios a entregar de la práctica 4.
# Comisiones 01, 06, 10, 11, 16 y 17:
# Los ejercicios a entregar son el 2, 3, 5, 9 y 14.
#-----------------------------------------------------------------------------------
# Ejercicio 2: Escribir un programa que lea dos números “n” y “m” y determine si m es
# divisible por n, mostrando el siguiente mensaje por pantalla: “El número n es/no es
# divisible por m”. Reemplazar n y m por los números correspondientes.

#SOLUCIÓN:

def imprimir_divisible(n, m):
    if n == 0 or m == 0:
        print("No se puede dividir por 0")
    elif m % n == 0:
        print("El número "+str(m)+" es divisible por "+str(n))
    else:
        print("El número "+str(m)+" no es divisible por "+str(n))

imprimir_divisible(0, 165)

#-----------------------------------------------------------------------------------
# Ejercicio 3: Escribir un programa que me indique si un número es divisible por 6,
# mostrando un mensaje por pantalla: “El número xx elegido es/no es divisible por 6”
# Ayuda: puede hacerlo usando la función definida en el ejercicio anterior.

#SOLUCIÓN:
def imp_divisible_por6(numero):
    imprimir_divisible(6, numero)

imp_divisible_por6(25)
#-----------------------------------------------------------------------------------
# Ejercicio 5: Dada la siguiente tabla

# Transporte             # Pasajeros
# Hoverboard                1
# Monopatin electrico       1
# Bicicleta                 2
# Moto                      2
# Auto                      4
# Camioneta                 12
# Colectivo                 40
# Avión                     200

# Escribir un programa que dada la cantidad de personas a viajar, determine el medio de
# transporte.
# Ayuda: defina una función que reciba como parámetro un número(la cantidad de persona
# a viajar) y retorne el medio de transporte que corresponda en la estructura adecuada.


def transporte(pasajeros):
	if pasajeros > 200:
		return "El máximo de pasajeros es 200."
	elif pasajeros == 1:
		return "Hoverboard o Monopatín eléctrico"
	elif pasajeros == 2:
		return "Bicicleta o Moto"
	elif pasajeros > 2 and pasajeros <= 4:
		return "Auto"
	elif pasajeros > 4 and pasajeros <= 12:
		return "Camioneta"
	elif pasajeros > 12 and pasajeros <= 40:
		return "Colectivo"
	elif pasajeros > 40 and pasajeros <= 200:
		return "Avión"


def print_transporte(pasajeros):
	print("Para "+str(pasajeros) +
	      " pasajeros se recomienda el siguiente vehiculo: "+transporte(pasajeros))

print_transporte(67)
viaje=int(input("Ingrese cantidad de pasajeros: "))
print_transporte(viaje)

#-----------------------------------------------------------------------------------
# Ejercicio 9: Diseña un programa Python que lea un carácter cualquiera desde el teclado,
# y muestre el mensaje @Es una MAYÚSCULA cuando el carácter sea una letra mayúscula y
# @Es una MINÚSCULA cuando sea una minúscula. En cualquier otro caso, no
# mostrará mensaje alguno. (Considera únicamente letras del alfabeto)
# Pista: aunque parezca una obviedad, recuerda que una letra es minúscula si está entre la
# ’a’ y la ’z’, y mayúscula si está entre la ’A’ y la ’Z’.
# Ayuda: defina una función que retorne un valor booleano si la letra es mayúscula y otra
# función similar, para el caso de la letra minúscula. Luego, en el programa principal,
# dependiendo del valor de retorno de las funciones, imprima el mensaje adecuado.


def imprimir_tipo(abc):
	if ord(abc) >= 65 and ord(abc) <= 90 or abc == "Ñ":
		print(str(abc)+" Es una mayúscula.")
	elif ord(abc) >= 97 and ord(abc) <= 122 or abc == "ñ":
		print(str(abc)+" Es una minúscula.")

letra = input("Ingrese una letra: ")
imprimir_tipo(letra)

#-----------------------------------------------------------------------------------
# Ejercicio 14: Calcular el número de pulsaciones que una persona debe tener por cada 10
# segundos de ejercicio aeróbico
# la fórmula que se aplica cuando la persona no está
# entrenada: (220-edad)/10
# si la persona está entrenada: (210-edad)/10.

def pulsaciones_cada10s(entrenamiento, edad):
    if entrenamiento == "Si" :
        return (210-edad)/10
    else:
        return(220-edad)/10

print(pulsaciones_cada10s("Si", 35))
print(pulsaciones_cada10s("No", 15))