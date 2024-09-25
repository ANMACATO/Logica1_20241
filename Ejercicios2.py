# Ejercicios 2
# Facil: 
"""for i in range(100,0,-1):
    print(i) # 

# Moderado
Positivos=0;
Negativos=0;
Ceros=0;
n = int(input("Ingrese la totalidad de números: "))
for i in range(n):
    num = float(input("Ingrese el número: "))
    if(num>0): # identifica si el número es par
        Positivos += 1
    elif(num<0):
        Negativos += 1
    else:
        Ceros += 1

print("Los números positivos fueron: ",Positivos)
print("El número es negativos fueron: ",Negativos)
print("El número es ceros fueron: ",Ceros)
"""
# Complejo
# Adivinar un número aleatorio
import random # librería para generar números aleatorios
numero_secreto = random.randint(1, 100)
adivino = True
Pares = 0
Impares = 0
for i in range(10):
    num = int(input("Intento número: " +str(i+1) + ". Ingrese el número a adivinar: "))
    if(num%2==0):
        Pares +=1
    else:
        Impares +=1
    if(num>numero_secreto):
        print("Tecleaste un número mayor al que debes adivinar")
    if(num<numero_secreto):
        print("Tecleaste un número menor al que debes adivinar")
    if(num==numero_secreto):
        print("¡Le atinaste! \n el número secreto era: ", numero_secreto)
        break
print("Los números pares ingresados fueron: ", Pares)
print("Los números impares ingresados fueron: ", Impares)