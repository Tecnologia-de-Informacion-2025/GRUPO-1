#Se leen tres números que son las longitudes de los lados de un triángulo. Determinar e informar 
#si el mismo es equilátero (3 lados iguales), isósceles (2 lados iguales) o escaleno (3 lados distintos).
L1 = int(input("escribi cuanto mide el lado de un triangulo: "))
L2 = int(input("escribi cuanto mide el segundo lado de un triangulo: "))
L3 = int(input("escribir cuanto mide el tercer lado de un triangulo: "))

if L1==L2:
    if L1==L3:
        print("Es un triangulo equilatero")
    else:
        print("Es un triangulo isósceles")
else:
    if L1==L3:
        print("Es un triangulo isósceles")
    else:
        if L2==L3:
            print("Es un trinagulo isósceles")
        else:
            print("Es un triangulo escaleno")