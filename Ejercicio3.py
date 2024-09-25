# Ejercicio 3
# Facil: tabla del 2

for i in range(11):
    print(2*i)

# Moderado: tablas de multiplicar del 1 al 10
for i in range(1,11):
    print("Tabla del ",i)
    for j in range(1,11):
        print(i," * ",j," = ",i*j)


# Dificil: clasificador
contador=1
op1=0 # mujeres
op2=0 # hombres
op3=0 # mayores
op4=0 # menores
op5=0 # hombres mayores de edad
op6=0 # hombres menores de edad
op7=0 # mujeres menores de edad
op8=0 # mujeres mayores de edad
while(contador<=5):
    edad = int(input("Ingrese la edad de la persona número " + str(contador) + ": "))
    genero = input("Ingrese el genero (M/F) de la persona número " + str(contador) + ": ")
    if(edad>=18):# mayores
        op3 += 1
        if(genero=="m" or genero=="M"): #hombres mayores de edad
            op5 += 1
        else:# mujeres mayores de edad
            op8 += 1
    else:# menores
        op4 += 1
        if(genero=="f" or genero=="F"): #mujeres menores de edad
            op7 += 1
        else:# hobres menores de edad
            op6 += 1
    contador +=1
op1 = op8 + op7 #mujeres
op2 = op5 + op6 #hombres
print("Mujeres mayores de edad", op8)
print("Mujeres menores de edad", op7)
print("Hombres mayores de edad", op5)
print("Hombres menores de edad", op6)
print("Total Mujeres: ", op1)
print("Total Hombres: ", op2)
print("Total menores de edad: ", op4)
print("Total mayores de edad: ", op3)



