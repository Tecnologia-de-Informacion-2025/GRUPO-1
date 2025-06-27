#Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

n1 = int(input('ingrese un numero: '))
n2 = int(input('ingrese otro numero: '))

for i in range(n1, n2):
    if i%2==0:
        print(f'{i} es par')