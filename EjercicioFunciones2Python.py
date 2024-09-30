# Declaración de funciones
# FACIL
# Desarrolle una función que calcule devuelva el número menor entre dos números.
"""
def menor(n1,n2):
    if(n1<=n2):
        men = n1
    else:
        men = n2
    return men

# MODERADO
# Desarrolle una función que calcule la temperatura media de un registro mensual por un año.
def Temp_Media(meses):
    acum = 0
    for i in range(meses):
        tempmensual = float(input(f"Ingrese la temperatura del mes {i+1}: "))
        acum += tempmensual
    acum = acum / meses
    return acum
"""
# AVANZADO
# Cree un algoritmo que calcule la temperatura media, mínima y máxima 
# de un registro de datos ingresados por el usuario. 
def Temp_MMM(meses):
    maxima = -1000
    minima = 1000
    acum = 0
    for i in range(meses):
        tempmensual = float(input(f"Ingrese la temperatura del mes {i+1}: ")) 
        if(tempmensual>maxima):
            maxima = tempmensual
        if(tempmensual<minima):
            minima = tempmensual
        print(maxima,minima)
        acum += tempmensual
    acum = acum / meses
    return acum, maxima, minima


# MAIN
"""
# Fácil
Num1 = float(input("Ingrese número 1: "))
Num2 = float(input("Ingrese número 2: "))
men=menor(Num1,Num2)
print("El número menor entre {} y {} es {}".format(Num1,Num2,men))

# Moderado
months=int(input("Ingrese los meses que registró  temperatura: "))
TepMedia = Temp_Media(months)
print(f"Durante los {months} se registró una temperatura media de {TepMedia}°C")
"""
#Avanzado
months=int(input("Ingrese los meses que registró  temperatura: "))
TepMedia, maxima, minima = Temp_MMM(months)
print(f"Durante los {months} se registró una temperatura media de {TepMedia}°C, una máxima de {maxima}°C y una mínima de {minima}°C")