import tkinter as tk

def imprimir_mensaje():
    print("Hola Mundo")

#Crear una ventana

root=tk.Tk()
root.title("MI VENTANA")

#Crear un Widget Boton
boton=tk.Button(root,text="Haz Click",command=imprimir_mensaje)
boton.pack()

#Mostrar la ventana
root.mainloop()
