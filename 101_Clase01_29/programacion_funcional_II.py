"""
Crear un Programa que solicite al usario ingresar valores
hasta que se ingrese 0.
-Calcular el promedio de los valores ingresados
-Cuantos Numeros se Ingresaron
"""
#Inicializar una lista vacia para almacenar valores ingresados
valores =[]
#Pedir al usuario que ingrese valores hasta que ingrese 0

def calcular_promedio(lista):
    if lista:
        promedio = sum(lista)/len(lista)
    else:
        promedio=0
    return promedio

valor=float(input("Ingrese un Numero (Ingrese 0 Para Terminar):"))
while valor !=0:
    valores.append(valor) #Agregar Valores a la lista
    valor=float(input("Ingrese un Numero (Ingrese 0 Para Terminar):"))

#calcular el promedio de los valores
promedio=calcular_promedio(valores)

cantidad_numeros=len(valores)
print(f"El Promedio de los valores Ingresados es {promedio}")        
print(f"Se Ingresaron  {cantidad_numeros}")


    

    


