import math
def promedio(datos):
    suma=0
    for i in range(len(datos)):
        suma+=datos[i]
    prom=suma/len(datos)
    return prom
def desviacionestandar(datos):
    suma=0
    prom=promedio(datos)
    for i in range(len(datos)):
        suma+=(datos[i]-prom)**2
    desv = math.sqrt (suma/(len(datos)-1))
    return desv

datos=[0]*10
for i in range (len(datos)):
    datos[i]=float(input())

print("El promedio es ",promedio(datos))
print("La desviacion estandar es ", desviacionestandar(datos))