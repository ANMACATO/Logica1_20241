N1 = float(input("Ingrese el primer número: "))
N2 = float(input("Ingrese el segundo número: "))
Operacion = input("""Ingrese la operación:
                  + para suma
                  - para resta
                  x para multiplicar 
                  / para dividir
                  """)
if (Operacion=="+"):
    Resultado = N1 + N2
elif (Operacion=="-"):
    Resultado = N1 - N2
elif (Operacion=="x"): 
    Resultado = N1 * N2
elif (Operacion=="/"): 
    Resultado = N1 / N2
else:
    print("Error - Operación no permitida -")

print(N1,Operacion,N2," = ",Resultado)