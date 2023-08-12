import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import datetime
global conexion
tabla_usuarios=None
tabla_inventario=None

boton_guardar_usuario=None

#metodo de cerrar ventanas
def cerrar_sesion(ventana_dashboard):
    #cerramos la ventana del dashboard
    ventana_dashboard.destroy()
    ventana.destroy()

#Funcion de la data de usuario
def datos_tabla_usuarios(tabla):
    #conexion global
    global conexion

    #eliminamos todos lo elementos antes de actualizar
    tabla.delete(*tabla.get_children())

    cursor = conexion.cursor()
    cursor.execute("select usuario, fecha_ingreso, id_cargo from usuario")
    resultado= cursor.fetchall()
    for usuario, fecha_ingreso, id_cargo in resultado:

        #insercion de datos
        tabla.insert("", "end", values=(usuario, id_cargo, fecha_ingreso))

#Funcion de la data de inventario
def datos_tabla_inventario(tabla):
    #conexion global
    global conexion
    cursor = conexion.cursor()
    cursor.execute("select descripcion_producto, cantidad_total, fecha_vencimiento, id_proveedor, costo_mayor from productos")
    resultado= cursor.fetchall()
    for descripcion_producto, cantidad_total, fecha_vencimiento, id_proveedor, costo_mayor in resultado:

        #insercion de datos
        tabla.insert("", "end", values=(descripcion_producto, cantidad_total, fecha_vencimiento, id_proveedor, costo_mayor))        
  
def crear_usuario():
    # Abrir la ventana usuario
    ventana_crear_usuario = tk.Toplevel()
    ventana_crear_usuario.title("crear usuario")
    ventana_crear_usuario.configure(bg="white")
   
    # Crear un marco para el formulario
    formulario_crear = tk.Frame(ventana_crear_usuario , bg="pink", padx=20, pady=20, borderwidth=2, relief="groove")
    formulario_crear.pack(padx=20, pady=20)

    titulo_label = tk.Label(formulario_crear, text="Crear Usuario:", bg="black", fg="white")
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
    
#metodo del boton1
def usuarios():
    etiqueta_titulo.config(text="Usuarios del sistema")
    global tabla_usuarios, boton_guardar_usuario
    if tabla_usuarios and tabla_usuarios.winfo_exists():
        tabla_usuarios.destroy()
    #si ya existe la tabla inventario/ destruir
    global tabla_inventario
    if tabla_inventario and tabla_inventario.winfo_exists():
        tabla_inventario.destroy()

    if boton_guardar_usuario and boton_guardar_usuario.winfo_exists():
        boton_guardar_usuario.destroy()

    #aplicar tema x
    estilo= ttk.Style()
    estilo.theme_use("clam")

    #crear la tabla de usuario del contenedor derecho
    tabla_usuarios = ttk.Treeview(contenido, columns=("Usuario", "Rol", "horario", "boton1", "boton2", "boton3"), show="headings")

    tabla_usuarios.heading("Usuario", text="Usuario del Sistema") 
    tabla_usuarios.heading("Rol", text="Rol del Usuario")
    tabla_usuarios.heading("horario", text="Horario de entrada")
    tabla_usuarios.heading("boton1", text="ver usuario")
    tabla_usuarios.heading("boton2", text="editar usuario")
    tabla_usuarios.heading("boton3", text="eliminar usuario")

    #ajustar tamaño de columnas
    tabla_usuarios.column("Usuario", width=100)
    tabla_usuarios.column("Rol", width=100)
    tabla_usuarios.column("horario",width=100)
    tabla_usuarios.column("boton1", width=50)
    tabla_usuarios.column("boton2", width=50)
    tabla_usuarios.column("boton3",width=50)

    #contenido de la tabla
    datos_tabla_usuarios(tabla_usuarios)

    #mostrar la tabla en el contenedor derecho
    tabla_usuarios.pack(fill="both",expand=True)

    #boton de crear usuario
    boton_guardar_usuario=tk.Button(contenido,text="crear usuario", command=crear_usuario)
    boton_guardar_usuario.pack(side="left",padx=10,pady=5)

#crear formulario de inventario

#metodo del boton2
def Inventario():
    etiqueta_titulo.config(text="Inventario General")
#si ya existe la tabla usuarios/ destruir
    if tabla_usuarios and tabla_usuarios.winfo_exists():
        tabla_usuarios.destroy()
#si ya existe la tabla inventario/ destruir
    global tabla_inventario
    if tabla_inventario:
        tabla_inventario.destroy()
    if boton_guardar_usuario: 
        boton_guardar_usuario.destroy()
    #contenido 
    contenido.config(text="Inventario de los Productos de Cinelandia")

    #crear la tabla de usuario del contenedor derecho
    tabla_inventario = ttk.Treeview(contenido, columns=("descripcion_producto", "cantidad_total", "fecha_vencimiento", "id_proveedor", "costo_mayor"), show="headings", padding=5)

    tabla_inventario.heading("descripcion_producto", text="producto") 
    tabla_inventario.heading("cantidad_total", text="cantidad de productos")
    tabla_inventario.heading("fecha_vencimiento", text="fecha de vencimiento")
    tabla_inventario.heading("id_proveedor", text="proveedores")
    tabla_inventario.heading("costo_mayor", text="precio de compra")

    #ajustar tamaño de columnas
    tabla_inventario.column("descripcion_producto", width=150)
    tabla_inventario.column("cantidad_total", width=100)
    tabla_inventario.column("fecha_vencimiento",width=100)
    tabla_inventario.column("id_proveedor", width=50)
    tabla_inventario.column("costo_mayor", width=50)

    #contenido de la tabla
    datos_tabla_inventario(tabla_inventario)

    #mostrar la tabla en el contenedor derecho
    tabla_inventario.pack(fill="both",expand=True)
    
#metodo del boton3
def boton3():
    print("fino3")


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
        ventana_dashboard.configure(bg="white")

        # Establecer el tamaño y posición de la ventana
        ventana_dashboard.geometry(f"{ancho_pantalla}x{alto_pantalla}+0+0")

        # Panel vertical izquierdo (Menú)
        panel_izquierdo = tk.Frame(ventana_dashboard, bg="light gray")
        panel_izquierdo.pack(side="left", fill="y")

        # Elementos del menú
        etiqueta_menu = tk.Label(panel_izquierdo, text="Menú", bg="light gray", font=("Arial", 16, "bold"))
        etiqueta_menu.pack(pady=10)

        # Opción 1
        opcion1 = tk.Button(panel_izquierdo, text="Usuarios", bg="white", padx=10, command=usuarios, pady=5)
        opcion1.pack(pady=5)
        

        # Opción 2
        opcion2 = tk.Button(panel_izquierdo, text="Inventario", bg="white", padx=10, command=Inventario, pady=5)
        opcion2.pack(pady=5)

        # Opción 3
        opcion3 = tk.Button(panel_izquierdo, text="Opción 3", bg="white", padx=10, command=boton3, pady=5)
        opcion3.pack(pady=5)

        # Contenedor a la derecha
        contenedor_derecho = tk.Frame(ventana_dashboard, bg="white")
        contenedor_derecho.pack(side="right", fill="both", expand=True)

        #elementos del contenedor derecho
        global etiqueta_titulo, contenido

        # Agregar elementos al contenedor derecho
        etiqueta_titulo = tk.Label(contenedor_derecho, text="Contenido", bg="white", font=("Arial", 16, "bold"))
        etiqueta_titulo.pack(pady=10)

        contenido = tk.Label(contenedor_derecho, text="Aquí va el contenido del menú seleccionado", bg="white")
        contenido.pack(pady=5)

        #configuramos el cierre de ventana
        ventana_dashboard.protocol("WM_DELETE_WINDOW", lambda:cerrar_sesion(ventana_dashboard))

        ventana_dashboard.mainloop()
        conexion.close()
        ventana_dashboard.destroy()
    else:
        messagebox.showerror("Inicio de sesión fallido", "Credenciales incorrectas")

# Ventana principal
ventana=tk.Tk()
ventana.title("sistema de inventario")
ventana.geometry("800x400")

# Agregar un marco que ocupe todo el espacio
marco = tk.Frame(ventana, bg="white")
marco.place(relwidth=1, relheight=1)

# Crear un marco para el formulario
formulario_frame = tk.Frame(marco, bg="pink", bd=5)
formulario_frame.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.3, anchor="center")

# Etiqueta de usuario
usuario_label = tk.Label(formulario_frame, text="Usuario:", bg="black", fg="white")
usuario_label.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.2)

# Cuadro de entrada de usuario
usuario_entry = tk.Entry(formulario_frame, bg="white")
usuario_entry.place(relx=0.4, rely=0.2, relwidth=0.5, relheight=0.2)

# Etiqueta de contraseña
password_label = tk.Label(formulario_frame, text="Contraseña:", bg="black", fg="white")
password_label.place(relx=0.1, rely=0.5, relwidth=0.3, relheight=0.2)

# Cuadro de entrada de contraseña
password_entry = tk.Entry(formulario_frame, show="*", bg="white")
password_entry.place(relx=0.4, rely=0.5, relwidth=0.5, relheight=0.2)

# Botón de inicio de sesión
boton_iniciar_sesion = tk.Button(formulario_frame, text="Iniciar sesión", command=iniciar_sesion, activebackground="#F50743")
boton_iniciar_sesion.place(relx=0.4, rely=0.8, relwidth=0.5, relheight=0.2)



# Iniciar el bucle principal de la ventana
ventana.mainloop()

ventana.destroy()

