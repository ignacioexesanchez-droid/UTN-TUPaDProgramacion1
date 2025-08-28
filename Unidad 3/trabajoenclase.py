# Ejercicio en clase (condicional)
fecha = input("Ingrese una fecha en formato 'día, DD/MM': ")
dia_semana, num_fecha = fecha.split(",") 
dia_semana = dia_semana.strip().lower() 
dia, mes = num_fecha.strip().split("/")
dia = int(dia)
mes = int(mes)
if dia < 1 or dia > 31 or mes < 1 or mes > 12:
    print("Error: la fecha ingresada no es válida.")
    exit()
if dia_semana == "lunes":
    nivel = "inicial"
elif dia_semana == "martes":
    nivel = "intermedio"
elif dia_semana == "miercoles":
    nivel = "avanzado"
elif dia_semana == "jueves":
    nivel = "práctica hablada"
elif dia_semana == "viernes":
    nivel = "ingles para viajeros"
else:
    print("Error: el día de la semana no es válido.")
    exit()

if nivel in ["inicial", "intermedio", "avanzado"]:
    examenes = input("¿Se tomaron exámenes? (si/no): ").lower()
    if examenes == "si":
        aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
        desaprobados = int(input("Ingrese la cantidad de alumnos no aprobados: "))
        total = aprobados + desaprobados
        if total > 0:
            porcentaje = (aprobados / total) * 100
            print(f"Porcentaje de aprobados: {porcentaje:.2f}%")
        else:
            print("No hubo alumnos cargados.")
    else:
        print("No se tomaron exámenes.")
elif nivel == "práctica hablada":
    asistencia = float(input("Ingrese el porcentaje de asistencia (%): "))
    if asistencia > 50:
        print("Asistió la mayoría.")
    else:
        print("No asistió la mayoría.")

elif nivel == "ingles para viajeros":
    if dia == 1 and (mes == 1 or mes == 7):
        print("Comienzo de nuevo ciclo.")
        alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
        arancel = float(input("Ingrese el arancel por alumno ($): "))
        ingreso_total = alumnos * arancel
        print(f"Ingreso total: ${ingreso_total}")
    else:
        print("Clase de inglés para viajeros (sin novedades especiales).")