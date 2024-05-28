try:
    num1= int(input("Ingrese Numero uno:"))
    num2= int(input("Ingrese Numero dos:"))
    resultado = num1 / num2
except:    
    print("Error No se puede dividir por cero")
else:#El Siguiente Bloque se ejecutara si existiera una excepcion
    print(f"El Resultado de la division es {resultado} ")    
finally:
    print("Terminado el proceso Correctamente")    