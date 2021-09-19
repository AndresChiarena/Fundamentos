# Ejercicio 10: Pedir ancho y largo de un terreno y mostrar cuántos paneles de pasto hay que comprar (son de 60x60 cm)
metros_de_ancho = float(input("Ingrese el ancho del terreno en metros: "))
metros_de_largo = float(input("Ingrese el largo del terreno en metros: "))
print("Debe comprar: ",round((metros_de_ancho )* ( metros_de_largo) / 0.36)," paneles de pasto." )