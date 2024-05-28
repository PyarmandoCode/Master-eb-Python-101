def excepcion_ejemplo01():
    try:
        num1= int(input("Ingrese Numero uno:"))
        num2= int(input("Ingrese Numero dos:"))
        resultado = num1 / num2
    except Exception as err:    
        print(f"Se produjo el siguiente error  {err}")
    else:#El Siguiente Bloque se ejecutara si existiera una excepcion
        print(f"El Resultado de la division es {resultado} ")    
    finally:
        print("Terminado el proceso Correctamente") 

"""
Tipos Comunes de Excepciones
Python tiene varios tipos integrados de excepciones:
- ZeroDivisionError: Ocurre cuando se intenta dividir por cero.
- ValueError: Ocurre cuando una función recibe un argumento de tipo correcto pero con un valor inapropiado.
- FileNotFoundError: Ocurre cuando un archivo o directorio no puede ser encontrado
- IndexError: Ocurre cuando se intenta acceder a un índice que está fuera del rango de una lista o tupla.
- KeyError: Ocurre cuando se intenta acceder a una clave que no existe en un diccionario.
"""            
def excepcion_zerodivisionerror():
    try:
        num1= int(input("Ingrese Numero uno:"))
        num2= int(input("Ingrese Numero dos:"))
        resultado = num1 / num2
    except ZeroDivisionError:    
        print("No se puede dividir por cero")
    else:#El Siguiente Bloque se ejecutara si existiera una excepcion
        print(f"El Resultado de la division es {resultado} ")    
    finally:
        print("Terminado el proceso Correctamente") 

def excepcion_valueerror():
    try:
        num1 = int(input("Ingrese Numero uno:"))
        num2 = int(input("Ingrese Numero dos:"))
    except ValueError:
        print("Valor Ingresado No Valido")    
    else:
        res=num1+num2
        print(f"El resultado es {res}")    
    finally:
        print("Terminado el Proceso Correctamente")    


mi_lista=["Colombia","Paraguay","Chile"] 
def excepcion_indexerror(lista,indice):
    try:
        elemento=lista[indice]
        print(f"Elemento en el indice {indice}:{elemento}")
    except IndexError:
        print(f"Error:Indice {indice} esta fuera del rango de la lista")    
    except Exception:
        print("Ocurrio un Error")        
    finally:
        print("Terminado el Proceso Correctamente")    


indice=input("Ingrese el indice:")
excepcion_indexerror(mi_lista,indice)    