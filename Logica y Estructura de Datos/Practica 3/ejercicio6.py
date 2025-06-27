#Hallar la suma de los N primeros números naturales, con N variable y conocido de antemano en cada caso.

suma = 0
for n in range(1, 10):
    suma = suma + n
print(f'la suma de todos los nuemro es: {suma}')