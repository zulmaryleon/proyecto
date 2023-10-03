import tkinter as tk
from tkinter import PhotoImage
from app.admin.inicio import obtener_ventas, obtener_compras
from app.utils import c_negro, c_verde, c_morado, c_rojo, c_azul, c_blanco, c_gris

def inicio_user(contenedor_derecho):
    # Limpia el contenido anterior
    for widget in contenedor_derecho.winfo_children():
        widget.destroy()

    etiqueta_titulo = tk.Label(contenedor_derecho, text="Inicio", fg=c_blanco, bg=c_negro, font=("Arial", 16, "bold"))
    etiqueta_titulo.pack(pady=10)