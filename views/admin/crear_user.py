import tkinter as tk
from app.admin.usuarios import guardar_usuario, obtener_roles, obtener_prefijo

def crear_usuario(tabla_usuarios):
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

    # Etiqueta para seleccionar el prefijo del documento
    prefijo_label = tk.Label(formulario_crear, text="Prefijo Documento:", bg="black", fg="white")
    prefijo_label.pack(pady=5)

    # Obtener los roles desde la base de datos
    prefijos = obtener_prefijo()   
    selected_prefijo = tk.StringVar()

    # Crear una lista de opciones para el menú desplegable
    opciones_prefijo = [prefijo[1] for prefijo in prefijos]

    # Menú desplegable de roles
    prefijo_option_menu = tk.OptionMenu(formulario_crear, selected_prefijo, *opciones_prefijo)
    prefijo_option_menu.pack(pady=5)

     # Etiqueta de usuario
    ci_label = tk.Label(formulario_crear, text="Cédula:", bg="black", fg="white")
    ci_label.pack(pady=5)

   # Cuadro de entrada de usuario
    ci = tk.Entry(formulario_crear, bg="white")
    ci.pack(pady=5) 
    
    # Etiqueta para seleccionar rol del usuario
    rol_label = tk.Label(formulario_crear, text="Rol del Usuario:", bg="black", fg="white")
    rol_label.pack(pady=5)

    # Obtener los roles desde la base de datos
    roles = obtener_roles()

    # Variable para almacenar el rol seleccionado (se guardará el id_cargo)
    selected_role = tk.StringVar()

    # Crear una lista de opciones para el menú desplegable
    opciones_roles = [rol[1] for rol in roles]

    # Menú desplegable de roles
    rol_option_menu = tk.OptionMenu(formulario_crear, selected_role, *opciones_roles)
    rol_option_menu.pack(pady=5)
    # Botón de guardar usuario
    boton_guardar_usuario = tk.Button(formulario_crear, text="Crear Usuario", command=lambda: guardar_usuario(usuario_crear, password_entry, password_crear_confirmar, ci, selected_role, ventana_crear_usuario, tabla_usuarios, selected_prefijo), activebackground="#F50743", font=("helvetica", 12))
    boton_guardar_usuario.pack(pady=10, ipadx=10)