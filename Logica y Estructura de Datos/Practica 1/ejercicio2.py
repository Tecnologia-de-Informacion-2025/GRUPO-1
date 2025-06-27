#Dado como dato el valor del lado de un cuadrado calcular su perímetro y su superficie, e informar los mismos con carteles aclaratorios.
#leer
lado = int(input("ingrese el valor del lado de su cuadrado: "))

#asignar
perimtetro = lado*4
area = lado*lado

#escribir
print(f"el perimetro del cuadrado es: {perimtetro}, y su area es: {area}")
