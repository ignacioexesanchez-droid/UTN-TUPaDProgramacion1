#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

print("ACTIVIDAD 1")
edad= int(input("escribir tu edad"))
if edad >= 18:
    print("eres mayor de edad")
else:
    print("eres menor de edad")
#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberámostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar elmensaje “Desaprobado”.
print("ACTIVIDAD 2")
nota=int(input("escribir tu nota"))
if nota>= 6:
    print("estas aprobado")
else:
    print("estas desaprobado")
#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa unnúmero par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en casocontrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
print("ACTIVIDAD 3")
num= int(input("ingrese un numero "))
if num % 2 == 0:
  print("tu numero es par")
else: 
  print("tu numero es impar") 
  #4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las ,siguientes categorías pertenece:● Niño/a: menor de 12 años.● Adolescente: mayor o igual que 12 años y menor que 18 años.● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.● Adulto/a: mayor o igual que 30 años
  print("ACTIVIDAD 4")
  edad2=int(input("ingrese tu edad"))
  if edad2 < 12 :
      print ("eres niño")
  elif edad >= 12 or edad<18:
      print("eres adolescente")
  elif edad >= 18 or edad <30:
   print("eres adulto")
  #5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por enpantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir porpantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el usode la función len() en Python para evaluar la cantidad de elementos que tiene un iterable talcomo una lista o un string.
print("ACTIVIDAD 5")
contraseña= str(input("ingrese contraseña"))
if len(contraseña)>= 8 and len(contraseña)<=14:
    print("contraseña correcta")
else:
    print("contraseña incorrecta") 
print("ACTIVIDAD 6")
import random
from statistics import mean, median ,mode
num_aleatorios=[random.randint(1,100) for i in range(50)]
media = mean (num_aleatorios)
mediana= median(num_aleatorios)
moda= mode (num_aleatorios)
print("Números aleatorios:", num_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)
# Determinar el sesgo
if media > mediana and mediana > moda:
    print("Hay sesgo positivo (a la derecha).")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo (a la izquierda).")
else:
    print("No hay sesgo (simétrica).")
#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresadotermina con vocal, añadir un signo de exclamación al final e imprimir el string resultante porpantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo porpantalla.  
print("ACTIVIDAD( 7")
frase = str(input("Ingrese una frase: "))
if frase[-1].lower() in "aeiou":
    frase = frase + "!"
    print(frase)
else:
    print(frase)
print("ACTIVIDAD 8")
nombre_de_usuario = input("Ingrese su nombre: ")
print("Menú de opciones:")
print("1. Convertir a MAYÚSCULAS")
print("2. Convertir a minúsculas")
print("3. Convertir a Título")

opcion = input("Ingrese una opción (1/2/3): ")

if opcion == "1":
    print(nombre_de_usuario.upper())
elif opcion == "2":
    print(nombre_de_usuario.lower())
elif opcion == "3":
    print(nombre_de_usuario.title())
print("ACTIVIDAD 9")
magnitud_terremoto = float(input("Ingrese la magnitud de un terremoto: "))
# Si la magnitud es menor a 3, se considera "Muy leve"
if magnitud_terremoto < 3:
        print("Muy leve")
# Si la magnitud está entre 3 (inclusive) y menor que 4 → "Leve"
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:         
        print("Leve")
# Si la magnitud está entre 4 (inclusive) y menor que 5 → "Moderado"
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
        print("Moderado")
# Si la magnitud está entre 5 (inclusive) y menor que 6 → "Fuerte"
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
        print("Fuerte")
# Si la magnitud está entre 6 (inclusive) y menor que 7 → "Muy fuerte"
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
        print("Muy fuerte")
else:  #Todo lo que sea 7 o más
        print("Extremo")
print("ACTIVIDAD 10")
# Pido al usuario el hemisferio en el que se encuentra (N o S).
hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper() # .upper() convierte la entrada a mayúscula por si se ingrea (n/s)
mes_del_año = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))
# Determinar estación
# Opción 1: Invierno en el hemisferio norte, Verano en el sur
# Del 21 de diciembre al 20 de marzo
if (mes_del_año == 12 and dia >= 21) or (mes_del_año in [1, 2]) or (mes_del_año == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
# Opción 2: Primavera en el norte, Otoño en el sur
# Del 21 de marzo al 20 de junio
elif (mes_del_año == 3 and dia >= 21) or (mes_del_año in [4, 5]) or (mes_del_año == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
# Opción 3: Verano en el norte, Invierno en el sur
# Del 21 de junio al 20 de septiembre
elif (mes_del_año == 6 and dia >= 21) or (mes_del_año in [7, 8]) or (mes_del_año == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
# Opción 4: Otoño en el norte, Primavera en el sur
# Del 21 de septiembre al 20 de diciembre
elif (mes_del_año == 9 and dia >= 21) or (mes_del_año in [10, 11]) or (mes_del_año == 12 and dia <= 20):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
# Mostrar resultado
if hemisferio == "N":
    print("En el hemisferio norte la estación es:", estacion_norte)
elif hemisferio == "S":
    print("En el hemisferio sur la estación es:", estacion_sur)
else:
    print("Opción de hemisferio no válida. Use N o S.")