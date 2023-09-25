# Importa las funciones para obtener ventas y compras
import tkinter as tk
from tkinter import messagebox, ttk
from app.admin.movimientos import datos_tabla_movimientos
from app.utils import c_negro, c_verde, c_morado, c_rojo, c_azul, c_blanco, c_gris

#metodo del boton4
def movimientos(contenedor_derecho):
    # Limpia el contenido anterior
    for widget in contenedor_derecho.winfo_children():
        widget.destroy()

    etiqueta_titulo = tk.Label(contenedor_derecho, text="Movimientos", fg=c_blanco, bg=c_verde, font=("Arial", 16, "bold"))
    etiqueta_titulo.pack(pady=10)

    # Crear un Frame principal para contener todo
    frame_principal = tk.Frame(contenedor_derecho, bg="white")
    frame_principal.pack(fill="both", expand=True)

    # Crear un Frame para contener el buscador
    frame_buscador = tk.Frame(frame_principal, bg="white")
    frame_buscador.pack(side="top", fill="x")

    # Crear la entrada de búsqueda
    entrada_busqueda = tk.Entry(frame_buscador)
    entrada_busqueda.pack(side="left")

    # Crear el botón de búsqueda
    boton_buscar = tk.Button(frame_buscador, text="Buscar", command=lambda: buscar(tabla_usuarios, entrada_busqueda))
    boton_buscar.pack(side="left")

    #crear la tabla de inventario del contenedor derecho
    tabla_movimientos = ttk.Treeview(frame_principal, columns=("id", "descripcion","status", "total"), show="headings", style="Custom.Treeview")

    tabla_movimientos.heading("id", text="Movimientos") 
    tabla_movimientos.heading("descripcion", text="Descripcion")
    tabla_movimientos.heading("status", text="Estado")
    tabla_movimientos.heading("total", text="Total")

    #ajustar tamaño de columnas
    tabla_movimientos.column("id", width=150)
    tabla_movimientos.column("descripcion", width=150)
    tabla_movimientos.column("status",width=100)
    tabla_movimientos.column("total",width=100)

    #contenido de la tabla
    datos_tabla_movimientos(tabla_movimientos)

    #mostrar la tabla en el contenedor derecho
    tabla_movimientos.pack(fill="both",expand=True)