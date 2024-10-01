# Función
def raiz(a,b,c):
    x1=(-b+pow(b**2-4*a*c,0.5))/(2*a)
    x2=(-b-pow(b**2-4*a*c,0.5))/(2*a)
    return x1,x2

# Main
a=int(input("Ingrese el valor de a: "))
b=int(input("Ingrese el valor de b: "))
c=int(input("Ingrese el valor de c: "))
x1,x2=raiz(a,b,c)
print(f"Las raices son: {x1:.2} y {x2:.2}") #limita a dos decimales
