#Solución con un acumulador

suma = 0 

for i in range(1, 5):
    numero = int(input('ingrese un nuemro: '))
    suma = suma + numero

print(f'la suma es {suma}')