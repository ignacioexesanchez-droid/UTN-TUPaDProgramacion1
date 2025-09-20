# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for num in range(0,101,):
     print (num)
     
     
# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene
num=int(input("ingrese un numero"))
num1=str(num)
cant=0
for num in num1:
    cant= cant + 1
print(cant)    
print(len(num1))


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
init = 0
end = 0

while init >= end:
    print("no se puede,el numero inicial es mayor o igual al final , ingrese otro numero")
    init = int(input("ingrese un valor inicial "))
    end = int(input("ingrese un valor final "))

print("todo ok", init , end)
number_range = list(range(init +1,end))

# 4 10
# number = [5 6 7 8 9]
suma = 0
for item in number_range:
    suma = suma + item     
    
print (f"La suma de todos los números enteros comprendidos entre {init} end es {end} = {suma}" )

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingresa un 0.
num = int(input("ingrese un numero entero "))
num_list = list()
suma = 0
while num > 0 :
    suma = suma + num 
    num_list.append(num)
    print("La suma parcial es ",suma )
    num = int(input("ingrese un numero entero "))
     
print(f"Su suma total de los numeros enteros {num_list} es {suma}")


# 5)Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, elprograma debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
num_random = random.randint (0,9)
print("numero random" , num_random)
attempts = 0
num = None
while (num is None) or num != num_random:
    num = int(input("ingrese un numero entero"))
    attempts= attempts + 1
    
print(f"la cantidad de intentos fueron {attempts} y tu numero fue correcto {num}") 


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
for num in range(100,-1,-1):
   print (num)



#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario
num = int(input("ingrese un numero postivo "))
num_list = list(range(num +1))
suma = 0 
for item in num_list:
    suma= suma + item 
     
print("tu suma es " ,suma)


#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el nprograma debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

limit = 5
num_list = []
while len(num_list) < limit:
    num = int(input("ingrese un numero "))
    num_list.append(num)

print(num_list)

pares_list = []
pares = 0 # mod
impares_list  = [] 
impares = 0  #mod con else
positivos_list = []
positivos = 0 # >0
negativos_list = []
negativos = 0 # else

for item in num_list:
    if item > 0:
        print ("tu numero es positvo")
        positivos_list.append(item)
        positivos = positivos +1
        
    else:
        print ("tu numero es negativo")
        negativos_list.append(item)
        negativos = negativos +1
    
    if item % 2 == 0:
        print ("tu numero es par")
        pares_list.append(item)
        pares = pares +1
    else:
         print ("tu numero es impar")
         impares_list.append(item)
         impares = impares +1

print(f"tus numeros postivos son {positivos}, tus mumeros negativos {negativos}, tus numeros pares son {pares}, tus numero impares {impares}")

print(f"tus lista de postivos es {positivos_list}, tus lista de negativos {negativos_list}, tus lista de pares son {pares_list}, tus lista de impares {impares_list}")



# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule lamedia de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

limit = 5
num_list = list ()
while len(num_list) < limit:
    num = int(input("ingrese numero positivos"))
    num_list.append(num)

suma=0
for item in num_list:
     suma = suma + item   
     
media= suma / len (num_list)
print("la media de todos los numeros ingresados es",media)
# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por elusuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

num = int(input("ingrese numero positivos"))
num_str = str(num)
str_list= []

for item in num_str:   
    str_list.inser(0,item)
    text = None

for item in str_list: 
    text = text + item             


