#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
list_num = list (range(0,101))
for item in list_num:
    if item % 4 == 0:
        print("tu multiplos de 4 son ",item)


# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona elindexing con números negativos!

list_frutas =list(["manzana", "banana", "frutilla", "anana", "mandarina"])
print (list_frutas[-2])


# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por  pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior
limite = 3
lista_vacia =[]
while len(lista_vacia)<limite:
    pal =str (input("ingrese palabras"))
    lista_vacia.append(pal)

for item in lista_vacia:
    print(lista_vacia)


#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestraen los videos o bien investigar cómo funciona el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"]
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[3] = "oso"              
print (animales)


#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numero = [7,8,5,4,5] 
numero.remove(max(numero))                                        
print (numero) 

#Lo que sucede es que la funcion remove , saca un elemento de la lista, este caso utiliza "max"que lo que hace es que elimine el elemento mayor(8) y la lista quede igual si el mismo


#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar porpantalla los dos primeros.
list_num = list (range(10,31,5))
print (list_num)
print (list_num[0])
print (list_num[1])


# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valorescualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "for"
autos[2] = "fiesta"
print (autos)


# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.
list_dobles = [] 
list_dobles.append ("10")
list_dobles.append ("20")
list_dobles.append ("30")
print (list_dobles)


# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
# ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
compras[2].append("agua")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)


# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.
lista_anidada = [[15],[True],[25.5, 57.9, 30.6],[False]]
print(lista_anidada)
# lista_anidada.append(15)
# lista_anidada.append(True)
# lista_anidada.append([25.5, 57.9, 30.6])
# lista_anidada.append(False)
# print(lista_anidada)