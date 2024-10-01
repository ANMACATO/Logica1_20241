# FACIL
def llamadasmenos3(minutos):
    costeo = minutos * 1000
    return costeo

# Intermedio (Incluye la función anterior)   
def llamadasmas3(minutos):
    costeo = minutos * 200
    return costeo

def llamadasmas3Inal(minutos):
    costeo = minutos * 300
    return costeo

# MAIN
Valt = 0
min = int(input("Ingrese cantidad de minutos consumidos: "))
print("""Ingrese tipo de llamada:
      1. Nacional
      2. Internacional""")
Tipollamada = int(input("Tecle la opción (1 o 2): "))

match(Tipollamada):
    case 1:
        if(min<3):
            Valt += llamadasmenos3(min)
        else:
            Valt += llamadasmenos3(2) + llamadasmas3(min-2)
    case 2:
        if(min<3):
            Valt += llamadasmenos3(min)
        else:
            Valt += llamadasmenos3(2) + llamadasmas3Inal(min-2)
if(Tipollamada==1):
    print("Hizo una llamada nacional de {} minutos, para un costo total de {} pesos".format(min,Valt))
else:
    print("Hizo una llamada Internacional de {} minutos, para un costo total de {} pesos".format(min,Valt))