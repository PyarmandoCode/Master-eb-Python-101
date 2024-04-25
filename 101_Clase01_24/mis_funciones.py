def acceso_sistemas(user,pas):
    usuario=input("Ingrese el usuario:")
    passw=input("Ingrese el Password:")
    if usuario ==user and passw ==pas:
        msg="Bienvenido al Sistema"
    else:
        msg="Usuario o clave incorrecta"
    return msg    

