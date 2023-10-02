# Importa las funciones para obtener ventas y compras
import tkinter as tk
from app.admin.inventario import consultar_producto, datos_tabla_inventario, guardar_producto, obtener_categorias, obtener_proveedores
from app.utils import c_negro, c_verde, c_morado, c_rojo, c_azul, c_blanco, c_gris

#crear formulario de inventario
def crear_producto(tabla_inventario):
    # Abrir la ventana producto
    ventana_crear_producto = tk.Toplevel()
    ventana_crear_producto.title("crear producto")
    ventana_crear_producto.configure(bg="white")
   
    # Crear un marco para el formulario
    formulario_crear = tk.Frame(ventana_crear_producto , bg="#1b2838", padx=20, pady=20, borderwidth=2, relief="groove")
    formulario_crear.pack(padx=20, pady=20)

    titulo_label = tk.Label(formulario_crear, text="Crear Producto:", bg="black", fg="white")
    titulo_label.pack(pady=10)

    # Etiqueta de producto
    producto_label = tk.Label(formulario_crear, text="Producto:", bg="black", fg="white")

    # Etiqueta de producto
    producto_label = tk.Label(formulario_crear, text="producto:", bg="black", fg="white")
    producto_label.pack(pady=5)

   # Cuadro de entrada de producto
    producto_crear = tk.Entry(formulario_crear, bg="white")
    producto_crear.pack(pady=5) 

    # Etiqueta de categoria
    categoria_label = tk.Label(formulario_crear, text="Categoria:", bg="black", fg="white")
    categoria_label.pack(pady=5)

    # Obtener los roles desde la base de datos
    categorias = obtener_categorias()
    selected_categoria = tk.StringVar()

    # Crear una lista de opciones para el menú desplegable
    opciones_prefijo = [categoria[1] for categoria in categorias]

    # Menú desplegable de roles
    prefijo_option_menu = tk.OptionMenu(formulario_crear, selected_categoria, *opciones_prefijo)
    prefijo_option_menu.pack(pady=5)

    # Etiqueta para cantidad
    cantidad_label = tk.Label(formulario_crear, text="Cantidad:", bg="black", fg="white")
    cantidad_label.pack(pady=5)

    # Cuadro de entrada de cantidad
    cantidad_crear = tk.Entry(formulario_crear, bg="white")
    cantidad_crear.pack(pady=5)

    # Etiqueta para precio del producto
    precio_label = tk.Label(formulario_crear, text="Precio al mayor:", bg="black", fg="white")
    precio_label.pack(pady=5)

    # Cuadro de entrada para el precio
    precio_crear = tk.Entry(formulario_crear, bg="white")
    precio_crear.pack(pady=5)

    # Etiqueta para precio del producto
    precio_unitario_label = tk.Label(formulario_crear, text="Precio unitario:", bg="black", fg="white")
    precio_unitario_label.pack(pady=5)

    # Cuadro de entrada del precio
    precio_unitario_crear = tk.Entry(formulario_crear, bg="white")
    precio_unitario_crear.pack(pady=5)

    # Etiqueta para la fecha de vencimiento
    fecha_vencimiento_label = tk.Label(formulario_crear, text="Fecha de vencimiento:", bg="black", fg="white")
    fecha_vencimiento_label.pack(pady=5)

    # Cuadro de entrada de la fecha de vencimiento
    fecha_vencimiento_crear = tk.Entry(formulario_crear, bg="white")
    fecha_vencimiento_crear.pack(pady=5)

    # Etiqueta para precio del producto
    proveedor_label = tk.Label(formulario_crear, text="Proveedor:", bg="black", fg="white")
    proveedor_label.pack(pady=5)

    # Obtener los roles desde la base de datos
    proveedores = obtener_proveedores()
    selected_proveedor = tk.StringVar()

    # Crear una lista de opciones para el menú desplegable
    opciones_proveedor = [proveedor[1] for proveedor in proveedores]

    # Menú desplegable de roles
    prefijo_option_menu = tk.OptionMenu(formulario_crear, selected_proveedor, *opciones_proveedor)
    prefijo_option_menu.pack(pady=5)


    # Botón de guardar producto
    boton_guardar_producto = tk.Button(formulario_crear, text="Crear Producto", command=lambda: guardar_producto(producto_crear, selected_categoria, precio_crear, precio_unitario_crear, cantidad_crear, fecha_vencimiento_crear, tabla_inventario, ventana_crear_producto, selected_proveedor), activebackground="#F50743", font=("helvetica", 12))
    boton_guardar_producto.pack(pady=10, ipadx=10)  