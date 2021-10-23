# Ejercicio 1: Escribir un programa que muestre la tabla de multiplicar de un número
# introducido por teclado por el usuario.

numero = int(input("Introducir un numero diferente a 0: "))
multiplica = 1

while multiplica <= 10: # para hacer hasta el 10 pero puede ser mas extenso
    resultado = numero*multiplica
    print(str(numero)+" x "+str(multiplica)+" = "+str(resultado))
    multiplica = multiplica + 1

# -----------------------------------------------------------------------------------
# Ejercicio 7: Escriba un programa que lea números de documentos de identidad de
# personas hasta que se ingrese el número “999”. Debe imprimir la cantidad de números de
# documentos menores que 20.000.000.

menos_de_20mill = 0
dni = int(input("Ingrese un numero de documento sin puntos(ingresar 999 para finalizar programa): "))

while dni != 999:
	if dni < 20000000:
		menos_de_20mill = menos_de_20mill +1
	dni = int(input("Ingrese un numero de documento: "))

print("personas con dni menor a 20 millones: "+str(menos_de_20mill))

#-----------------------------------------------------------------------------------
# Parte III: Ahora practicamos con Colecciones

# Ejercicio 12: Dada la siguiente lista [1, 14, 56, 43, 23, 46, 58, 123, 67 ] escribir un
# programa que muestre el número más alto.

lista = [1, 14, 56, 43, 23, 46, 58, 123, 67]

print(max(lista))  # seria la opción más directa...
#si lo que se requiere es utilizar while, podria hacer algo como:

x = 0
mayor = [lista[0]]
while x <= 8:
    if mayor[0] < lista[x]:
        mayor.pop(0)
        mayor.append(lista[x])
    x = x+1
print(mayor)

# -----------------------------------------------------------------------------------
# Ejercicio 13: Escriba un programa que solicite nombres de localidades y códigos postales
# al usuario hasta que se ingresa el código postal 0. Debe generar una lista con todos los
# valores ingresados e imprimirla.

localidad = input("Ingrese una localidad: ")
cod_postal = int(input("Ingrese un codigo postal(finaliza el programa con '0'): "))
lista_de_codigos = []

while cod_postal !=0:
    lista_de_codigos.append((localidad,cod_postal))
    localidad = input("Ingrese una localidad: ")
    cod_postal = int(input("Ingrese un codigo postal: "))

print(lista_de_codigos)