#Ingresar cinco notas de exámenes y mostrar el promedio

suam_de_notas = 0

for i in range(1, 6):
    nota = float(input('ingrese la nota del examen: '))
    suam_de_notas = suam_de_notas + nota

print(suam_de_notas/5)