empleados_=dict()#constructor
empleados_={}

empleados_ = {
    'codigo':'A102',
    'nombre':'Arturo',
    'apellido':'Flores'
}

print(empleados_['apellido'])
print(empleados_['codigo'])
print(empleados_['nombre'])

claves=empleados_.keys()
valores=empleados_.values()
#print(f"Las claves son {claves}")
#print(f"Los Valores son {valores}")
#print(f"Las claves y valores {empleados_.items()}")

lista_empleados=[
    {'codigo':'A102','nombre':'Arturo','apellido':'Flores'},
    {'codigo':'A103','nombre':'Carlos','apellido':'Flores'},
    {'codigo':'A104','nombre':'Pedro','apellido':'Flores'},
    {'codigo':'A105','nombre':'Maria','apellido':'Flores'},
    {'codigo':'A106','nombre':'Jaime','apellido':'Flores'},
    {'codigo':'A107','nombre':'Charly','apellido':'Flores'},
]

print(lista_empleados[3]["nombre"])

