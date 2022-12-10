# Programa para calcular la raiz cuadrada haciendo uso del bucle while
import math
print("Programa para calcular la raiz cuadrada")
numero = int(input("Introduce un numero para calcular: "))
intentos = 0

while numero<0:
    print("No se pude hallar la raiz de un numero negativo")

    if intentos == 2:
        print("Has errado demasiadas veces, finalizó el programa")
        break;

        numero=int(input("Introduce un numero porfavor: "))
        if numero<0:
            intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))
    