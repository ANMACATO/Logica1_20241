Salario = float(input('Ingrese el salario del trabajador: '))
Edad = int(input('Ingrese la edad del trabajador: '))
Anos = int(input('Ingrese los años trabajando en la empresa: '))
ValTot = Salario

if(Salario<=2000000):
    ValTot += ValTot*(0.2)
    print(ValTot)
else:
    ValTot += ValTot*(0.1)
    print(ValTot)
if (Edad>=40):
    ValTot += (Edad-40)*50000
    print(ValTot)
ValTot += (Edad/5)*5000
if (Edad>=55 and Anos>=15):
    ValTot += (Anos*200000)
    print(Anos*200000)
print("El salario del trabajador será: ", ValTot)
