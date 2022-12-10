# Programa para calificar a un alumno
print("Programa para calificar a un alumno")
cal_alumno = input('Introduce tu calificacion: ')

# Funcion para calificar
def calificar(cal):
    estatus = 'Aprobado'
    # Condicional IF
    if cal<5:
        estatus = 'Reprobado'
    return estatus

# Llamar la funcion 
print(calificar(int(cal_alumno)))
