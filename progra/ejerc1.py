nombre_apellido= str (input("ingrese nombre y apellido"))
edad = int(input("ingrese edad "))
ingresos = int (input("ingrese ingresos familiares mensuales"))
while True:
    promedio = float(input("ingrese promedio 0 a 10"))
    if promedio > 6:
       print ("aceptado")
    else:
        print ("rechazado") 
    break
print (nombre_apellido, edad, "años" )
if ingresos < 300.000:
    print ("beca completa")
elif ingresos<= 600000:
 print("media beca")
else:
 print("rechazado") 
#o	Si los ingresos familiares < $300.000 → beca completa.Si los ingresos entre $300.000 y $600.000 → media beca.Si los ingresos > $600.000 → rechazado.
