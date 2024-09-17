n = int(input("Ingrese el número natural: "))
cont = 1
suma = 0
while(cont<=n):
    if(cont%3==0):
        cont +=1
        continue
    suma += n
    print("Contador = " + str(cont) + " El módulo: " + str(cont%3) + " La suma total: " + str(suma))
    if(suma>=1000):
        break
    cont +=1



