Texto = input("Ingrese una palabra o texto con 5 caracteres: ")
if(len(Texto)<5):
    print("No se tecleó una palabra de 5 letras")
else:
    if(Texto[0]=="1"):
        print("Se incluye un número 1 en la 1ra letra")
    elif(Texto[1]=="1"):
        print("Se incluye un número 1 en la 2da letra")
    elif(Texto[2]=="1"):
        print("Se incluye un número 1 en la 3ra letra")
    elif(Texto[3]=="1"):
        print("Se incluye un número 1 en la 4ta letra")
    elif(Texto[4]=="1"):
        print("Se incluye un número 1 en la 5ta letra")
    else:
        print("No se tecleó el número 1 en la palabra")