# Importa las funciones para obtener ventas y compras
import tkinter as tk
from app.admin.inicio import obtener_ventas, obtener_compras
from app.utils import c_negro, c_verde, c_morado, c_rojo, c_azul, c_blanco, c_gris

def inicio(contenedor_derecho):
    # Limpia el contenido anterior
    for widget in contenedor_derecho.winfo_children():
        widget.destroy()
        
    etiqueta_titulo = tk.Label(contenedor_derecho, text="Inicio", fg=c_blanco, bg=c_verde, font=("Arial", 16, "bold"))
    etiqueta_titulo.pack(pady=10)

    # Obtener datos de ventas y compras
    ventas_semana = obtener_ventas(semana=True)
    ventas_mes = obtener_ventas(mes=True)
    ventas_anio = obtener_ventas(anio=True)

    compras_semana = obtener_compras(semana=True)
    compras_mes = obtener_compras(mes=True)
    compras_anio = obtener_compras(anio=True)

    # Calcular el dinero total de ventas y compras
    total_ventas_semana = sum(ventas_semana)
    total_ventas_mes = sum(ventas_mes)
    total_ventas_anio = sum(ventas_anio)

    total_compras_semana = sum(compras_semana)
    total_compras_mes = sum(compras_mes)
    total_compras_anio = sum(compras_anio)

    # Mostrar el resumen en etiquetas
    resumen_ventas = tk.Label(contenedor_derecho, text=f"Ventas de la semana: ${total_ventas_semana:.2f}", bg="white")
    resumen_ventas.pack(pady=5)

    resumen_compras = tk.Label(contenedor_derecho, text=f"Compras de la semana: ${total_compras_semana:.2f}", bg="white")
    resumen_compras.pack(pady=5)

    resumen_ventas_mes = tk.Label(contenedor_derecho, text=f"Ventas del mes: ${total_ventas_mes:.2f}", bg="white")
    resumen_ventas_mes.pack(pady=5)

    resumen_compras_mes = tk.Label(contenedor_derecho, text=f"Compras del mes: ${total_compras_mes:.2f}", bg="white")
    resumen_compras_mes.pack(pady=5)

    resumen_ventas_anio = tk.Label(contenedor_derecho, text=f"Ventas del año: ${total_ventas_anio:.2f}", bg="white")
    resumen_ventas_anio.pack(pady=5)

    resumen_compras_anio = tk.Label(contenedor_derecho, text=f"Compras del año: ${total_compras_anio:.2f}", bg="white")
    resumen_compras_anio.pack(pady=5)
