#Convierta un valor dado en grados Fahrenheit a grados Celsius.
#Recordar que la fórmula para la conversión es: F = 9/5 * C + 32
#leer
grados_fahrenheit = int(input("ingrese los grados en fahrenheit: "))

#asignar
grados_celsius = (grados_fahrenheit - 32)* 5/9

#escribir
print(f"grados celsius {grados_celsius}")