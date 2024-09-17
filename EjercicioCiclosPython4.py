otro = "s"
suma = 0
while(otro=="s"):
    Dato = int(input("Ingrese un número entero: "))
    otro = input("""Desea ingresar otro número?
    teclee s o n para SI o NO
    ingrese respuesta aquí (s/n): """)
    suma+=Dato  

print("La suma es: ", suma)
    

