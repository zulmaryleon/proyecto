# Importa las funciones para obtener ventas y compras
import tkinter as tk
from tkinter import messagebox, ttk

# Modulos de logica
from app.admin.inventario import consultar_producto, datos_tabla_inventario
from app.utils import c_negro, c_verde, c_morado, c_rojo, c_azul, c_blanco, c_gris, buscar

# Modulos de vistas formularios
from views.admin.crear_producto import crear_producto
from views.admin.editar_producto import editar_producto
from views.admin.eliminar_producto import eliminar_producto

# Modulos vistas formularios 
from views.comprar import comprar_producto
from views.vender import vender_producto

#metodo del boton2
def inventario(contenedor_derecho, username):
    # Limpia el contenido anterior
    for widget in contenedor_derecho.winfo_children():
        widget.destroy()

    etiqueta_titulo = tk.Label(contenedor_derecho, text="Inventario", fg=c_blanco, bg=c_negro, font=("Arial", 16, "bold"))
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

    # Crear la entrada de búsqueda
    boton_buscar = tk.Button(frame_buscador, text="Buscar", command=lambda: buscar(tabla_inventario, entrada_busqueda))
    boton_buscar.pack(side="left")

    #crear la tabla de inventario del contenedor derecho
    tabla_inventario = ttk.Treeview(frame_principal, columns=("#", "descripcion_producto", "cantidad_total", "fecha_vencimiento", "id_proveedor", "costo_mayor", "precio_unitario"), show="headings", style="Custom.Treeview")

    tabla_inventario.heading("#", text="#") 
    tabla_inventario.heading("descripcion_producto", text="producto") 
    tabla_inventario.heading("cantidad_total", text="cantidad")
    tabla_inventario.heading("fecha_vencimiento", text="fecha de vencimiento")
    tabla_inventario.heading("id_proveedor", text="proveedores")
    tabla_inventario.heading("costo_mayor", text="precio de compra")
    tabla_inventario.heading("precio_unitario", text="precio de venta")

    #ajustar tamaño de columnas
    tabla_inventario.column("#", width=25)
    tabla_inventario.column("descripcion_producto", width=100)
    tabla_inventario.column("cantidad_total", width=100)
    tabla_inventario.column("fecha_vencimiento",width=150)
    tabla_inventario.column("id_proveedor", width=150)
    tabla_inventario.column("costo_mayor", width=150)
    tabla_inventario.column("precio_unitario", width=150)

    #contenido de la tabla
    datos_tabla_inventario(tabla_inventario)

    #mostrar la tabla en el contenedor derecho
    tabla_inventario.pack(fill="both",expand=True)

    #boton de crear producto
    boton_guardar_inventario=tk.Button(frame_principal,text="crear producto", command = lambda: crear_producto(tabla_inventario))
    boton_guardar_inventario.pack(side="left",padx=10,pady=5)

    # Botones Editar y Eliminar (ocultos inicialmente)
    editar_button = tk.Button(frame_principal, text="Editar", command=lambda: editar_producto(id_producto))
    eliminar_button = tk.Button(frame_principal, text="Eliminar", command=lambda: eliminar_producto(id_producto))

    # Botones vender y comprar (ocultos inicialmente)
    vender_button = tk.Button(frame_principal, text="Vender", command=lambda: vender_producto(id_producto))
    comprar_button = tk.Button(frame_principal, text="Comprar", command=lambda: comprar_producto(id_producto))
    
    # Configurar la acción de selección de inventario
    def seleccionar_producto(event):
        item_seleccionado = tabla_inventario.selection()
        if item_seleccionado:
            id_producto = tabla_inventario.item(item_seleccionado, "values")[0]
            editar_button.configure(command=lambda: editar_producto(id_producto, tabla_inventario))
            eliminar_button.configure(command=lambda: eliminar_producto(id_producto, tabla_inventario))
            vender_button.configure(command=lambda: vender_producto(id_producto, tabla_inventario, username))
            comprar_button.configure(command=lambda: comprar_producto(id_producto, tabla_inventario, username))
            editar_button.pack(side="left", padx=10, pady=5)
            eliminar_button.pack(side="left", padx=10, pady=5)
            vender_button.pack(side="left", padx=10, pady=5)
            comprar_button.pack(side="left", padx=10, pady=5)

        else:
            editar_button.pack_forget()
            eliminar_button.pack_forget()
            vender_button.pack_forget()
            comprar_button.pack_forget()

    tabla_inventario.bind("<<TreeviewSelect>>", seleccionar_producto)