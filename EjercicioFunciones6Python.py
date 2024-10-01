def factorial(n):
    if(n==0):
        fact = 1
    else:
        fact = n*factorial(n-1)
    return fact


num = int(input("Ingrese el valor: "))
resu=factorial(num)
print(f"El factorial de {num} es {resu}")