nombre = input("Ingresar nombre: ")
apellido = input("Ingresar apellido: ")
nacimiento = input("Ingresar fecha de nacimiento (dd/mm/aaaa): ")
contrasena = nombre[0] + apellido[0] +"_"+nacimiento[-4:]
print("Nueva contraseña creada para ",nombre," :",contrasena)