#Dado un número del 1 al 7 determinar el nombre del día de la semana que le corresponde.
dia_de_la_semana = int(input("escribe un nemero entre 1-7: "))


if dia_de_la_semana==1:
    print("Domingo")
elif dia_de_la_semana==2:
    print("Lunes")
elif dia_de_la_semana==3:
    print("Martes")
elif dia_de_la_semana==4:
    print("Miercoles")
elif dia_de_la_semana==5:
    print("Jueves")
elif dia_de_la_semana==6:
    print("Viernes")
elif dia_de_la_semana==7:
    print("Sabado")
else:
    print("numero invalido, debe estar entre 1 y 7.")