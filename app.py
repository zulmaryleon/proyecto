import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

#Funcion de la data de usuario
def datos_tabla_usuarios(tabla):
    #insercion de datos
    tabla.insert("", "end", values=("usuario1", "administrador", "horario"))
    tabla.insert("", "end", values=("usuario2", "empleado","horario"))
    tabla.insert("", "end", values=("usuario3", "empleada", "horario"))

#metodo del boton1
def usuarios():
    etiqueta_titulo.config(text="Usuarios del sistema")

    #aplicar tema x
    estilo= ttk.Style()
    estilo.theme_use("clam")

    #crear la tabla de usuario del contenedor derecho
    tabla_usuarios = ttk.Treeview(contenido, columns=("Usuario", "Rol", "horario"), show="headings")

    tabla_usuarios.heading("Usuario", text="Usuario del Sistema") 
    tabla_usuarios.heading("Rol", text="Rol del Usuario")
    tabla_usuarios.heading("horario", text="Horario de entrada")

    #ajustar tamaño de columnas
    tabla_usuarios.column("Usuario", width=100)
    tabla_usuarios.column("Rol", width=100)
    tabla_usuarios.column("horario",width=100)

    #contenido de la tabla
    datos_tabla_usuarios(tabla_usuarios)

    #mostrar la tabla en el contenedor derecho
    tabla_usuarios.pack(fill="both",expand=True)

#metodo del boton2
def Inventario():
    etiqueta_titulo.config(text="Inventario General")
    #contenido 
    contenido.config(text="Inventario de los Productos de Cinelandia")
    
#metodo del boton3
def boton3():
    print("fino3")


# Metodo de inicio de session
def iniciar_sesion():
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
    conexion.close()

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



        ventana_dashboard.mainloop()

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

