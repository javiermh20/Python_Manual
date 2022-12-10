# Programa para verificar si es correcto un email
contador = 0
miEmail = input("Introduce tu direccion de email: ")

# ciclo for para contar los caracteres especiales del correo
for i in miEmail:
    if (i=="@" or i =="."):
        contador = contador + 1

# if para verificar que el correo es correcto
if contador==2:
    print("Email es correcto")
else:
    print("Email incorrecto")
