Temp1 = float(input("Ingrese la temperatura registrada en la mañana: ")) #Temp. mañana
Temp2 = float(input("Ingrese la temperatura registrada en la tarde: ")) #Temp. tarde
Temp3 = float(input("Ingrese la temperatura registrada en la noche: ")) #Temp. noche

a,b,c = Temp1,Temp2,Temp3
j1,j2,j3 = "mañana","tarde","noche"
d = 0
if(a>b):
    if(a<c):
        a = Temp3
        c = Temp1
        j1 = "noche"
        j3 = "mañana"
    if(c>b):
        d = b
        b = c
        c = b
        j2 = "noche"
        j3 = "tarde"
else:
    a = Temp2
    b = Temp1
    j1 = "tarde"
    j2 = "mañana"
    if(a<c):
        d = a
        a = c
        c = d
        j1 = "noche"
        j3 = "mañana"
    if(b<c):
        d = b
        b = c
        c = d
        j2 = "noche"
        j3 = "tarde"


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

     
          



     