import tkinter as tk
from tkinter import messagebox

#def principal():

class TodoApp:
    def __init__(self,root):
        self.root=root
        self.root.title("Listaa Tareas")

        self.tareas=[] #Lista de elementos

        #Entrada de datos para agregar las tareas
        self.entry=tk.Entry(root,width=30)
        self.entry.grid(row=0,column=0,padx=5,pady=5)

        #Boton para agregar Tarea
        self.agregar_boton=tk.Button(root,text="Agregar Tareas",command=self.agregar_tarea)
        self.agregar_boton.grid(row=0,column=1,padx=5,pady=5)

        #Lista para mostrar las tareas
        self.lista_tareas=tk.Listbox(root,width=50)
        self.lista_tareas.grid(row=1,column=0,columnspan=2,padx=5,pady=5)

    def agregar_tarea(self):
        tarea=self.entry.get()#capturar el valor ingresado
        if tarea:
            self.tareas.append(tarea)
            self.actualizar_lista_tareas()
            self.entry.delete(0,tk.END)
            #size=len(tarea)

            #messagebox.askquestion("informacion",size)

    def actualizar_lista_tareas(self):
        self.lista_tareas.delete(0,tk.END)        
        for i,tarea in enumerate(self.tareas,start=1):
            self.lista_tareas.insert(tk.END,f"{i}.{tarea}")





if __name__=="__main__":
    root=tk.Tk()
    app=TodoApp(root)
    root.mainloop()

