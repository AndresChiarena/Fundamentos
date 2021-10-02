#Ejercicio 15: Definir una función llamada calculo_dosis que reciba tres números.
#Uno para la cantidad de días que debe suministrarse el remedio, 
#el segundo dato para la cantidad de veces por día que debe tomarlo, 
#y el último dato para la cantidad de comprimidos que trae el envase.
#La función debe devolver verdadero si el envase alcanza para ese tratamiento y falso si no alcanza. 

def calculo_dosis(dias,dosis_diaria,envase):
    return (dias*dosis_diaria) <= envase


print (calculo_dosis(7, 3, 20))
print(calculo_dosis(30, 2, 60))
print(calculo_dosis(14, 2, 30))



