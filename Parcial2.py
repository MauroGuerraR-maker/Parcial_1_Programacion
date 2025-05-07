#Ingreso del numero de edad
edad=int(input("Introduzca la edad de la persona: "))

#Filtros correspondientes a determinado margen de edad
if 0<=edad<13:
    print("Niño")
if 13<=edad<=17:
    print("Adolescente")
if 18<=edad<=59:
    print("Adulto")
if edad>60:
    print("Adulto mayor")
#Filtro ante posibles entradas negativas
if edad<0:
    print("Error")