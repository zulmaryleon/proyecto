from tkinter import messagebox
from app.database import get_database_connection

# Función para consultar un usuario en MySQL
conexion = get_database_connection()

def datos_tabla_inventario(tabla):
    #eliminamos todos lo elementos antes de actualizar
    tabla.delete(*tabla.get_children())

    cursor = conexion.cursor()
    cursor.execute("select id_producto, descripcion_producto, cantidad_total, fecha_vencimiento, id_proveedor, costo_mayor, precio_unitario from productos")
    resultado= cursor.fetchall()
    for id_producto, descripcion_producto, cantidad_total, fecha_vencimiento, id_proveedor, costo_mayor, precio_unitario in resultado:

        #insercion de datos
        tabla.insert("", "end", values=(id_producto, descripcion_producto, cantidad_total, fecha_vencimiento, id_proveedor, costo_mayor, precio_unitario)) 

# Función para consultar un producto en MySQL
def consultar_producto(id_producto):
    cursor = conexion.cursor(dictionary=True)  # Utiliza dictionary=True para obtener un diccionario
    # Consultar el inventario por ID
    try:
        consulta = "SELECT descripcion_producto, id_categoria, cantidad_total, costo_mayor, precio_unitario, fecha_vencimiento, id_proveedor FROM productos WHERE id_producto = %s"
        cursor.execute(consulta, (id_producto,))
        producto = cursor.fetchone()

        cursor.close()

        return producto

    except Exception as e:
        conexion.rollback()
        messagebox.showerror("Error", f"No se ha podido consultar el producto: {str(e)}")

#crear formulario de inventario
def crear_producto():
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

    titulo_label = tk.Label(formulario_crear, text="Crear producto:", bg="black", fg="white")
    titulo_label.pack(pady=10)

    # Etiqueta de producto
    producto_label = tk.Label(formulario_crear, text="producto:", bg="black", fg="white")
    producto_label.pack(pady=5)

   # Cuadro de entrada de producto
    producto_crear = tk.Entry(formulario_crear, bg="white")
    producto_crear.pack(pady=5) 

    # Etiqueta de categoria
    categoria_label = tk.Label(formulario_crear, text="Categoria:", bg="black", fg="white")
    categoria_label.pack(pady=5)

    # Cuadro de entrada de categoria
    categoria_entry = tk.Entry(formulario_crear, bg="white")
    categoria_entry.pack(pady=5)

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

    # Cuadro de entrada del precio
    proveedor_crear = tk.Entry(formulario_crear, bg="white")
    proveedor_crear.pack(pady=5)

    
    def guardar_producto():
        global conexion #definimos la variable conexion como global
        producto = producto_crear.get()
        categoria = categoria_entry.get()
        cantidad = cantidad_crear.get()
        precio_mayor=precio_crear.get()
        precio_unitario = precio_unitario_crear.get()
        fecha_vencimiento= fecha_vencimiento_crear.get()
        proveedor = proveedor_crear.get()
        fecha_actual=datetime.date.today()

        #creamos una sentencia para guardar los datos en la base de datos
        try:
            #abrir cursor
            cursor=conexion.cursor()
            consulta="INSERT INTO productos (descripcion_producto, id_categoria, cantidad_total, costo_mayor, precio_unitario, fecha_vencimiento, id_proveedor) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(consulta, (producto, categoria, cantidad, precio_mayor, precio_unitario, fecha_vencimiento, proveedor))

            conexion.commit()
            #actualizar tabla
            datos_tabla_inventario(tabla_inventario)

            cursor.close()
            ventana_crear_producto.destroy()

            messagebox.showinfo("Producto creado", 'Se ha registrado el producto correctamente')

            messagebox.showinfo("Usuario creado", 'Se ha registrado el producto correctamente')
        except Exception as e:
            conexion.rollback()
            messagebox.showerror("Error", f"No se ha podido registrar el producto: {str(e)}")

    # Botón de guardar producto
    boton_guardar_producto = tk.Button(formulario_crear, text="Crear Producto", command=guardar_producto, activebackground="#F50743", font=("helvetica", 12))
    boton_guardar_producto.pack(pady=10, ipadx=10)        