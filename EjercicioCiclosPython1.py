Num1 = int(input("Ingrese el primer número: "))
Num2 = int(input("Ingrese el segundo número: "))
# Comparacion numero mayor
if(Num1>=Num2):
    print("El número mayor es: ", Num1)
    Mayor = Num1
    Menor = Num2
else:
    print("El número mayor es: ", Num2)
    Mayor = Num2
    Menor = Num1
# Suma
print("La suma es: ",Num1+Num2)
# Secuencia
contador = Menor
while(contador<=Mayor):
    print(contador)
    contador += 1