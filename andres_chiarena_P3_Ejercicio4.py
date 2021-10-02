#Ejercicio 4: Definir una función denominada “imprimo_fecha” que reciba tres cadenas de caracteres 
#que representan un día, un mes y un año e imprima  la fecha de la siguiente manera: “ 21 de septiembre de 2012”.

def imprimo_fecha(dd,mm,aaaa):
    print(str(dd)+" de "+str(mm)+" de "+str(aaaa))

imprimo_fecha(25,"julio",1988)

dd= input("Ingresar día: ")
mm= input("Ingresar mes: ")
aaaa= input("ingresar año: ")
imprimo_fecha(dd,mm,aaaa)