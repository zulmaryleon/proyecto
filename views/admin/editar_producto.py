import tkinter as tk
from app.admin.inventario import consultar_producto, editar_datos_producto
def editar_producto(id_producto, tabla_producto):
    producto = consultar_producto(id_producto)
    # Puedes utilizar el valor de id_producto para identificar y editar el proveedpr correspondiente.
    print(f"Editar producto con ID: {id_producto}")
    # Abrir la ventana producto
    ventana_editar_producto = tk.Toplevel()
    ventana_editar_producto.title("Editar producto")
    ventana_editar_producto.configure(bg="white")

    formulario_editar = tk.Frame(ventana_editar_producto, bg="#1b2838", padx=20, pady=20, borderwidth=2, relief="groove")
    formulario_editar.pack(padx=20, pady=20)

    titulo_label = tk.Label(formulario_editar, text="Editar producto:", bg="black", fg="white")
    titulo_label.pack(pady=10)
    
    producto_label = tk.Label(formulario_editar, text="producto:", bg="black", fg="white")
    producto_label.pack(pady=5)

    producto_editar = tk.Entry(formulario_editar, bg="white")
    producto_editar.pack(pady=5)
    producto_editar.insert(0, producto.get("descripcion_producto", ""))

    cantidad_label = tk.Label(formulario_editar, text="Cantidad:", bg="black", fg="white")
    cantidad_label.pack(pady=5)

    cantidad_editar = tk.Entry(formulario_editar, bg="white")
    cantidad_editar.pack(pady=5)
    cantidad_editar.insert(0, producto.get("cantidad_total", ""))

    fecha_vencimiento_label = tk.Label(formulario_editar, text="fecha_vencimiento:", bg="black", fg="white")
    fecha_vencimiento_label.pack(pady=5)

    fecha_vencimiento = tk.Entry(formulario_editar, bg="white")
    fecha_vencimiento.pack(pady=5)
    fecha_vencimiento.insert(0, producto.get("fecha_vencimiento", ""))

    proveedores_label = tk.Label(formulario_editar, text="proveedores:", bg="black", fg="white")
    proveedores_label.pack(pady=5)

    proveedores_editar = tk.Entry(formulario_editar, bg="white")
    proveedores_editar.pack(pady=5)
    proveedores_editar.insert(0, producto.get("id_proveedor", ""))

    precio_compra_label = tk.Label(formulario_editar, text="precio_compra:", bg="black", fg="white")
    precio_compra_label.pack(pady=5)

    precio_compra_editar = tk.Entry(formulario_editar, bg="white")
    precio_compra_editar.pack(pady=5)
    precio_compra_editar.insert(0, producto.get("costo_mayor", ""))

    precio_venta_label = tk.Label(formulario_editar, text="precio_unitario:", bg="black", fg="white")
    precio_venta_label.pack(pady=5)

    precio_venta_editar = tk.Entry(formulario_editar, bg="white")
    precio_venta_editar.pack(pady=5)
    precio_venta_editar.insert(0, producto.get("precio_unitario", ""))

    # Botón de guardar producto
    boton_editar_producto = tk.Button(formulario_editar, text="Editar producto", command= lambda: editar_datos_producto(id_producto, producto_editar,cantidad_editar, fecha_vencimiento, proveedores_editar,precio_compra_editar, precio_venta_editar, ventana_editar_producto, tabla_producto), activebackground="#F50743", font=("helvetica", 12))
    boton_editar_producto.pack(pady=10, ipadx=10)
