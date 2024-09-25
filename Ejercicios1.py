# Ejercicios
# Facil
for i in range(10):
    print(i+1) # Se suma 1 porque el for inicia en 0 y termina en 9
# Moderado
acumulador = 0
n = int(input("Ingrese el rango: "))
for i in range(n):
    if(i%2==0): # identifica si el número es par
        acumulador += i # acumula la suma
print("la suma es", acumulador)
# Complejo
# un número primo solo es divisible por el y por el 1.
contador = 0
num = int(input("Ingrese numero: "))
for i in range(1,num+1):
    if(num%i==0):
        contador += 1
if(contador<=2 and num>1):
    print("El número es primo")
else:
    print("El número no es primo")

    