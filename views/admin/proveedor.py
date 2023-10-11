# Importa las funciones para obtener ventas y compras
import tkinter as tk
from tkinter import messagebox, ttk
from app.admin.proveedor import consultar_proveedor, datos_tabla_proveedor
from app.utils import c_negro, c_verde, c_morado, c_rojo, c_azul, c_blanco, c_gris, buscar
from views.admin.crear_proveedor import crear_proveedor
from views.admin.editar_proveedor import editar_proveedor
from views.admin.eliminar_proveedor import eliminar_proveedor

#metodo del boton3
def proveedor(contenedor_derecho):
    # Limpia el contenido anterior
    for widget in contenedor_derecho.winfo_children():
        widget.destroy()
   
    etiqueta_titulo = tk.Label(contenedor_derecho, text="Proveedores", fg = c_blanco, bg= c_negro, font=("Arial", 16, "bold"))
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
    boton_buscar = tk.Button(frame_buscador, text="Buscar", command=lambda: buscar(tabla_proveedor, entrada_busqueda))
    boton_buscar.pack(side="left")

    #crear la tabla de inventario del contenedor derecho
    tabla_proveedor = ttk.Treeview(frame_principal, columns=("#", "nombre", "codigo","id_prefijo_documento"), show="headings", style="Custom.Treeview")

    tabla_proveedor.heading("#", text="#") 
    tabla_proveedor.heading("nombre", text="Proveedor") 
    tabla_proveedor.heading("id_prefijo_documento", text="Rif")
    tabla_proveedor.heading("codigo", text="Documento")
    

    #ajustar tamaño de columnas
    tabla_proveedor.column("#", width=25)
    tabla_proveedor.column("nombre", width=150)
    tabla_proveedor.column("id_prefijo_documento", width=150)
    tabla_proveedor.column("codigo",width=150)
    

    #contenido de la tabla
    datos_tabla_proveedor(tabla_proveedor)

    #mostrar la tabla en el contenedor derecho
    tabla_proveedor.pack(fill="both",expand=True)

    #boton de crear proveedor
    boton_crear_proveedor=tk.Button(frame_principal,text="crear proveedor", command=lambda: crear_proveedor(tabla_proveedor))
    boton_crear_proveedor.pack(side="left",padx=10,pady=5)
    
    # Botones Editar y Eliminar (ocultos inicialmente)
    editar_button = tk.Button(frame_principal, text="Editar", command=lambda: editar_proveedor(id_proveedor))
    eliminar_button = tk.Button(frame_principal, text="Eliminar", command=lambda: eliminar_proveedor(id_proveedor))

    # Configurar la acción de selección de proveedor
    def seleccionar_proveedor(event):
        item_seleccionado = tabla_proveedor.selection()
        if item_seleccionado:
            id_proveedor = tabla_proveedor.item(item_seleccionado, "values")[0]
            editar_button.configure(command=lambda: editar_proveedor(id_proveedor, tabla_proveedor, ))
            eliminar_button.configure(command=lambda: eliminar_proveedor(id_proveedor, tabla_proveedor))
            editar_button.pack(side="left", padx=10, pady=5)
            eliminar_button.pack(side="left", padx=10, pady=5)
        else:
            editar_button.pack_forget()
            eliminar_button.pack_forget()

    tabla_proveedor.bind("<<TreeviewSelect>>", seleccionar_proveedor)