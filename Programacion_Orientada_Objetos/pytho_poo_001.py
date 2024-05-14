class Mostro:
    #constructor que me permite definir atributos
    #self reutilizar los atributos(CARACTERISTICA de la clase)
    def __init__(self,nombre,descri,nivel,lugar=None):
        self.nom=nombre
        self.desc=descri
        self.niv=nivel
        self.lug=lugar

    #metodos son el compartiendo que heredan el objeto

    def mostrar_peligrosidad(self):
        if self.niv==1:
            msj="Muy Peligroso"
        elif self.niv==2:
            msj="Peligroso"    
        elif self.niv ==3:
            msj="Se le puede combatir"    
        else:
            msj="Muy Facil de Vencer"    
        return msj    
    
    def __str__(self):
        return f"Este Mostro se llama {self.nom} y tiene un nivel de peligrosidad {self.niv}"


#Objetos
#Instanciando la clase Mostro
obj_dracula=Mostro("Dracula","Vampiro chupa sangre",3,"Transilvania")
obj_fran=Mostro("Frankestein","Mutante de gran altura",2,"Georgia")
obj_mole=Mostro("Mole","Cuerpo en base a rocas",1,"New York")

#print(obj_dracula.__dict__)
#print(obj_dracula.desc)
#print(obj_fran.nom)
#print(obj_mole.niv)
#print(obj_dracula.lug)

#print(obj_dracula.mostrar_peligrosidad())
print(obj_dracula)

