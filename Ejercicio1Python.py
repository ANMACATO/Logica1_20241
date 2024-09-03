band = 0
Val = int(input("Ingrese la cantidad de personas: "))
print("Hay menores de edad en el grupo de personas?: ")
Men = input("Responda si o no: ")
if (Val>10):
    band=1
if (Men=='si'):
    ValMen = int(input('Ingrese la cantidad de menores: '))
    Val -= ValMen
    ValMen *= 8000
    ValAd = Val * 17000
else:
    ValAd = Val * 17000
    ValMen = 0
Valtot = ValAd + ValMen
print("\n-FACTURA-","\nMenores: ",ValMen, "\nAdultos: ", ValAd)
if(band==1):
    print("Valor total: ", Valtot)
    print("Descuento 10% : ", (ValAd + ValMen)*0.1)
    Valtot -=Valtot*0.1
print("El valor a pagar es: ",Valtot)