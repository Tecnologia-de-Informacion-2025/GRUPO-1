#Dada una cantidad de pesos, una tasa de interés y un número de años, devuelva el monto final a obtener.
#leer
capital_inicial = int(input("ingrese el capital que desee: "))
tasa_de_interes = int(input("cual es la tasa de interes por año?: "))
años = int(input("a cuantos años quiere que sea el plazo fijo?: "))

#asignar
plazo_fijo = capital_inicial*(1+tasa_de_interes/100)**años

#escribir
print(plazo_fijo)