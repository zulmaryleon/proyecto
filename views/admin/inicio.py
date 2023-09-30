import tkinter as tk
from tkinter import PhotoImage
from app.admin.inicio import obtener_ventas, obtener_compras
from app.utils import c_negro, c_verde, c_morado, c_rojo, c_azul, c_blanco, c_gris

def inicio(contenedor_derecho):
    # Limpia el contenido anterior
    for widget in contenedor_derecho.winfo_children():
        widget.destroy()

    etiqueta_titulo = tk.Label(contenedor_derecho, text="Inicio", fg=c_blanco, bg=c_verde, font=("Arial", 16, "bold"))
    etiqueta_titulo.pack(pady=10)

    # Datos de ejemplo para las tarjetas
    datos_tarjetas = [
        {"imagen": "imagenes/movimientos.png", "resumen": "Resumen 1"},
        {"imagen": "imagenes/productos.png", "resumen": "Resumen 2"},
        {"imagen": "imagenes/proveedor.png", "resumen": "Resumen 3"},
        # Agrega más datos de tarjetas aquí
    ]

    # Crear tarjetas en una cuadrícula
    fila_actual = 0
    columna_actual = 0
    for datos in datos_tarjetas:
        imagen = PhotoImage(file=datos["imagen"])
        tarjeta = tk.Frame(contenedor_derecho, padx=10, pady=10, relief=tk.RAISED, borderwidth=2)
        tarjeta.grid(row=fila_actual, column=columna_actual, padx=10, pady=10)

        # Agregar la imagen a la tarjeta
        imagen_label = tk.Label(tarjeta, image=imagen)
        imagen_label.pack()

        # Agregar el resumen debajo de la imagen
        resumen_label = tk.Label(tarjeta, text=datos["resumen"], font=("Arial", 12))
        resumen_label.pack()

        # Actualizar la posición de la cuadrícula
        columna_actual += 1
        if columna_actual > 2:
            columna_actual = 0
            fila_actual += 1
