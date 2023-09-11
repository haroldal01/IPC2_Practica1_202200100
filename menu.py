from casilla import *
from lista_casillas import *


opcion1 = 5345

mitablero = listaCasillas()

while opcion1 != 3:
    print("elija una opción")
    print("1. crear tablero")
    print("2. mostrar datos del estudiante")
    print("3. salir ")

    opcion1 = int(input())

    if opcion1 == 1:
        ancho = int(input(" ingrese el ancho del tablero "))
        alto = int(input(" ingrese el alto del tablero "))
        mitablero.iniciar_tablero(alto,ancho,"⊛")

        mitablero.filas = alto
        mitablero.columnas = ancho

        #mitablero.imprimir_lista()

        continuar = 21

        while continuar != 2:
            print("======================================= GUATEMATEL ============================================")
            print("rango 1-",alto)
            fila = int(input("ingrese la fila de la casilla "))
            print("rango 1-",ancho)
            columna = int(input(" ingrese la columna de la casilla "))
            color = input(" ingrese el color de la casilla, solo ingrese la primera letra del color: \n V: verde \n R: rojo \n A: azul \n P: púrpura \n N: naranja \n")

            if color == "v" or color == "V":
                color = "green"
            elif color == "r" or color == "R":
                color = "red"
            elif color == "a" or color == "A":
                color = "blue"
            elif color == "p" or color == "P":
                color = "purple"
            elif color == "n" or color == "N":
                color = "orange"
            else:
                print("esa opción no es válida")


            mitablero.actualizar(fila,columna,color)

            mitablero.imprimir_tablero()

            continuar = int(input("¿desea continuar agregando casillas? \n 1.sí  \n 2.no "))

            if continuar == 2:
                mitablero.graficar()
                print("saliendo...")
            else:
                print("ingrese una opción válida")

        
    
          
    

    elif opcion1 ==2:
        print("carnet: 202200100")
        print("Harold Alejandro Sánchez Hernández")
        print("Introducción a la programación y computación 2")
        print("Sección C")


    elif opcion1 == 3:
        print("saliendo...")

    else:
        print("ingrese una opción correcta")


