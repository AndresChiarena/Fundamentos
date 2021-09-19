#Ejercicio 23: Dada la siguiente información, elija una estructura de datos que permita guardarla adecuadamente 
#● Guerra del Peloponeso 431 a.C 
#● Revolución de Mayo 1810 d.C
#● Llegada de los españoles a América 1492 d.C
#● Comienzo de la construcción de la gran Muralla China 214 a.C

#guardo los datos en tuplas
hecho1 = ("Guerra del Peloponeso ","431 a.C")
hecho2 = ("Revolución de Mayo ","1810 d.C")
hecho3 = ("Llegada de los españoles a América ","1492 d.C")
hecho4 = ("Comienzo de la construcción de la gran Muralla China ","214 a.C")

#y creo una lista vacia para ir agregando hechos en orden cronológico
linea_de_tiempo = []

linea_de_tiempo.append(hecho1)
linea_de_tiempo.append(hecho4)
linea_de_tiempo.append(hecho3)
linea_de_tiempo.append(hecho2)

#imprimo la lista que contiene las tuplas
print (linea_de_tiempo)