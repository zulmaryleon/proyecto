# Importaciones frameworks y dependencias del proyecto
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import mysql.connector
import datetime, time

# Variablers globales del proyecto
global conexion

tabla_usuarios=None
tabla_inventario=None
tabla_proveedor=None
tabla_movimientos=None

boton_guardar_usuario=None
boton_guardar_producto=None
boton_crear_proveedor=None
boton_guardar_proveedor=None
boton_guardar_inventario=None

editar_button=None
eliminar_button=None

entrada_busqueda=None
boton_buscar=None

# Función para consultar un usuario en MySQL
def consultar_usuario(id_usuario):
    #conexion global
    global conexion

    cursor = conexion.cursor(dictionary=True)  # Utiliza dictionary=True para obtener un diccionario
    # Consultar el usuario por ID
    try:
        consulta = "SELECT ci_usuario, usuario, correo, fecha_ingreso, id_cargo FROM usuario WHERE id_usuario = %s"
        cursor.execute(consulta, (id_usuario,))
        usuario = cursor.fetchone()

        cursor.close()

        return usuario

    except Exception as e:
        conexion.rollback()
        messagebox.showerror("Error", f"No se ha podido consultar el usuario: {str(e)}")

def editar_usuario(id_usuario):
    usuario = consultar_usuario(id_usuario)
    # Puedes utilizar el valor de id_usuario para identificar y editar el usuario correspondiente.
    print(f"Editar usuario con ID: {id_usuario}")
    # Abrir la ventana usuario
    ventana_editar_usuario = tk.Toplevel()
    ventana_editar_usuario.title("Editar usuario")
    ventana_editar_usuario.configure(bg="white")

    formulario_editar = tk.Frame(ventana_editar_usuario, bg="#1b2838", padx=20, pady=20, borderwidth=2, relief="groove")
    formulario_editar.pack(padx=20, pady=20)

    titulo_label = tk.Label(formulario_editar, text="Editar Usuario:", bg="black", fg="white")
    titulo_label.pack(pady=10)
    
    usuario_label = tk.Label(formulario_editar, text="Usuario:", bg="black", fg="white")
    usuario_label.pack(pady=5)

    usuario_editar = tk.Entry(formulario_editar, bg="white")
    usuario_editar.pack(pady=5)
    usuario_editar.insert(0, usuario.get("usuario", ""))

    ci_label = tk.Label(formulario_editar, text="Cédula:", bg="black", fg="white")
    ci_label.pack(pady=5)

    ci_editar = tk.Entry(formulario_editar, bg="white")
    ci_editar.pack(pady=5)
    ci_editar.insert(0, usuario.get("ci_usuario", ""))

    correo_label = tk.Label(formulario_editar, text="Correo:", bg="black", fg="white")
    correo_label.pack(pady=5)

    correo_entry = tk.Entry(formulario_editar, bg="white")
    correo_entry.pack(pady=5)
    correo_entry.insert(0, usuario.get("correo", ""))

    rol_label = tk.Label(formulario_editar, text="Rol del Usuario:", bg="black", fg="white")
    rol_label.pack(pady=5)

    rol_entry = tk.Entry(formulario_editar, bg="white")
    rol_entry.pack(pady=5)
    rol_entry.insert(0, usuario.get("id_cargo", ""))

    fecha_label = tk.Label(formulario_editar, text="Fecha de registro:", bg="black", fg="white")
    fecha_label.pack(pady=5)

    fecha_entry = tk.Entry(formulario_editar, bg="white")
    fecha_entry.pack(pady=5)
    fecha_entry.insert(0, usuario.get("fecha_ingreso", ""))

    def editar_usuario():
        global conexion #definimos la variable conexion como global
        usuario = usuario_editar.get()
        correo = correo_entry.get()
        rol= rol_entry.get()
        ci= ci_editar.get()
        fecha_actual=datetime.date.today()
        #creamos una sentencia para guardar los datos en la base de datos
        try:
            # Crear la sentencia SQL para actualizar el usuario en la base de datos
            sentencia = "UPDATE usuario SET usuario = %s, correo = %s, id_cargo = %s, fecha_ingreso = %s, ci_usuario = %s WHERE id_usuario = %s"
            datos = (usuario, correo, rol, fecha_actual, ci, id_usuario)

            cursor = conexion.cursor()
            cursor.execute(sentencia, datos)
            conexion.commit()

            #actualizar tabla
            datos_tabla_usuarios(tabla_usuarios)

            cursor.close()
            ventana_editar_usuario.destroy()

            messagebox.showinfo("Usuario editar", 'Se ha editado el usuario correctamente')
        except Exception as e:
            conexion.rollback()
            messagebox.showerror("Error", f"No se ha podido editar el usuario: {str(e)}")


    # Botón de guardar usuario
    boton_editar_usuario = tk.Button(formulario_editar, text="Editar Usuario", command=editar_usuario, activebackground="#F50743", font=("helvetica", 12))
    boton_editar_usuario.pack(pady=10, ipadx=10)

def eliminar_usuario(id_usuario):
    # Aquí debes implementar la lógica para eliminar el usuario con el ID proporcionado.
    # Puedes utilizar el valor de id_usuario para identificar y eliminar el usuario correspondiente.
    print(f"Eliminar usuario con ID: {id_usuario}")
    global conexion #definimos la variable conexion como global
    try:
         # Crear un cursor
        cursor = conexion.cursor()

        # Consulta para obtener información del usuario
        consulta = f"SELECT usuario FROM usuario WHERE id_usuario = {id_usuario}"
        cursor.execute(consulta)
        usuario = cursor.fetchone()

        # Verificar si se encontró el usuario
        if usuario is None:
            messagebox.showinfo("Información", f"No se encontró un usuario con el ID {id_usuario}")
        else:
            nombre_usuario = usuario[0]

            # Crear una ventana Tkinter para la confirmación
            ventana_confirmacion = tk.Tk()
            ventana_confirmacion.title("Confirmación")

            # Función para eliminar el usuario
            def confirmar_eliminar():
                # Consulta para eliminar al usuario
                consulta_eliminar = f"DELETE FROM usuario WHERE id_usuario = {id_usuario}"
                cursor.execute(consulta_eliminar)
                conexion.commit()
                #actualizar tabla
                datos_tabla_usuarios(tabla_usuarios)
                messagebox.showinfo("Información", f"Usuario '{nombre_usuario}' (ID: {id_usuario}) ha sido eliminado.")
                ventana_confirmacion.destroy()

            # Función para cancelar la eliminación
            def cancelar_eliminar():
                messagebox.showinfo("Información", "Operación de eliminación cancelada.")
                ventana_confirmacion.destroy()

            # Etiqueta de confirmación
            etiqueta_confirmacion = tk.Label(ventana_confirmacion, text=f"¿Estás seguro de eliminar al usuario '{nombre_usuario}' (ID: {id_usuario})?")
            etiqueta_confirmacion.pack()

            # Botones de confirmar y cancelar
            boton_confirmar = tk.Button(ventana_confirmacion, text="Confirmar", command=confirmar_eliminar)
            boton_cancelar = tk.Button(ventana_confirmacion, text="Cancelar", command=cancelar_eliminar)

            boton_confirmar.pack()
            boton_cancelar.pack()

            ventana_confirmacion.mainloop()
    except Exception as e:
        conexion.rollback()
        messagebox.showerror("Error", f"No se ha podido editar el usuario: {str(e)}")            

#metodo de cerrar ventanas
def cerrar_sesion(ventana_dashboard):
    #cerramos la ventana del dashboard
    ventana_dashboard.destroy()
    ventana.destroy()

def buscar(tabla, entrada_busqueda):
    valor_busqueda = entrada_busqueda.get()
    # Itera sobre los elementos de la tabla y muestra solo los que coinciden con la búsqueda
    for row_id in tabla.get_children():
        values = tabla.item(row_id, 'values')
        if valor_busqueda.lower() in [str(value).lower() for value in values]:
            tabla.selection_set(row_id)
        else:
            tabla.selection_remove(row_id)

#Funcion de la data de usuario
def datos_tabla_usuarios(tabla):
    #conexion global
    global conexion

    #eliminamos todos lo elementos antes de actualizar
    tabla.delete(*tabla.get_children())

    cursor = conexion.cursor()
    cursor.execute("select id_usuario, usuario, fecha_ingreso, id_cargo from usuario")
    resultado= cursor.fetchall()
    for id_usuario, usuario, fecha_ingreso, id_cargo in resultado:

        #insercion de datos
        tabla.insert("", "end", values=(id_usuario, usuario, id_cargo, fecha_ingreso))       

#Funcion de la data de movimientos
def datos_tabla_movimientos(tabla):
    #conexion global
    global conexion

    #eliminamos todos lo elementos antes de actualizar
    tabla.delete(*tabla.get_children())

    cursor = conexion.cursor()
    cursor.execute("select id_movimientos, descripcion_movimiento, id_status_movimientos,total, id_usuario, fecha_registro from movimientos")
    resultado= cursor.fetchall()
    for id_movimientos, descripcion_movimiento, id_status_movimientos, total, id_usuario, fecha_registro  in resultado:
        #insercion de datos
        tabla.insert("", "end", values=(id_movimientos, descripcion_movimiento, id_status_movimientos,total))

def crear_usuario():
    # Abrir la ventana usuario
    ventana_crear_usuario = tk.Toplevel()
    ventana_crear_usuario.title("crear usuario")
    ventana_crear_usuario.configure(bg="white")
   
    # Crear un marco para el formulario
    formulario_crear = tk.Frame(ventana_crear_usuario , bg="#1b2838", padx=20, pady=20, borderwidth=2, relief="groove")
    formulario_crear.pack(padx=20, pady=20)

    titulo_label = tk.Label(formulario_crear, text="Crear Usuario:", bg="#1b2838", fg="white")
    titulo_label.pack(pady=10)
    # Etiqueta de usuario
    usuario_label = tk.Label(formulario_crear, text="Usuario:", bg="black", fg="white")
    usuario_label.pack(pady=5)

   # Cuadro de entrada de usuario
    usuario_crear = tk.Entry(formulario_crear, bg="white")
    usuario_crear.pack(pady=5) 

    # Etiqueta de contraseña
    password_label = tk.Label(formulario_crear, text="Contraseña:", bg="black", fg="white")
    password_label.pack(pady=5)

    # Cuadro de entrada de contraseña
    password_entry = tk.Entry(formulario_crear, show="*", bg="white")
    password_entry.pack(pady=5)

    # Etiqueta para confirmar contraseña
    password_label = tk.Label(formulario_crear, text="confirmar Contraseña:", bg="black", fg="white")
    password_label.pack(pady=5)

    # Cuadro de entrada de contraseña para confirmar
    password_crear_confirmar = tk.Entry(formulario_crear, show="*", bg="white")
    password_crear_confirmar.pack(pady=5)

    # Etiqueta para rol del usuario
    rol_label = tk.Label(formulario_crear, text="Rol del Usuario:", bg="black", fg="white")
    rol_label.pack(pady=5)

    # Cuadro de entrada de rol del usuario
    rol_entry = tk.Entry(formulario_crear, bg="white")
    rol_entry.pack(pady=5)

    def guardar_usuario():
        global conexion #definimos la variable conexion como global
        ci="123"
        usuario = usuario_crear.get()
        contrasena = password_entry.get()
        confirmar_contrasena= password_crear_confirmar.get()
        rol=rol_entry.get()
        correo="123"
        fecha_actual=datetime.date.today()

        if (contrasena==confirmar_contrasena):
             #creamos una sentencia para guardar los datos en la base de datos
            try:
                #abrir cursor
                cursor=conexion.cursor()
                consulta="INSERT INTO usuario (ci_usuario, usuario, contraseña, correo, fecha_ingreso, id_cargo) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(consulta, (ci, usuario, contrasena, correo, fecha_actual, rol))

                conexion.commit()
                #actualizar tabla
                datos_tabla_usuarios(tabla_usuarios)

                cursor.close()
                ventana_crear_usuario.destroy()

                messagebox.showinfo("Usuario creado", 'Se ha registrado el usuario correctamente')
            except Exception as e:
                conexion.rollback()
                messagebox.showerror("Error", f"No se ha podido registrar el usuario: {str(e)}")

        else: messagebox.showerror("Error al registrar", "Las contrasenas no coinciden, vuelva a intentarlo")

    # Botón de guardar usuario
    boton_guardar_usuario = tk.Button(formulario_crear, text="Crear Usuario", command=guardar_usuario, activebackground="#F50743", font=("helvetica", 12))
    boton_guardar_usuario.pack(pady=10, ipadx=10)

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
    
#metodo del boton1
def usuarios():
    etiqueta_titulo.config(text="Usuarios del sistema", bg="#2c3e50", fg="white")
    global tabla_usuarios, boton_guardar_usuario, tabla_inventario, boton_guardar_inventario, editar_button, eliminar_button, entrada_busqueda, boton_buscar
    if tabla_usuarios and tabla_usuarios.winfo_exists():
        tabla_usuarios.destroy()
        #si ya existe la tabla inventario/ destruir

    if tabla_inventario and tabla_inventario.winfo_exists():
        tabla_inventario.destroy()

    if boton_guardar_usuario and boton_guardar_usuario.winfo_exists():
        boton_guardar_usuario.destroy()


    if tabla_proveedor and tabla_proveedor.winfo_exists():
        tabla_proveedor.destroy()

    if boton_crear_proveedor and boton_crear_proveedor.winfo_exists():
        boton_crear_proveedor.destroy()

    if boton_guardar_inventario and boton_guardar_inventario.winfo_exists():
        boton_guardar_inventario.destroy()    

    if tabla_movimientos and tabla_movimientos.winfo_exists():
        tabla_movimientos.destroy()

    if boton_guardar_inventario: 
        boton_guardar_inventario.destroy()

    if editar_button: 
        editar_button.destroy()   

    if eliminar_button: 
        eliminar_button.destroy()     

    if entrada_busqueda:
        entrada_busqueda.destroy()
    
    if boton_buscar:
        boton_buscar.destroy()
        
    #aplicar tema x
    estilo= ttk.Style()
    estilo.configure("Custom.Treeview.Heading", font=("Arial", 12, "bold"))
    estilo.configure("Custom.Treeview", font=("Arial", 10), background="#ececec", fieldbackground="#ececec")

    #crear la tabla de usuario del contenedor derecho
    tabla_usuarios = ttk.Treeview(contenido, columns=("id", "Usuario", "Rol", "Registrado"), show="headings", style="Custom.Treeview")

    entrada_busqueda = tk.Entry(contenido)
    entrada_busqueda.pack(side=tk.TOP)

    boton_buscar = tk.Button(contenido, text="Buscar", command=lambda: buscar(tabla_usuarios, entrada_busqueda))
    boton_buscar.pack(side=tk.TOP)

    tabla_usuarios.heading("id", text="#") 
    tabla_usuarios.heading("Usuario", text="Usuario") 
    tabla_usuarios.heading("Rol", text="Rol del Usuario")
    tabla_usuarios.heading("Registrado", text="Fecha de registro")

    #ajustar tamaño de columnas
    tabla_usuarios.column("id", width=50)
    tabla_usuarios.column("Usuario", width=200)
    tabla_usuarios.column("Rol", width=200)
    tabla_usuarios.column("Registrado", width=200)
   
    #contenido de la tabla
    datos_tabla_usuarios(tabla_usuarios)

    #mostrar la tabla en el contenedor derecho
    tabla_usuarios.pack(fill="both",expand=True)

    # Botón de crear usuario
    boton_guardar_usuario = tk.Button(contenido, text="Crear Usuario", command=crear_usuario)
    boton_guardar_usuario.pack(side="left", padx=10, pady=5)

    # Botones Editar y Eliminar (ocultos inicialmente)
    editar_button = tk.Button(contenido, text="Editar", command=lambda: editar_usuario(id_usuario))
    eliminar_button = tk.Button(contenido, text="Eliminar", command=lambda: eliminar_usuario(id_usuario))

    # Configurar la acción de selección de usuario
    def seleccionar_usuario(event):
        item_seleccionado = tabla_usuarios.selection()
        if item_seleccionado:
            id_usuario = tabla_usuarios.item(item_seleccionado, "values")[0]
            editar_button.configure(command=lambda: editar_usuario(id_usuario))
            eliminar_button.configure(command=lambda: eliminar_usuario(id_usuario))
            editar_button.pack(side="left", padx=10, pady=5)
            eliminar_button.pack(side="left", padx=10, pady=5)
        else:
            editar_button.pack_forget()
            eliminar_button.pack_forget()

    tabla_usuarios.bind("<<TreeviewSelect>>", seleccionar_usuario)
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#METODOS_INVENTARIO
#Funcion de la data de inventario
def datos_tabla_inventario(tabla):
    #conexion global
    global conexion

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
    #conexion global
    global conexion

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
        
def editar_producto(id_producto):
    producto = consultar_producto(id_producto)
    # Puedes utilizar el valor de id_producto para identificar y editar el producto correspondiente.
    print(f"Editar producto con ID: {id_producto}")
    # Abrir la ventana proveedor
    ventana_editar_producto = tk.Toplevel()
    ventana_editar_producto.title("Editar producto")
    ventana_editar_producto.configure(bg="white")

    formulario_editar = tk.Frame(ventana_editar_producto, bg="#1b2838", padx=20, pady=20, borderwidth=2, relief="groove")
    formulario_editar.pack(padx=20, pady=20)

    titulo_label = tk.Label(formulario_editar, text="Editar producto:", bg="black", fg="white")
    titulo_label.pack(pady=10)

    descripcion_producto_label = tk.Label(formulario_editar, text="Descripcion producto:", bg="black", fg="white")
    descripcion_producto_label.pack(pady=5)

    descripcion_producto_editar = tk.Entry(formulario_editar, bg="white")
    descripcion_producto_editar.pack(pady=5)
    descripcion_producto_editar.insert(0, producto.get("descripcion_producto", ""))

    categoria_label = tk.Label(formulario_editar, text="Categoria:", bg="black", fg="white")
    categoria_label.pack(pady=5)

    categoria_entry = tk.Entry(formulario_editar, bg="white")
    categoria_entry.pack(pady=5)
    categoria_entry.insert(0, producto.get("id_categoria", ""))

    cantidad_label = tk.Label(formulario_editar, text="Cantidad total:", bg="black", fg="white")
    cantidad_label.pack(pady=5)

    cantidad_entry = tk.Entry(formulario_editar, bg="white")
    cantidad_entry.pack(pady=5)
    cantidad_entry.insert(0, producto.get("cantidad_total", ""))

    costo_mayor_label = tk.Label(formulario_editar, text="Costo mayor:", bg="black", fg="white")
    costo_mayor_label.pack(pady=5)

    costo_mayor_entry = tk.Entry(formulario_editar, bg="white")
    costo_mayor_entry.pack(pady=5)
    costo_mayor_entry.insert(0, producto.get("costo_mayor", ""))

    precio_unitario_label = tk.Label(formulario_editar, text="Precio Unitario:", bg="black", fg="white")
    precio_unitario_label.pack(pady=5)

    precio_unitario_entry = tk.Entry(formulario_editar, bg="white")
    precio_unitario_entry.pack(pady=5)
    precio_unitario_entry.insert(0, producto.get("precio_unitario", ""))

    fecha_vencimiento_label = tk.Label(formulario_editar, text="Fecha de vencimiento:", bg="black", fg="white")
    fecha_vencimiento_label.pack(pady=5)

    fecha_vencimiento_entry = tk.Entry(formulario_editar, bg="white")
    fecha_vencimiento_entry.pack(pady=5)
    fecha_vencimiento_entry.insert(0, producto.get("fecha_vencimiento", ""))

    proveedor_label = tk.Label(formulario_editar, text="Proveedor:", bg="black", fg="white")
    proveedor_label.pack(pady=5)

    proveedor_entry = tk.Entry(formulario_editar, bg="white")
    proveedor_entry.pack(pady=5)
    proveedor_entry.insert(0, producto.get("id_proveedor", ""))


    def editar_datos_producto():
        global conexion #definimos la variable conexion como global
        descripcion_producto = descripcion_producto_editar.get()
        categoria= categoria_entry.get()
        cantidad = cantidad_entry.get()
        costo_mayor= costo_mayor_entry.get()
        precio_unitario= precio_unitario_entry.get()
        fecha_vencimiento= fecha_vencimiento_entry.get()
        proveedor= proveedor_entry.get()
        
        #creamos una sentencia para guardar los datos en la base de datos
        try:
            # Crear la sentencia SQL para actualizar el producto en la base de datos
            sentencia = "UPDATE productos SET descripcion_producto = %s, id_categoria = %s, cantidad_total = %s, costo_mayor = %s, precio_unitario = %s, fecha_vencimiento = %s, id_proveedor = %s  WHERE id_producto = %s"
            datos = (descripcion_producto, categoria, cantidad, costo_mayor, precio_unitario, fecha_vencimiento, proveedor,  id_producto)

            cursor = conexion.cursor()
            cursor.execute(sentencia, datos)
            conexion.commit()

            #actualizar tabla
            datos_tabla_inventario(tabla_inventario)

            cursor.close()
            ventana_editar_producto.destroy()

            messagebox.showinfo("Producto editar", 'Se ha editado el producto correctamente')
        except Exception as e:
            conexion.rollback()
            messagebox.showerror("Error", f"No se ha podido editar el producto: {str(e)}")

    # Botón de guardar producto
    boton_editar_producto = tk.Button(formulario_editar, text="Editar Producto", command=editar_datos_producto, activebackground="#F50743", font=("helvetica", 12))
    boton_editar_producto.pack(pady=10, ipadx=10)   

def eliminar_producto(id_producto):
    # Aquí debes implementar la lógica para eliminar el producto con el ID proporcionado.
    # Puedes utilizar el valor de id_producto para identificar y eliminar el producto correspondiente.
    print(f"Eliminar producto con ID: {id_producto}")
    global conexion #definimos la variable conexion como global
    try:
         # Crear un cursor
        cursor = conexion.cursor()

        # Consulta para obtener información del producto
        consulta = f"SELECT descripcion_producto FROM productos WHERE id_producto = {id_producto}"
        cursor.execute(consulta)
        descripcion_producto = cursor.fetchone()

        # Verificar si se encontró el producto
        if descripcion_producto is None:
            messagebox.showinfo("Información", f"No se encontró un producto con el ID {id_producto}")
        else:
            nombre_producto = descripcion_producto[0]

            # Crear una ventana Tkinter para la confirmación
            ventana_confirmacion = tk.Tk()
            ventana_confirmacion.title("Confirmación")

            # Función para eliminar el producto
            def confirmar_eliminar():
                # Consulta para eliminar al producto
                consulta_eliminar = f"DELETE FROM productos WHERE id_producto = {id_producto}"
                cursor.execute(consulta_eliminar)
                conexion.commit()
                #actualizar tabla
                datos_tabla_inventario(tabla_inventario)
                messagebox.showinfo("Información", f"Producto '{nombre_producto}' (ID: {id_producto}) ha sido eliminado.")
                ventana_confirmacion.destroy()

            # Función para cancelar la eliminación
            def cancelar_eliminar():
                messagebox.showinfo("Información", "Operación de eliminación cancelada.")
                ventana_confirmacion.destroy()

            # Etiqueta de confirmación
            etiqueta_confirmacion = tk.Label(ventana_confirmacion, text=f"¿Estás seguro de eliminar el producto '{nombre_producto}' (ID: {id_producto})?")
            etiqueta_confirmacion.pack()

            # Botones de confirmar y cancelar
            boton_confirmar = tk.Button(ventana_confirmacion, text="Confirmar", command=confirmar_eliminar)
            boton_cancelar = tk.Button(ventana_confirmacion, text="Cancelar", command=cancelar_eliminar)

            boton_confirmar.pack()
            boton_cancelar.pack()

            ventana_confirmacion.mainloop()
    except Exception as e:
        conexion.rollback()
        messagebox.showerror("Error", f"No se ha podido eliminar el producto: {str(e)}")            

#metodo del boton2
def Inventario():
    etiqueta_titulo.config(text="Inventario General")
    global tabla_usuarios, boton_guardar_usuario, tabla_inventario, boton_guardar_inventario,tabla_proveedor,boton_crear_proveedor,tabla_movimientos, editar_button, eliminar_button, entrada_busqueda, boton_buscar

    #si ya existe la tabla usuarios/ destruir
    if tabla_usuarios and tabla_usuarios.winfo_exists():
        tabla_usuarios.destroy()
        #si ya existe la tabla inventario/ destruir
    
    if tabla_inventario:
        tabla_inventario.destroy()

    if boton_guardar_usuario and boton_guardar_usuario.winfo_exists():
        boton_guardar_usuario.destroy()

    if tabla_proveedor and tabla_proveedor.winfo_exists():
        tabla_proveedor.destroy()

    if boton_crear_proveedor and boton_crear_proveedor.winfo_exists():
        boton_crear_proveedor.destroy()

    if boton_guardar_inventario and boton_guardar_inventario.winfo_exists():
        boton_guardar_inventario.destroy()  

    if tabla_movimientos and tabla_movimientos.winfo_exists():
        tabla_movimientos.destroy()

    if boton_guardar_inventario: 
        boton_guardar_inventario.destroy()

    if boton_guardar_inventario: 
        boton_guardar_inventario.destroy()

    if editar_button: 
        editar_button.destroy()   

    if eliminar_button: 
        eliminar_button.destroy()     

    if entrada_busqueda:
        entrada_busqueda.destroy()
    
    if boton_buscar:
        boton_buscar.destroy()
     
    #aplicar tema x
    estilo= ttk.Style()
    estilo.configure("Custom.Treeview.Heading", font=("Arial", 12, "bold"))
    estilo.configure("Custom.Treeview", font=("Arial", 10), background="#ececec", fieldbackground="#ececec")   
    
    #contenido 
    contenido.config(text="Inventario de los Productos de Cinelandia")

    #crear la tabla de inventario del contenedor derecho
    tabla_inventario = ttk.Treeview(contenido, columns=("#", "descripcion_producto", "cantidad_total", "fecha_vencimiento", "id_proveedor", "costo_mayor", "precio_unitario"), show="headings", style="Custom.Treeview")

    entrada_busqueda = tk.Entry(contenido)
    entrada_busqueda.pack(side=tk.TOP)

    boton_buscar = tk.Button(contenido, text="Buscar", command=lambda: buscar(tabla_inventario, entrada_busqueda))
    boton_buscar.pack(side=tk.TOP)

    tabla_inventario.heading("#", text="ID") 
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
    boton_guardar_inventario=tk.Button(contenido,text="crear producto", command=crear_producto)
    boton_guardar_inventario.pack(side="left",padx=10,pady=5)

    # Botones Editar y Eliminar (ocultos inicialmente)
    editar_button = tk.Button(contenido, text="Editar", command=lambda: editar_producto(id_producto))
    eliminar_button = tk.Button(contenido, text="Eliminar", command=lambda: eliminar_producto(id_producto))

    # Configurar la acción de selección de inventario
    def seleccionar_producto(event):
        item_seleccionado = tabla_inventario.selection()
        if item_seleccionado:
            id_producto = tabla_inventario.item(item_seleccionado, "values")[0]
            editar_button.configure(command=lambda: editar_producto(id_producto))
            eliminar_button.configure(command=lambda: eliminar_producto(id_producto))
            editar_button.pack(side="left", padx=10, pady=5)
            eliminar_button.pack(side="left", padx=10, pady=5)
        else:
            editar_button.pack_forget()
            eliminar_button.pack_forget()

    tabla_inventario.bind("<<TreeviewSelect>>", seleccionar_producto)

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# METODOS_PROVEEDOR
# Funcion de la data de proveedores
def datos_tabla_proveedor(tabla):
    #conexion global
    global conexion

    #eliminamos todos lo elementos antes de actualizar
    tabla.delete(*tabla.get_children())

    cursor = conexion.cursor()
    cursor.execute("select id_proveedor, nombre, codigo, id_prefijo_documento from proveedor")
    resultado= cursor.fetchall()
    for id_proveedor, nombre, codigo, id_prefijo_documento in resultado:

        #insercion de datos
        tabla.insert("", "end", values=(id_proveedor, nombre, codigo, id_prefijo_documento))

def crear_proveedor():
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
    documento_label = tk.Label(formulario_crear, text="Prefijo Documento:", bg="black", fg="white")
    documento_label.pack(pady=5)

    # Cuadro de entrada de cantidad
    documento_crear = tk.Entry(formulario_crear, bg="white")
    documento_crear.pack(pady=5)

    def guardar_proveedor():
        global conexion #definimos la variable conexion como global
        nombre = proveedor_crear.get()
        codigo= codigo_entry.get()
        prefijo_documento=documento_crear.get()
        
        fecha_actual=datetime.date.today()
     
            #creamos una sentencia para guardar los datos en la base de datos
        try:
            #abrir cursor
            cursor=conexion.cursor()
            consulta="INSERT INTO proveedor (nombre, codigo, id_prefijo_documento) VALUES (%s, %s, %s)"
            cursor.execute(consulta, (nombre, codigo, prefijo_documento))

            conexion.commit()
            #actualizar tabla
            datos_tabla_proveedor(tabla_proveedor)

            cursor.close()
            ventana_crear_proveedor.destroy()

            messagebox.showinfo("Proveedor creado", 'Se ha registrado el proveedor correctamente')
        except Exception as e:
            conexion.rollback()
            messagebox.showerror("Error", f"No se ha podido registrar el proveedor: {str(e)}")

    # Botón de guardar producto
    boton_guardar_proveedor = tk.Button(formulario_crear, text="Guardar Proveedor", command=guardar_proveedor, activebackground="#F50743", font=("helvetica", 12))
    boton_guardar_proveedor.pack(pady=10, ipadx=10)

# Función para consultar un proveedor en MySQL
def consultar_proveedor(id_proveedor):
    #conexion global
    global conexion

    cursor = conexion.cursor(dictionary=True)  # Utiliza dictionary=True para obtener un diccionario
    # Consultar el usuario por ID
    try:
        consulta = "SELECT nombre, codigo, id_prefijo_documento FROM proveedor WHERE id_proveedor = %s"
        cursor.execute(consulta, (id_proveedor,))
        Proveedor = cursor.fetchone()

        cursor.close()

        return Proveedor

    except Exception as e:
        conexion.rollback()
        messagebox.showerror("Error", f"No se ha podido consultar el proveedor: {str(e)}")
        
def editar_proveedor(id_proveedor):
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

    prefijo_documento_label = tk.Label(formulario_editar, text="Prefijo Documento:", bg="black", fg="white")
    prefijo_documento_label.pack(pady=5)

    prefijo_documento_entry = tk.Entry(formulario_editar, bg="white")
    prefijo_documento_entry.pack(pady=5)
    prefijo_documento_entry.insert(0, proveedor.get("id_prefijo_documento", ""))

    def editar_datos_proveedor():
        global conexion #definimos la variable conexion como global
        nombre = proveedor_editar.get()
        codigo = codigo_editar.get()
        id_prefijo_documento= prefijo_documento_entry.get()
    
        #creamos una sentencia para guardar los datos en la base de datos
        try:
            # Crear la sentencia SQL para actualizar el proveedor en la base de datos
            sentencia = "UPDATE proveedor SET nombre = %s, codigo = %s, id_prefijo_documento = %s WHERE id_proveedor = %s"
            datos = (nombre, codigo, id_prefijo_documento, id_proveedor)

            cursor = conexion.cursor()
            cursor.execute(sentencia, datos)
            conexion.commit()

            #actualizar tabla
            datos_tabla_proveedor(tabla_proveedor)

            cursor.close()
            ventana_editar_proveedor.destroy()

            messagebox.showinfo("Proveedor editar", 'Se ha editado el proveedor correctamente')
        except Exception as e:
            conexion.rollback()
            messagebox.showerror("Error", f"No se ha podido editar el proveedor: {str(e)}")

    # Botón de guardar proveedor
    boton_editar_proveedor = tk.Button(formulario_editar, text="Editar Proveedor", command=editar_datos_proveedor, activebackground="#F50743", font=("helvetica", 12))
    boton_editar_proveedor.pack(pady=10, ipadx=10)

def eliminar_proveedor(id_proveedor):
    # Aquí debes implementar la lógica para eliminar el usuario con el ID proporcionado.
    # Puedes utilizar el valor de id_usuario para identificar y eliminar el usuario correspondiente.
    print(f"Eliminar proveedor con ID: {id_proveedor}")
    global conexion #definimos la variable conexion como global
    try:
         # Crear un cursor
        cursor = conexion.cursor()

        # Consulta para obtener información del usuario
        consulta = f"SELECT nombre FROM proveedor WHERE id_proveedor = {id_proveedor}"
        cursor.execute(consulta)
        nombre = cursor.fetchone()

        # Verificar si se encontró el usuario
        if nombre is None:
            messagebox.showinfo("Información", f"No se encontró un proveedor con el ID {id_proveedor}")
        else:
            nombre_proveedor = nombre[0]

            # Crear una ventana Tkinter para la confirmación
            ventana_confirmacion = tk.Tk()
            ventana_confirmacion.title("Confirmación")

            # Función para eliminar el usuario
            def confirmar_eliminar():
                # Consulta para eliminar al usuario
                consulta_eliminar = f"DELETE FROM proveedor WHERE id_proveedor = {id_proveedor}"
                cursor.execute(consulta_eliminar)

                conexion.commit()
                #actualizar tabla
                datos_tabla_proveedor(tabla_proveedor)
                messagebox.showinfo("Información", f"Proveedor '{nombre_proveedor}' (ID: {id_proveedor}) ha sido eliminado.")
                ventana_confirmacion.destroy()

            # Función para cancelar la eliminación
            def cancelar_eliminar():
                messagebox.showinfo("Información", "Operación de eliminación cancelada.")
                ventana_confirmacion.destroy()

            # Etiqueta de confirmación
            etiqueta_confirmacion = tk.Label(ventana_confirmacion, text=f"¿Estás seguro de eliminar el proveedor '{nombre_proveedor}' (ID: {id_proveedor})?")
            etiqueta_confirmacion.pack()

            # Botones de confirmar y cancelar
            boton_confirmar = tk.Button(ventana_confirmacion, text="Confirmar", command=confirmar_eliminar)
            boton_cancelar = tk.Button(ventana_confirmacion, text="Cancelar", command=cancelar_eliminar)

            boton_confirmar.pack()
            boton_cancelar.pack()

            ventana_confirmacion.mainloop()
    except Exception as e:
        conexion.rollback()
        messagebox.showerror("Error", f"No se ha podido eliminar el proveedor: {str(e)}")            

#metodo del boton3
def Proveedor():
    etiqueta_titulo.config(text="Proveedor")
    global tabla_usuarios, boton_guardar_usuario, tabla_inventario, boton_guardar_inventario,tabla_proveedor,boton_crear_proveedor, tabla_movimientos, editar_button, eliminar_button, entrada_busqueda, boton_buscar
    #si ya existe la tabla usuarios/ destruir
    if tabla_usuarios and tabla_usuarios.winfo_exists():
        tabla_usuarios.destroy()
    #si ya existe la tabla inventario/ destruir

    if tabla_inventario and tabla_inventario.winfo_exists():
        tabla_inventario.destroy()

    if boton_guardar_usuario and boton_guardar_usuario.winfo_exists():
        boton_guardar_usuario.destroy()

    if tabla_proveedor and tabla_proveedor.winfo_exists():
        tabla_proveedor.destroy()

    if boton_crear_proveedor and boton_crear_proveedor.winfo_exists():
        boton_crear_proveedor.destroy()

    if boton_guardar_inventario and boton_guardar_inventario.winfo_exists():
        boton_guardar_inventario.destroy() 
    
    if tabla_movimientos and tabla_movimientos.winfo_exists():
        tabla_movimientos.destroy()

    if boton_guardar_inventario: 
        boton_guardar_inventario.destroy()

    if editar_button: 
        editar_button.destroy()   

    if eliminar_button: 
        eliminar_button.destroy()     

    if entrada_busqueda:
        entrada_busqueda.destroy()
    
    if boton_buscar:
        boton_buscar.destroy()
        
    #aplicar tema x
    estilo= ttk.Style()
    estilo.configure("Custom.Treeview.Heading", font=("Arial", 12, "bold"))
    estilo.configure("Custom.Treeview", font=("Arial", 10), background="#ececec", fieldbackground="#ececec")  
   
    #contenido 
    contenido.config(text="Inventario de los Productos de Cinelandia")

    #crear la tabla de inventario del contenedor derecho
    tabla_proveedor = ttk.Treeview(contenido, columns=("#", "nombre", "codigo","id_prefijo_documento"), show="headings", style="Custom.Treeview")

    entrada_busqueda = tk.Entry(contenido)
    entrada_busqueda.pack(side=tk.TOP)

    boton_buscar = tk.Button(contenido, text="Buscar", command=lambda: buscar(tabla_proveedor, entrada_busqueda))
    boton_buscar.pack(side=tk.TOP)

    tabla_proveedor.heading("#", text="ID") 
    tabla_proveedor.heading("nombre", text="Proveedor") 
    tabla_proveedor.heading("codigo", text="Rif")
    tabla_proveedor.heading("id_prefijo_documento", text="Documento")
    

    #ajustar tamaño de columnas
    tabla_proveedor.column("#", width=25)
    tabla_proveedor.column("nombre", width=150)
    tabla_proveedor.column("codigo", width=150)
    tabla_proveedor.column("id_prefijo_documento",width=150)
    

    #contenido de la tabla
    datos_tabla_proveedor(tabla_proveedor)

    #mostrar la tabla en el contenedor derecho
    tabla_proveedor.pack(fill="both",expand=True)

    #boton de crear proveedor
    boton_crear_proveedor=tk.Button(contenido,text="crear proveedor", command=crear_proveedor)
    boton_crear_proveedor.pack(side="left",padx=10,pady=5)
    
    # Botones Editar y Eliminar (ocultos inicialmente)
    editar_button = tk.Button(contenido, text="Editar", command=lambda: editar_proveedor(id_proveedor))
    eliminar_button = tk.Button(contenido, text="Eliminar", command=lambda: eliminar_proveedor(id_proveedor))

    # Configurar la acción de selección de proveedor
    def seleccionar_proveedor(event):
        item_seleccionado = tabla_proveedor.selection()
        if item_seleccionado:
            id_proveedor = tabla_proveedor.item(item_seleccionado, "values")[0]
            editar_button.configure(command=lambda: editar_proveedor(id_proveedor))
            eliminar_button.configure(command=lambda: eliminar_proveedor(id_proveedor))
            editar_button.pack(side="left", padx=10, pady=5)
            eliminar_button.pack(side="left", padx=10, pady=5)
        else:
            editar_button.pack_forget()
            eliminar_button.pack_forget()

    tabla_proveedor.bind("<<TreeviewSelect>>", seleccionar_proveedor)



#metodo del boton4
def Movimientos():
    etiqueta_titulo.config(text="Movimientos")
    global tabla_usuarios, boton_guardar_usuario, tabla_inventario, boton_guardar_inventario,tabla_proveedor,boton_crear_proveedor, tabla_movimientos, editar_button, eliminar_button, entrada_busqueda, boton_buscar
    #si ya existe la tabla usuarios/ destruir
    if tabla_usuarios and tabla_usuarios.winfo_exists():
        tabla_usuarios.destroy()
    #si ya existe la tabla inventario/ destruir

    if tabla_inventario and tabla_inventario.winfo_exists():
        tabla_inventario.destroy()

    if boton_guardar_usuario and boton_guardar_usuario.winfo_exists():
        boton_guardar_usuario.destroy()

    if tabla_proveedor and tabla_proveedor.winfo_exists():
        tabla_proveedor.destroy()

    if boton_crear_proveedor and boton_crear_proveedor.winfo_exists():
        boton_crear_proveedor.destroy()

    if boton_guardar_inventario and boton_guardar_inventario.winfo_exists():
        boton_guardar_inventario.destroy() 
    
    if tabla_movimientos and tabla_movimientos.winfo_exists():
        tabla_movimientos.destroy()
    
    if boton_guardar_inventario: 
        boton_guardar_inventario.destroy()

    if editar_button: 
        editar_button.destroy()   

    if eliminar_button: 
        eliminar_button.destroy()     

    if entrada_busqueda:
        entrada_busqueda.destroy()
    
    if boton_buscar:
        boton_buscar.destroy()

    #aplicar tema x
    estilo= ttk.Style()
    estilo.configure("Custom.Treeview.Heading", font=("Arial", 12, "bold"))
    estilo.configure("Custom.Treeview", font=("Arial", 10), background="#ececec", fieldbackground="#ececec")      
   
    #contenido 
    contenido.config(text="Movimientos de los Productos de Cinelandia")

    #crear la tabla de inventario del contenedor derecho
    tabla_movimientos = ttk.Treeview(contenido, columns=("id", "descripcion","status", "total"), show="headings", style="Custom.Treeview")

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

# Metodo de inicio de session
def iniciar_sesion():
    global conexion #definimos la variable conexion como global
    usuario = usuario_entry.get()
    contrasena = password_entry.get()

    #conexion a la base de datos
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "cinelandia"
    )

    cursor= conexion.cursor()
    cursor.execute("select usuario from usuario where usuario = %s and contraseña = %s", (usuario,contrasena))    
    resultado= cursor.fetchone()

    # Verificar las credenciales de inicio de sesión
    if resultado is not None: 
        messagebox.showinfo("Inicio de sesión exitoso", f"Bienvenido, {usuario}!")
        ventana.withdraw()  # Ocultar la ventana de inicio de sesión

        # Obtener el ancho y alto de la pantalla
        ancho_pantalla = ventana.winfo_screenwidth()
        alto_pantalla = ventana.winfo_screenheight()

        # Abrir la ventana del panel
        ventana_dashboard = tk.Toplevel()
        ventana_dashboard.title("Panel")
        ventana_dashboard.configure(bg="#1b2838")

        # Establecer el tamaño y posición de la ventana
        ventana_dashboard.geometry(f"{ancho_pantalla}x{alto_pantalla}+0+0")

        # Panel vertical izquierdo (Menú)
        panel_izquierdo = tk.Frame(ventana_dashboard, bg="#2c3e50",  width=300)
        panel_izquierdo.pack(side="left", fill="y")

        # Elementos del menú
        etiqueta_menu = tk.Label(panel_izquierdo, text="Menú", bg="light gray", font=("Arial", 16, "bold"))
        etiqueta_menu.pack(pady=10)

        # Opción 1
        opcion1 = tk.Button(panel_izquierdo, text="Usuarios", bg="#2c3e50", fg="white", padx=10, pady=5, command=usuarios, relief="flat")
        opcion1.pack(pady=5)
        opcion1.config(cursor="hand2")  # Cambia el cursor a una mano (pointer)

        # Opción 2
        opcion2 = tk.Button(panel_izquierdo, text="Inventario", bg="#2c3e50", fg="white", padx=10, pady=5, command=Inventario, relief="flat")
        opcion2.pack(pady=5)
        opcion2.config(cursor="hand2")  # Cambia el cursor a una mano (pointer)

        # Opción 3
        opcion3 = tk.Button(panel_izquierdo, text="Proveedores", bg="#2c3e50", fg="white", padx=10, pady=5, command=Proveedor, relief="flat")
        opcion3.pack(pady=5)
        opcion3.config(cursor="hand2")  # Cambia el cursor a una mano (pointer)

        # Opción 4
        opcion4 = tk.Button(panel_izquierdo, text="Movimientos", bg="#2c3e50", fg="white", padx=10, pady=5, command=Movimientos, relief="flat")
        opcion4.pack(pady=5)
        opcion4.config(cursor="hand2")  # Cambia el cursor a una mano (pointer)

        # Agregar recuadro inferior
        recuadro_inferior = tk.Frame(panel_izquierdo, bg="#2c3e50", bd=1, relief="solid")
        recuadro_inferior.pack(side="bottom", fill="x")

        # Puedes reemplazar 'ruta_imagen.png' con la ruta de tu imagen
        imagen = tk.PhotoImage(file="imagenes/user.png")
        imagen = redimensionar_imagen(imagen, 50, 50),
        imagen_label = tk.Label(recuadro_inferior, image=imagen, bg="#2c3e50")
        imagen_label.image = imagen
        imagen_label.pack(side="top", padx=10)

        # Agregar icono de configuración
        icono_configuracion = tk.PhotoImage(file='imagenes/settings.png')
        icono_configuracion = redimensionar_imagen(icono_configuracion, 25, 25)
        icono_label = tk.Label(recuadro_inferior, image=icono_configuracion, bg="#2c3e50")
        icono_label.image = icono_configuracion
        icono_label.pack(side="right", padx=10)

        # Agregar rol
        rol_label = tk.Label(recuadro_inferior, text="Username: Admin", bg="#2c3e50", fg="white")
        rol_label.pack(padx=10)

        username = tk.Label(recuadro_inferior, text="Rol: Administrador", bg="#2c3e50", fg="white")
        username.pack(padx=10)

        # Contenedor a la derecha
        contenedor_derecho = tk.Frame(ventana_dashboard, bg="#1b2838")
        contenedor_derecho.pack(side="right", fill="both", expand=True)

        # Contenedor resaltado
        contenedor_resaltado = tk.Frame(contenedor_derecho, bg="#2c3e50", padx=20, pady=20)
        contenedor_resaltado.pack(pady=10)

        #elementos del contenedor derecho
        global etiqueta_titulo, contenido

        # Agregar elementos al contenedor resaltado
        etiqueta_titulo = tk.Label(contenedor_resaltado, text="Contenido", bg="white", font=("Arial", 16, "bold"))
        etiqueta_titulo.pack(pady=10)

        contenido = tk.Label(contenedor_resaltado, text="Aquí va el contenido del menú seleccionado", bg="white")
        contenido.pack(pady=5)

        #configuramos el cierre de ventana
        ventana_dashboard.protocol("WM_DELETE_WINDOW", lambda:cerrar_sesion(ventana_dashboard))

        ventana_dashboard.mainloop()
        conexion.close()
        ventana_dashboard.destroy()
    else:
        messagebox.showerror("Inicio de sesión fallido", "Credenciales incorrectas")

# Función para manejar el evento Enter en la ventana principal
def on_enter(event):
    iniciar_sesion()

# Función para cambiar la imagen en el carrusel
def cambiar_imagen(index):
    global imagen_actual
    imagen_actual = index
    imagen = imagenes[imagen_actual]
    imagen_carrusel.configure(image=imagen)
    imagen_carrusel.image = imagen

# Función para avanzar automáticamente el carrusel
def avanzar_carrusel():
    global imagen_actual
    # Calcula el índice de la siguiente imagen
    siguiente_indice = (imagen_actual + 1) % len(imagenes)
    cambiar_imagen(siguiente_indice)
    ventana.after(3000, avanzar_carrusel)  # Cambia la imagen cada 3000 milisegundos (3 segundos)

# Función para redimensionar una imagen
def redimensionar_imagen(imagen, ancho, alto):
    return imagen.subsample(int(imagen.width() / ancho), int(imagen.height() / alto))

# Ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Inventario")
ventana.geometry("800x400")
ventana.configure(bg="#1b2838")  # Cambia el color de fondo de la ventana


# Marco principal para la disposición
marco_principal = tk.Frame(ventana, bg="#1b2838")
marco_principal.place(relx=0, rely=0, relwidth=1, relheight=1)

# Título
titulo_marco = tk.Label(marco_principal, text="Sistema inventario Cinelandia", bg="#2c3e50", fg="white", font=("Helvetica", 16, "bold"))
titulo_marco.place(relx=0.55, rely=0.05, relwidth=0.4, relheight=0.1)  # Ajusta el valor de relx para mover el título a la izquierda

# Marco para el carrusel de imágenes a la izquierda
carrusel_marco = tk.Frame(marco_principal, bg="#1b2838")
carrusel_marco.place(relx=0, rely=0, relwidth=0.55, relheight=0.95)

# Cargar las imágenes
imagen1 = tk.PhotoImage(file="imagenes/img.png")
imagen2 = tk.PhotoImage(file="imagenes/img2.png")
imagen3 = tk.PhotoImage(file="imagenes/img.png")
img_user = tk.PhotoImage(file="imagenes/user.png")

ancho_deseado = 240  # Especifica el ancho deseado para las imágenes
alto_deseado = 280   # Especifica el alto deseado para las imágenes

# Lista de imágenes para el carrusel
imagenes = [
    redimensionar_imagen(imagen1, ancho_deseado, alto_deseado),
    redimensionar_imagen(imagen2, ancho_deseado, alto_deseado),
    redimensionar_imagen(imagen3, ancho_deseado, alto_deseado)
]

# Variable para rastrear la imagen actual en el carrusel
imagen_actual = 0

# Etiqueta para el carrusel
imagen_carrusel = tk.Label(carrusel_marco, image=imagenes[0], bg="#1b2838")
imagen_carrusel.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

# Indicadores de imágenes (puntos)
indicadores = []
for i in range(len(imagenes)):
    indicador = tk.Label(carrusel_marco, text="●", font=("Helvetica", 14), bg="#1b2838", fg="white", activebackground="#F50743")
    indicador.bind("<Button-1>", lambda event, index=i: cambiar_imagen(index))
    indicadores.append(indicador)
    indicador.place(relx=0.43 + i * 0.05, rely=0.80)

# Marco para el formulario a la derecha con borde
formulario_frame = tk.Frame(marco_principal, bg="#2c3e50", bd=5)
formulario_frame.place(relx=0.55, rely=0.25, relwidth=0.4, relheight=0.5)

# Título del formulario
titulo_label = tk.Label(formulario_frame, text="Iniciar Sesión", bg="#2c3e50", fg="white", font=("Helvetica", 16, "bold"))
titulo_label.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

# Imagen centrada
# Reemplaza "imagen_central.png" con la ruta de tu imagen
imagen_central = redimensionar_imagen(img_user, 50, 50),
imagen_label = tk.Label(formulario_frame, image=imagen_central, bg="#2c3e50")
imagen_label.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.3)

# Etiqueta de usuario
usuario_label = tk.Label(formulario_frame, text="Usuario:", bg="#2c3e50", fg="white")
usuario_label.place(relx=0.1, rely=0.6, relwidth=0.3, relheight=0.1)

# Cuadro de entrada de usuario
usuario_entry = tk.Entry(formulario_frame, bg="white")
usuario_entry.place(relx=0.4, rely=0.6, relwidth=0.5, relheight=0.1)

# Etiqueta de contraseña
password_label = tk.Label(formulario_frame, text="Contraseña:", bg="#2c3e50", fg="white")
password_label.place(relx=0.1, rely=0.7, relwidth=0.3, relheight=0.1)

# Cuadro de entrada de contraseña
password_entry = tk.Entry(formulario_frame, show="*", bg="white")
password_entry.place(relx=0.4, rely=0.7, relwidth=0.5, relheight=0.1)

# Botón de inicio de sesión
boton_iniciar_sesion = tk.Button(formulario_frame, text="Iniciar sesión", command=iniciar_sesion, bg="#1b2838", fg="white", activebackground="#F50743")
boton_iniciar_sesion.place(relx=0.4, rely=0.85, relwidth=0.5, relheight=0.1)

# Configura el evento Enter en la ventana principal
ventana.bind("<Return>", on_enter)

# Inicia el carrusel automático
avanzar_carrusel()

# Ejecutar la aplicación
ventana.mainloop()

ventana.destroy()