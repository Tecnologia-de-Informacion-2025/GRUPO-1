#Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) 
#y la vuelva a solicitar hasta que las dos contraseñas coincidan, con un límite de tres peticiones.
contraseña = 'd.r202025'
c = input('ingrese su contraseña: ')
intentos = 3

while(contraseña != c and intentos > 1):
    c = input('ingrese su contraseña: ')
    intentos = intentos - 1
    
if (contraseña != c):
    print('usuario bloqueado')
else:
    print('login successful')