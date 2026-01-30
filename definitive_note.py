# Programa para Calcular la Nota Definitiva de una asignatura

#---------------------------------------------------------
# LIBRERIAS
#---------------------------------------------------------
import math

print("-------------------------------------------------")
print("Nota Definitiva de una asignatura")
print("-------------------------------------------------")

#---------------------------------------------------------
# INPUT
#---------------------------------------------------------

nc=int(input("Digite el valor del la Nota Cognitiva: "))
np=int(input("Digite el valor del la Nota Procedimental: "))
na=int(input("Digite el valor del la Nota Actitudinal: "))
au=int(input("Digite el valor del la Autoevaluacion: "))
bi=int(input("Digite el valor del la Nota Bimestral: "))

#---------------------------------------------------------
# PROCESSING
#---------------------------------------------------------

nd=0.3*nc+0.3*np+0.1*na+0.1*au+0.2*bi

#---------------------------------------------------------
# OUTPUT
#---------------------------------------------------------

print("-------------------------------------------------")
print("-------------------Resultado---------------------")
print("-------------------------------------------------")
print("El valor de la Nota Definitiva de la Asignatura es:"+str(nd))
print("-------------------------------------------------")