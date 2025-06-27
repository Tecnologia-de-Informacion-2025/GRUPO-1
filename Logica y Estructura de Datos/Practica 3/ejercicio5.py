#Ingresar 10 números por teclado y determinar la cantidad de pares.

cantidad_pares = 0
for i in range(1, 10):
    numero = int(input('ingrese un numero: '))
    if numero%2==0:
        cantidad_pares = cantidad_pares+1
print(cantidad_pares)