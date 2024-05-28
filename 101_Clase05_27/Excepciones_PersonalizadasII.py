"""
assert es una palabra clave para realizar afirmaciones o comprobaciones de 
condiciones
sintaxis:
- assert expresion , mensaje_de_error
"""

try:
    edad = int(input("Ingrese la edad:"))
    assert edad>=0, "Error:la edad tiene un formato invalido"
    print(f"edad ingresada correctamente {edad}")
except (ValueError,AssertionError) as e:
    print(f"{e}")   
