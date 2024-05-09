import datetime #modulo
"""
Tipos de datos Primitivos
- numericos : INT,FLOAT
- cadena: STR
- bool : True,False
- Colecciones : listas [],diccionarios{k,v},tuplas (),set {v}
"""

fecha_actual= datetime.datetime.now()
fecha_actual_solo_fecha=fecha_actual.date()

#print(f"Fecha y Hora actual: {fecha_actual}")
#print(f"Solo la Fecha : {fecha_actual_solo_fecha}")

#Operadoes Matematicos

"""
Operadores de suma, resta, multiplicación y división:
Suma: +
Ejemplo: a + b

Resta: -
Ejemplo: a - b

Multiplicación: *
Ejemplo: a * b

División: /
Ejemplo: a / b

División entera: //
Ejemplo: a // b (Devuelve el cociente entero de la división)

Módulo: %
Ejemplo: a % b (Devuelve el residuo de la división)

"""

resultado = 28//7
#print(f"El Resultado es {resultado}")

lista_pares=[]
lista_impares=list() #constructor
while True:
    numero=int(input("Ingrese el numero a averiguar:"))
    #print(type(numero))
    if numero % 2 ==0:
        print("EL Numero es Par") #Ver
        lista_pares.append(numero)
    else:
        print("EL Numero es ImPar") #False
        lista_impares.append(numero)
    resp=input("Desea Continuar:")
    if resp=="n":
        print(f"Lista de Pares {lista_pares}")
        print(f"Lista de Impares {lista_impares}")
        break







numeros= [12,14,56,78]
numeros.append(12)











