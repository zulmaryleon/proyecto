import tkinter as tk
from app.admin.proveedor import guardar_proveedor, obtener_prefijo

def crear_proveedor(tabla_proveedor):
    # Abrir la ventana producto
    ventana_crear_proveedor = tk.Toplevel()
    ventana_crear_proveedor.title("crear proveedor")
    ventana_crear_proveedor.configure(bg="white")
   
    # Crear un marco para el formulario de proveedor
    formulario_crear = tk.Frame(ventana_crear_proveedor , bg="#1b2838", padx=20, pady=20, borderwidth=2, relief="groove")
    formulario_crear.pack(padx=20, pady=20)

    titulo_label = tk.Label(formulario_crear, text="Crear Proveedor:", bg="black", fg="white")
    titulo_label.pack(pady=10)

    # Etiqueta de producto
    proveedor_label = tk.Label(formulario_crear, text="Proveedor:", bg="black", fg="white")
    proveedor_label.pack(pady=5)

   # Cuadro de entrada de proveedor
    proveedor_crear = tk.Entry(formulario_crear, bg="white")
    proveedor_crear.pack(pady=5) 

    # Etiqueta de categoria
    codigo_label = tk.Label(formulario_crear, text="Rif:", bg="black", fg="white")
    codigo_label.pack(pady=5)

    # Cuadro de entrada de categoria
    codigo_entry = tk.Entry(formulario_crear, bg="white")
    codigo_entry.pack(pady=5)

    # Etiqueta para cantidad
    # Etiqueta para seleccionar rol del usuario
    prefijo_label = tk.Label(formulario_crear, text="Rol del Usuario:", bg="black", fg="white")
    prefijo_label.pack(pady=5)

    # Obtener los roles desde la base de datos
    prefijos = obtener_prefijo()
    selected_prefijo = tk.StringVar()

    # Crear una lista de opciones para el menú desplegable
    opciones_prefijo = [prefijo[1] for prefijo in prefijos]

    # Menú desplegable de roles
    prefijo_option_menu = tk.OptionMenu(formulario_crear, selected_prefijo, *opciones_prefijo)
    prefijo_option_menu.pack(pady=5)

    # Botón de guardar producto
    boton_guardar_proveedor = tk.Button(formulario_crear, text="Guardar Proveedor", command=lambda: guardar_proveedor(proveedor_crear, codigo_entry, selected_prefijo, ventana_crear_proveedor, tabla_proveedor), activebackground="#F50743", font=("helvetica", 12))
    boton_guardar_proveedor.pack(pady=10, ipadx=10)