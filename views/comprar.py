import tkinter as tk
from app.admin.inventario import consultar_producto
from views.confirmar_comprar import hacer_compra
def comprar_producto(id_producto, tabla_producto, username):
    producto = consultar_producto(id_producto)
    # Puedes utilizar el valor de id_producto para identificar y editar el proveedpr correspondiente.
    print(f"Editar producto con ID: {id_producto}")
    # Abrir la ventana producto
    ventana = tk.Toplevel()
    ventana.title("Comprar producto")
    ventana.configure(bg="white")

    formulario = tk.Frame(ventana, bg="#1b2838", padx=20, pady=20, borderwidth=2, relief="groove")
    formulario.pack(padx=20, pady=20)

    titulo_label = tk.Label(formulario, text="Comprar producto:", bg="black", fg="white")
    titulo_label.pack(pady=10)
    
    producto_label = tk.Label(formulario, text="producto:", bg="black", fg="white")
    producto_label.pack(pady=5)

    producto_editar = tk.Entry(formulario, bg="white")
    producto_editar.pack(pady=5)
    producto_editar.insert(0, producto.get("descripcion_producto", ""))

    cantidad_label = tk.Label(formulario, text="Nueva cantidad:", bg="black", fg="white")
    cantidad_label.pack(pady=5)
    cantidad = tk.Entry(formulario, bg="white")
    cantidad.pack(pady=5)

    precio_label = tk.Label(formulario, text="Precio:", bg="black", fg="white")
    precio_label.pack(pady=5)

    precio = tk.Entry(formulario, bg="white")
    precio.pack(pady=5)
    precio.insert(0, producto.get("precio_unitario", ""))

    proveedores_label = tk.Label(formulario, text="Proveedor:", bg="black", fg="white")
    proveedores_label.pack(pady=5)

    proveedores_editar = tk.Entry(formulario, bg="white")
    proveedores_editar.pack(pady=5)
    proveedores_editar.insert(0, producto.get("id_proveedor", ""))
    

    # Botón de guardar producto
    boton_editar_producto = tk.Button(formulario, text="Comprar productos", command= lambda: hacer_compra(id_producto, precio,cantidad, proveedores_editar, ventana, tabla_producto, username), activebackground="#F50743", font=("helvetica", 12))
    boton_editar_producto.pack(pady=10, ipadx=10)
