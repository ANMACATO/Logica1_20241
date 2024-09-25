# Ejercicio 4
# Facil

palabra = "hola mundo"
cont = len(palabra) # longitud de la palabra
for i in range(cont):
    print(palabra[i],palabra[cont-1])
    cont -=1

# Moderado
# Ventas con descuento
ventas=descuento=0
cant=0
while(True):
    venta=int(input("Ingresar el total de la compra: "))
    ventas += venta
    if(venta>100000):
        descuento += venta*0.1
    if(descuento>500000):
        break

print("Ventas del día, sin aplicar descuento: ", ventas)
print("Total en descuentos: ", descuento)
print("Ventas del día, aplicando descuento: ", ventas-descuento)

# Complejo
# Librería para generación de números aleatorios
import random  
# Generación de número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

adivino = True

while(adivino):
    Numero = int(input("Ingrese un número entre 1 y 100 para ver si adivinas: "))
    if(Numero<numero_secreto):
        print("Tecleaste un número menor al que debes adivinar...")
    elif(Numero>numero_secreto):
        print("Tecleaste un número mayor al que debes adivinar...")
    else:
        print("¡Le atinaste! \n el número secreto era: ", numero_secreto)
        adivino = False