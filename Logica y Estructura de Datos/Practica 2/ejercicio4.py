#Dado un año indicar si es bisiesto.
año = int(input("ingrese un año: "))

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print(f"el año {año} es bisiesto")
        else:
            print(f"le año {año} no es bisiesto")
    else:
        print(f"el año {año} se bisiesto")
else:
    print(f"el año {año} no es bisiesto")

#otra forma mas sensilla
    
#if año % 4==0 or año % 100==0 and año % 400==0:
#    print(f"el año {año} es bisiesto")
#else:
#    print(f"el año {año} no es bisiesto")
