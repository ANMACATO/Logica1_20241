Origen = int(input("""Ingrese el origen en el AMVA:
                1. Barbosa. 
                2. Girardota.
                3. Copacabana.
                4. Bello.
                5. Medellín.
                6. Itagüí.
                7. Envigado.
                8. Sabaneta.
                9. La estrella.
                10. Caldas.
                Teclee el número correspondiente al origen: """))
Destino = int(input("""Ingrese el destino en el AMVA:
                1. Barbosa. 
                2. Girardota.
                3. Copacabana.
                4. Bello.
                5. Medellín.
                6. Itagüí.
                7. Envigado.
                8. Sabaneta.
                9. La estrella.
                10. Caldas.
                Teclee el número correspondiente al destino: """))
Tiempo = int(input("Ingrese el tiempo que ha destinado para el viaje en minutos: "))
Dinero = int(input("Ingrese el dinero disponible para el viaje: "))
Condicion = int(input("""Ingrese si tiene alguna condición especial para transportarse:
    1. No tiene alguna necesidad especial.
    2. Transporte ecológico.
    3. Necesidad de accesibilidad
    Teclee el número correspondiente a la condición: """))

DistReco = Destino - Origen
if(DistReco<0):
    DistReco = -DistReco
if(DistReco<=3):
    Band = 1 # Recorrido corto
elif (DistReco>3 and DistReco<=6):
    Band = 2 # Recorrido medio
else:
    Band = 3 # Recorrido largo

match (Band):
    case 1:#Recorridos cortos
            if (Tiempo>120 and Dinero<=5000): #Autobus
                 print("Se recomienda tomar el autobus")
            elif (Dinero>20000 and Tiempo<=60): #Taxi
                 print("Se recomienda tomar un taxi")
            elif (Dinero<=5000 and Tiempo>60 and Tiempo<=120): #Bicicleta
                 print("Se recomienda ir en bicicleta")
            elif (Tiempo>120 and Dinero==0): #Caminando
                 print("Se recomienda ir caminando")                 
            else:
                 print("Tome cualquier opción")                 

    case 2: #Recorridos medios
        if (Tiempo>120 and Dinero<=5000):
            print("Se recomienda tomar el autobus")
        elif (Tiempo<40 and Dinero>5000 and Dinero<=20000 and Condicion == 2 or Condicion == 3):
             print("Se recomienda tomar el metro")
        else:
             print("Tome cualquier opción")                 
                
    case 3: #Recorridos largos
          if (Tiempo>120 and Dinero<=5000):
               print("Se recomienda tomar el autobus")
          elif (Tiempo<40 and Dinero>5000 and Dinero<=20000 and Condicion == 2 or Condicion == 3):
               print("Se recomienda tomar el metro")
          else:
                 print("Tome cualquier opción")
    case _:
          print("Caso imposible")





