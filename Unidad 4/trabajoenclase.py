#Vas a programar un juego clásico contra la computadora: Piedra, papel o tijeras.
print("ACTIVIDAD 2")
import random

victorias = 0
derrotas = 0
empates = 0
continuar = 1

while continuar == 1:
    print("\nElige una opción:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")

    opcion = int(input("Tu elección (1,2,3): "))

    if opcion < 1 or opcion > 3:
        print("Opción inválida. Intenta de nuevo.")
        continue  
    opcionPC = random.randint(1, 3)
    
    if opcion == 1:
        Usuario = "Piedra"
    elif opcion == 2:
        Usuario = "Papel"
    else:
        Usuario = "Tijera"

    if opcionPC == 1:
        PC = "Piedra"
    elif opcionPC == 2:
        PC = "Papel"
    else:
        PC = "Tijera"

    print("Tú elegiste:", Usuario)
    print("La compu eligió:", PC)

    if opcion == opcionPC:
        print("¡Empate!")
        empates += 1
    elif (opcion == 1 and opcionPC == 3) or \
         (opcion == 2 and opcionPC == 1) or \
         (opcion== 3 and opcionPC == 2):
        print("¡Ganaste!")
        victorias += 1
    else:
        print("Perdiste :(")
        derrotas += 1

    continuar = int(input("¿Deseas jugar otra vez? (1: Sí, 0: No): "))
print("\nResumen del juego:")
print("Victorias:", victorias)
print("Derrotas:", derrotas)
print("Empates:", empates)