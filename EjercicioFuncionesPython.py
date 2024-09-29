# Ejercicios 1. Subprogramas
# Fácil
# Implementar un subprograma que calcule y muestre la tabla
#  de multiplicar de un número dado por el usuario usando un ciclo. 

def tabla(N1):
    for i in range(11):
        print(f"{N1} * {i} = {N1*i}")
    return

# Moderado
# Implementar una función que determine si un número
#  es primo utilizando un ciclo y comparaciones.
def primo(N1):
    cont=0
    for i in range(1,N1):
        if(N1%i==0):
            cont += 1
    return cont


# Avanzado
# Natural, entero, racional, irracional y real
def sumar(a=0,b=0):
    return a+b

def restar(a=0,b=0):
    return a-b

def multiplicar(a=0,b=0):
    return a*b

def dividir(a=0,b=0):
    if(b==0):
        print("Error: división por cero")
    else:
        return a/b

def modulo(a=0,b=0):
    return a%b

def factorial(a=0):
    acum = 1
    for i in range(1,int(a)+1):
        acum *= i
    return acum

# MAIN
"""
numero=int(input("Ingrese el valor: "))
# LLamado a ejercicio FACIL
tabla(numero)
# Llamado a ejercicio MODERADO
contador=primo(numero)
if(contador<2 and numero!=1):
    print(f"el numero {numero} es primo")
else:
    print(f"el numero {numero} no es primo")
"""
# Llamado a ejercicio DIFICIL
# main
print("""CALCULADORA
      1. suma
      2. resta
      3. multiplicar
      4. dividir
      5. modulo
      6. factorial""")
Selec=int(input("Teclee operación a realizar: "))
if(Selec>6 or Selec<=0):
    print("error")
else:
    n1 = float(input("Ingrese número 1: "))

match(Selec):
    case 1:
        n2 = float(input("Ingrese número 2: "))
        print(f"{n1} + {n2} = {sumar(n1,n2)}")
    case 2:
        n2 = float(input("Ingrese número 2: "))
        print(f"{n1} - {n2} = {restar(n1,n2)}")
    case 3:
        n2 = float(input("Ingrese número 2: "))
        print(f"{n1} * {n2} = {multiplicar(n1,n2)}")
    case 4:
        n2 = float(input("Ingrese número 2: "))
        print(f"{n1} / {n2} = {dividir(n1,n2)}")
    case 5:
        n2 = float(input("Ingrese número 2: "))
        print(f"{n1} % {n2} = {modulo(n1,n2)}")
    case 6:
        print(f"{n1}! = {factorial(n1)}")
    case _:
        print("Dato incorrecto")