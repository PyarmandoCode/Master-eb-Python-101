from datetime import datetime,timedelta

print(f"La Fecha Actual del sistema {datetime.now()}")
fecha_actual=datetime.now()
#año=fecha_actual.year
#mes=fecha_actual.month
#dia=fecha_actual.day
#hora=fecha_actual.hour

#Operaciones entre fecha
#nueva_fecha=fecha_actual+timedelta(days=7)
#print(nueva_fecha)

#fecha1=datetime(2022,5,10)
#fecha2=datetime(2022,3,15)
#diferencia_entre_fecha=fecha1-fecha2
#print(f"diferencia entre fechas {diferencia_entre_fecha}")


fecha_actual=datetime.now()
numero_mes=fecha_actual.month #5
#print(f"Numero de mes {numero_mes}")

def nombre_mes(numero):#Creando funcion
    match numero:
        case 1:
            return "Enero"
        case 2:
            return "Febrero"
        case 3:
            return "Marzo"
        case 4:
            return "Abril"
        case 5:
            return "Mayo"
        case _:
            return "Opcion no valida"

#print(nombre_mes(numero_mes))

import calendar
nombre_mes=calendar.month_name[numero_mes]
print(f"El Nombre del mes es {nombre_mes} ")