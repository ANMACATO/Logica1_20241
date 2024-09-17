# Desarrollar un programa que genere un número aleatorio entre 1 y 100.
# El usuario tiene que ingresar un número y el algoritmo debe guiar al
# usuario diciendo la cercanía al número (mayor, menor, igual al número generado). 
# El ciclo se repite hasta que el usuario acierte.

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








