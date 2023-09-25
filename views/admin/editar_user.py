from app.boton_usuarios import consultar_usuario
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

    editar_usuario_consulta()


    # Botón de guardar usuario
    boton_editar_usuario = tk.Button(formulario_editar, text="Editar Usuario", command=editar_usuario_consulta()
, activebackground="#F50743", font=("helvetica", 12))
    boton_editar_usuario.pack(pady=10, ipadx=10)