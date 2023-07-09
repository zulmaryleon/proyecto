import tkinter as tk
from funciones.funcionesdebotones import redirigir_inicio, redirigir_inventario, redirigir_productos, redirigir_usuario

ventana=tk.Tk()
ventana.title("sistema de inventario")
ventana.geometry("1200x800")

navbar=tk.Frame(ventana,bg="pink")
navbar.pack(side="top", fill="x")

fondo=tk.Label(navbar, bg="pink")
fondo.pack(side="left")

#botonesizquierdos
boton1=tk.Button(navbar,text="inicio", command=redirigir_inicio)
boton1.pack(side="left")
boton2=tk.Button(navbar,text="productos", command=redirigir_productos)
boton2.pack(side="left")

#botonesderechos
boton3=tk.Button(navbar,text="usuario", command=redirigir_usuario)
boton3.pack(side="right")
boton4=tk.Button(navbar,text="inventario", command=redirigir_inventario)
boton4.pack(side="right")




ventana.mainloop()

ventana.quit()

