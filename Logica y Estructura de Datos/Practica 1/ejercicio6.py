#Determinar el número de horas, minutos y segundos que hay en 6250 segundos.
#asignar
horas = 6250 // 3600
minutos = (6250 % 3600) // 60
segundos = (6250 % 3600) % 60

#escribir
print(f"hay {horas} horas, {minutos} minutos y {segundos} segundos")