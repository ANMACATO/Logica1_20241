Temp1 = float(input("Ingrese la temperatura registrada en la mañana: ")) #Temp. mañana
Temp2 = float(input("Ingrese la temperatura registrada en la tarde: ")) #Temp. tarde
Temp3 = float(input("Ingrese la temperatura registrada en la noche: ")) #Temp. noche

if(Temp1>Temp2):
    if(Temp1>Temp3):
        if(Temp2>Temp3):
            a,b,c = Temp1,Temp2,Temp3
            j1,j2,j3 = "mañana","tarde","noche"
        else:
            a,b,c = Temp1,Temp3,Temp2
            j1,j2,j3 = "mañana","noche","tarde"
    else: 
        if(Temp1>Temp2):
            a,b,c = Temp3,Temp1,Temp2
            j1,j2,j3 = "noche","mañana","tarde"
        else:
            a,b,c = Temp3,Temp2,Temp1
            j1,j2,j3 = "noche","tarde","mañana"
else:
    if(Temp2>Temp3):
        if(Temp1>Temp3):
            a,b,c = Temp2,Temp1,Temp3
            j1,j2,j3 = "tarde","mañana","noche"
        else:
            a,b,c = Temp2,Temp3,Temp1
            j1,j2,j3 = "tarde","noche","mañana"
    else:
        if(Temp1>Temp2):
            a,b,c = Temp3,Temp1,Temp2
            j1,j2,j3 = "noche","mañana","tarde"
        else:
            a,b,c = Temp3,Temp2,Temp1
            j1,j2,j3 = "noche","tarde","mañana"

print("La temperatura más alta se dió en la",j1,"con un  valor de",a,"° luego en la",j2,"con una temperatura igual a",b, "° y finalmente en la ",j3,"con una temperatura igual a",c,"°")

#Detectar si es par#
if(a%2==0):
    print("La temperatura de la",j1,"es par")
else:
    print("La temperatura de la",j1,"es impar")
if(b%2==0):
    print("La temperatura de la",j2,"es par")
else:
    print("La temperatura de la",j2,"es impar")
if(c%2==0):
    print("La temperatura de la",j3,"es par")
else:
    print("La temperatura de la",j3,"es impar")            
