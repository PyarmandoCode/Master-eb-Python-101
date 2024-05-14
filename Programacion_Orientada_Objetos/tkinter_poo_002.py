import tkinter as tk
import tkinter as ttk

class EtiquetaPersonalizada(tk.Label):
    def __init__(self,master=None,**kwargs):
        self.bg_color=kwargs.pop('bg_color','blue')
        self.fg_color=kwargs.pop('fg_color','white')
        super().__init__(master,**kwargs)
        self.config(bg=self.bg_color,fg=self.fg_color)

class VentanaPrincipal:
    def __init__(self,root):
        self.root=root
        self.root.title("Ejemplo de Tkinter con POO")
        self.root.geometry("300x200")

        self.etiqueta2=EtiquetaPersonalizada(root,text="Hola soy una etiqueta personalizada",bg_color="blue",fg_color="white")
        self.etiqueta2.pack(pady=30)

        self.etiqueta=EtiquetaPersonalizada(root,text="Hola Soy una etiqueta con estilo!",bg_color="blue",fg_color="white")
        self.etiqueta.pack(pady=10)

        self.boton=tk.Button(root,text="Haz Click",command=self.cambiar_texto)
        self.boton.pack()

    def cambiar_texto(self):
        self.etiqueta.config(text="El Texto ha cambiado")    


if __name__=="__main__":
    root=tk.Tk()#Objeto que que utiliza la clase tkinter para usar sus widgets
    app=VentanaPrincipal(root)
    root.mainloop()



        