#Si un alumno obtiene una nota promedio mayor o igual a 60 y su porcentaje de asistencia es mayor o igual a 75, 
#su condición final es regular, sino libre.
nota = float(input("ingrese el porcentaje de la nota: "))
asistencia = float(input("ingrese el porcentajme de asistencia: "))

if nota>=60:
    if asistencia>=75:
        print("Regular")
    else:
        print("Libre")
else:
    print("Libre")