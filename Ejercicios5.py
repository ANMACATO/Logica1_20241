n = int(input("Ingrese la cantidad de estudiantes: "))
Nota30a = 0
Nota40 = 0
Nota30b = 0
Notas = " | "
Nombres = " | "
Estado = " | "
for i in range(n):
    cont = 1
    Nombre = input("Ingrese el nombre del estudiante: ")
    while(cont<3):
        Nota = float(input("Ingrese nota " + str(cont) + " del primer corte (30%): "))
        Nota30a += Nota
        cont +=1
    cont = 1
    while(cont<3):
        Nota = float(input("Ingrese nota " + str(cont) + " del segundo corte (40%): "))
        Nota40 += Nota
        cont +=1
    cont = 1
    while(cont<3):
        Nota = float(input("Ingrese nota " + str(cont) + " del tercer corte (30%): "))
        Nota30b += Nota
        cont +=1
    Nota30a = Nota30a/2;
    Nota30b = Nota30b/2;
    Nota40 = Nota40/2;
    Nota = Nota30a*0.3 + Nota40*0.4 + Nota30b*0.3
    print("ESTUDIANTE: ", Nombre)
    print("NOTA DEFINITIVA: ", Nota)
    if(Nota>=3):
        print("GANA")
    elif (Nota>=2.5 and Nota<3):
        print("HABILITA")
    else: 
        print("PIERDE")