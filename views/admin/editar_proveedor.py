import tkinter as tk
from app.admin.proveedor import consultar_proveedor, editar_datos_proveedor, obtener_prefijo
def editar_proveedor(id_proveedor, tabla_proveedor):
    proveedor = consultar_proveedor(id_proveedor)
    # Puedes utilizar el valor de id_proveedor para identificar y editar el proveedpr correspondiente.
    print(f"Editar proveedor con ID: {id_proveedor}")
    # Abrir la ventana proveedor
    ventana_editar_proveedor = tk.Toplevel()
    ventana_editar_proveedor.title("Editar proveedor")
    ventana_editar_proveedor.configure(bg="white")

    formulario_editar = tk.Frame(ventana_editar_proveedor, bg="#1b2838", padx=20, pady=20, borderwidth=2, relief="groove")
    formulario_editar.pack(padx=20, pady=20)

    titulo_label = tk.Label(formulario_editar, text="Editar proveedor:", bg="black", fg="white")
    titulo_label.pack(pady=10)
    
    proveedor_label = tk.Label(formulario_editar, text="Proveedor:", bg="black", fg="white")
    proveedor_label.pack(pady=5)

    proveedor_editar = tk.Entry(formulario_editar, bg="white")
    proveedor_editar.pack(pady=5)
    proveedor_editar.insert(0, proveedor.get("nombre", ""))

    codigo_label = tk.Label(formulario_editar, text="Còdigo:", bg="black", fg="white")
    codigo_label.pack(pady=5)

    codigo_editar = tk.Entry(formulario_editar, bg="white")
    codigo_editar.pack(pady=5)
    codigo_editar.insert(0, proveedor.get("codigo", ""))

    # Etiqueta para seleccionar el prefijo del documento
    prefijo_label = tk.Label(formulario_editar, text="Prefijo Documento:", bg="black", fg="white")
    prefijo_label.pack(pady=5)

    # Obtener los roles desde la base de datos
    prefijos = obtener_prefijo()
    selected_prefijo = tk.StringVar()

    # Crear una lista de opciones para el menú desplegable
    opciones_prefijo = [prefijo[1] for prefijo in prefijos]

    # Menú desplegable de roles
    prefijo_option_menu = tk.OptionMenu(formulario_editar, selected_prefijo, *opciones_prefijo)
    prefijo_option_menu.pack(pady=5)

    # Botón de guardar proveedor
    boton_editar_proveedor = tk.Button(formulario_editar, text="Editar Proveedor", command= lambda: editar_datos_proveedor(id_proveedor, proveedor_editar,codigo_editar, selected_prefijo, tabla_proveedor, ventana_editar_proveedor), activebackground="#F50743", font=("helvetica", 12))
    boton_editar_proveedor.pack(pady=10, ipadx=10)
