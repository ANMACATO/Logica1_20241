Temp1 = float(input("Ingrese la temperatura registrada en la mañana: ")) #Temp. mañana
Temp2 = float(input("Ingrese la temperatura registrada en la tarde: ")) #Temp. tarde
Temp3 = float(input("Ingrese la temperatura registrada en la noche: ")) #Temp. noche

if(Temp1>Temp2): #(T1 > T2)
    if(Temp1>Temp3): #(T1 > T2) & (T1 > T3)
        if(Temp2>Temp3): #(T1 > T2) & (T1 > T3) & (T2 > T3) = T1 > T2 > T3
            a,b,c = Temp1,Temp2,Temp3
            j1,j2,j3 = "mañana","tarde","noche"
        else: #(T1 > T2) & (T1 > T3) & (T3 > T2) = T1 > T3 > T2
            a,b,c = Temp1,Temp3,Temp2
            j1,j2,j3 = "mañana","noche","tarde"
    else:  #(T1 > T2) & (T3 > T1) &  = T3 > T1 > T2 
        a,b,c = Temp3,Temp1,Temp2
        j1,j2,j3 = "noche","mañana","tarde"
else: #(T2 > T1)
    if(Temp2>Temp3):#(T2 > T1) & (T2 > T3)
        if(Temp1>Temp3):#(T2 > T1) & (T2 > T3) & (T1 > T3) = T2 > T1 > T3
            a,b,c = Temp2,Temp1,Temp3
            j1,j2,j3 = "tarde","mañana","noche"
        else:#(T2 > T1) & (T2 > T3) & (T3 > T1) = T2 > T3 > T1
            a,b,c = Temp2,Temp3,Temp1
            j1,j2,j3 = "tarde","noche","mañana"
    else:#(T2 > T1) & (T3 > T2) = T3 > T2 > T1 
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
