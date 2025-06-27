#Dado el importe bruto de una compra de libros, el tipo de cliente de que se trata y
#la cantidad total pedida por el mismo, determinar el importe bonificado.
importe = float(input('importe: '))
tipo = input('ingrese tipo persona: ')
cantidad = int(input('cantidad: '))

if tipo == 'P':
  if cantidad < 6:
    print(importe)
  else:
    if cantidad < 18:
      print(importe * 0.95)
    else:
      print(importe * 0.9)
else:
  if cantidad <= 24:
    print(importe * 0.8)
  else:
    print(importe * 0.75)