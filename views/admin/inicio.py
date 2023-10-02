import tkinter as tk
from tkinter import PhotoImage
from app.admin.inicio import obtener_ventas, obtener_compras
from app.utils import c_negro, c_verde, c_morado, c_rojo, c_azul, c_blanco, c_gris

def inicio(contenedor_derecho):
    # Limpia el contenido anterior
    for widget in contenedor_derecho.winfo_children():
        widget.destroy()

    etiqueta_titulo = tk.Label(contenedor_derecho, text="Inicio", fg=c_blanco, bg=c_negro, font=("Arial", 16, "bold"))
    etiqueta_titulo.pack(pady=10)

    # Etiqueta y entrada para agregar producto
    # Contenedor de gráficos (a la derecha de los recuadros)
    contenedor_graficos = tk.Frame(contenedor_derecho, bg=c_blanco, borderwidth=2, relief="solid")
    contenedor_graficos.pack(side="right", fill="both", expand=True)

    # Crear un recuadro grande para la gráfica
    recuadro_grafica = tk.Frame(contenedor_graficos, width=300, height=300, bg="white", borderwidth=2, relief="solid")
    recuadro_grafica.pack(padx=10, pady=10)    
