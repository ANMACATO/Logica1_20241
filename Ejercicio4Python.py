TipoPlan = int(input(
    "Ingrese el tipo de plan deseado: \n"
    "1. Plan Premium: (20%) de datos adicionales.\n"
    "2. Plan Avanzado: (15%) de datos adicionales.\n"
    "3. Plan Básico: (10%) de datos adicionales.\n"
    "4. Plan Económico: (5%) de datos adicionales.\n"
    "Seleccione el tipo: "))

Plan = 1000*1000000
Costo = 50000
band = 0
if (TipoPlan==1):
    Plan += Plan*0.2
    Costo += Costo*0.1
    text = "Premium,"
elif(TipoPlan==2):
    Plan += Plan*0.15
    Costo += Costo*0.05
    text = "Avanzado,"
elif(TipoPlan==3):
    Plan -= Plan*0.1
    Costo -= Costo*0.1
    text = "Básico,"
elif(TipoPlan==4):
    Plan -= Plan*0.05
    Costo -= Costo*0.2
    text = "Económico,"
else:
    print("Selección equivocada")
    band=1

if (band!=1):
    print("El plan escogido fue el ", text, "con un total de datos igual a: ", Plan/1000000, "Mb y un costo  mensual de: $",Costo)
