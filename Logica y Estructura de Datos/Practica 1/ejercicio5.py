#Calcular el sueldo de un operario conociendo la cantidad de horas que trabajó en el mes y lo que gana por hora.
#leer
horas_de_trabajo = int(input("cuantas horas trabajo este mes?: "))
sueldo_por_hora = int(input("cuanto cobra por hora?: "))

#asignar
sueldo_del_mes = horas_de_trabajo*sueldo_por_hora

#escribir
print(f"el sueldo que cobrara este mes es {sueldo_del_mes}")