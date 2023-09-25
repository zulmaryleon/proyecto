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