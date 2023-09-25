from tkinter import messagebox
from app.database import get_database_connection

# Función para consultar un usuario en MySQL
conexion = get_database_connection()

def consultar_usuario(id_usuario):
    global conexion #definimos la variable conexion como global
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