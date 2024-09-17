"""
# Opción 1 : 
continuar = "s"
Promedio = cont = 0

while(continuar=="s"):
    cont+=1
    print("Ingrese la nota para el estudiante número: ", cont)
    Nota = float(input("Nota: "))
    Promedio += Nota
    continuar = input("Desea ingresar otro estudiante? \nTeclee ""s"" para si y ""n"" para no: ")

print("El promedio de notas para el grupo es: ",Promedio/cont)
   
"""
continuar = True
Promedio = cont = 0
while (continuar):
    cont+=1
    print("Ingrese la nota para el estudiante número: ", cont)
    Nota = float(input("Nota: "))
    Promedio += Nota
    continuar = input("Desea ingresar otro estudiante? \nTeclee ""s"" para si y ""n"" para no: ")
    if(continuar=="n"):
        continuar=False
        
print("El promedio de notas para el grupo es: ",Promedio/cont)
    
