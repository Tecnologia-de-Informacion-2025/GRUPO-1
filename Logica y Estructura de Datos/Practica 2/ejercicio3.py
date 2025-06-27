#Ingresar 3 letras mayúsculas y mostrarlas ordenadas alfabéticamente.
letra1 = input("escribe una letra en mayuscula: ")
letra2 = input("escribe una letra en mayuscula: ")
letra3 = input("escribe una letra en mayuscula: ")

if letra1 > letra2:
    if letra1 > letra3:
        if letra2 > letra3:
            print(letra3, letra2, letra1)
        else:
            print(letra2, letra3, letra1)
    else:
        print(letra2, letra1, letra3)
else:
    if letra1 > letra3:
        print(letra3, letra1, letra2)
    else:
        if letra2 > letra3:
            print(letra1, letra3, letra2)
        else:
            print(letra1, letra2, letra3)