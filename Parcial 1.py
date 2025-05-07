#Entrada  de numeros
num1= int(input("Ingrese un numero: "))
num2= int(input("Ingrese un numero: "))
num3= int(input("Ingrese un numero: "))
num4= int(input("Ingrese un numero: "))
num5= int(input("Ingrese un numero: "))
#Variable donde se sumaran los numeros que cumplan las condiciones
modulo= 0 
#Filtros para numeros pares y positivos
if ((num1%2)==0):  #Filtro numero par
    if num1>0:       #Filtro numero positivo
        modulo += num1
if ((num2%2)==0):
    if num2>0:
        modulo += num2
if ((num3%2)==0):
    if num3>0:
        modulo += num3
if ((num4%2)==0):
    if num4>0:
        modulo += num4
if ((num5%2)==0):
    if num5>0:
        modulo += num5
#Resultado de la operacion
print("La suma de todos los positivos pares es: ",modulo)