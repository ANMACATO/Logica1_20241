from random import randrange
saldo=randrange(0,5000000)
print("""---Bienvenido a Bancolombia---:\n
Ingrese la operción bancaria que desea realizar:\n
      1.Consultar saldo
      2.Retirar dinero
      3.Depositar dinero
      4.Transferir
      5.Salir\n""")
opcion=int(input("Seleccione la opción: "))
if opcion==5:
    print("Transacción terminada")
elif opcion==1:
    print("Su saldo disponible es: $",saldo)
elif opcion==2:
    retiro=int(input("Ingres el valor a retirar: "))
    if retiro > saldo:
        print("Saldo insuficiente, su saldo es: $",saldo)
    else:
        saldo-=retiro
        print("Retire su dinero \n Su saldo actual es: $",saldo)
elif opcion==3:
    monto=int(input("Indique el valor a depositar: "))
    saldo+=monto
    print("Su nuevo saldo es: $",saldo)
elif opcion==4:
    cuenta=input("Indique el número de cuenta: ")
    monto=int(input("Indique el monto a tranferir: "))
    if monto>saldo:
        print("¡Fondos insuficientes!\nNo es posible realizar la transferencia...")
    else:
        saldo -=monto
        print("Transferencia exitosa \n Su saldo actual es: $",saldo)
else:
    print("Opción no válida")