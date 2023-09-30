from tkinter import messagebox
from app.database import get_database_connection
import datetime, time

# Función para consultar un usuario en MySQL
conexion = get_database_connection()

#Funcion de la data de usuario
def datos_tabla_usuarios(tabla):
    #conexion global

    #eliminamos todos lo elementos antes de actualizar
    tabla.delete(*tabla.get_children())

    cursor = conexion.cursor()
    cursor.execute("select id_usuario, usuario, fecha_ingreso, id_cargo from usuario")
    resultado= cursor.fetchall()
    for id_usuario, usuario, fecha_ingreso, id_cargo in resultado:

        #insercion de datos
        tabla.insert("", "end", values=(id_usuario, usuario, id_cargo, fecha_ingreso))   

def consultar_usuario(id_usuario):
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

def obtener_id_de_descripcion(descripcion):
    global conexion  # Asegúrate de que la variable 'conexion' esté configurada correctamente

    try:
        if not conexion.is_connected():
            conexion = get_database_connection()  # Vuelve a crear la conexión si es necesario

        # Abrir cursor
        cursor = conexion.cursor()

        # Consulta SQL para obtener el ID de un cargo basado en la descripción
        consulta = "SELECT id_cargo FROM cargo WHERE descripcion_cargo = %s"
        cursor.execute(consulta, (descripcion,))

        # Obtener el resultado
        resultado = cursor.fetchone()

        if resultado:
            id_cargo = resultado[0]
            return id_cargo
        else:
            return None  # Devolver None si no se encuentra la descripción

    except Exception as e:
        print(f"Error al obtener ID de descripción: {str(e)}")
        return None
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def guardar_usuario(usuario_crear, password_entry, password_crear_confirmar, ci, selected_role, ventana_crear_usuario, tabla_usuarios):
    global conexion  # Indicar que estás utilizando la variable global

    ci_valor = ci.get()
    usuario = usuario_crear.get()
    contrasena = password_entry.get()
    confirmar_contrasena = password_crear_confirmar.get()
    rol = obtener_id_de_descripcion(selected_role.get())  # Función que obtiene la ID basada en la descripción
    fecha_actual = datetime.date.today()
    print(f"Eliminar usuario con ID cargo: {selected_role.get()}")
    print(f"Eliminar usuario con ID cargo: {rol}")

    if contrasena == confirmar_contrasena:
        try:
            if not conexion.is_connected():
                conexion = get_database_connection()  # Vuelve a crear la conexión si es necesario
           
            # Abrir cursor
            cursor = conexion.cursor()
            consulta = "INSERT INTO usuario (ci_usuario, usuario, contraseña, fecha_ingreso, id_cargo) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(consulta, (ci_valor, usuario, contrasena, fecha_actual, rol))

            conexion.commit()
            # Actualizar tabla
            datos_tabla_usuarios(tabla_usuarios)

            cursor.close()
            ventana_crear_usuario.destroy()
            messagebox.showinfo("Usuario creado", 'Se ha registrado el usuario correctamente')

        except Exception as e:
            conexion.rollback()
            messagebox.showerror("Error", f"No se ha podido registrar el usuario: {str(e)}")
    else:
        messagebox.showerror("Error al registrar", "Las contraseñas no coinciden, vuelva a intentarlo")

# Función para obtener los roles desde la base de datos (debes implementarla)
def obtener_roles():
    roles = []
    try:
        # Crea un cursor
        cursor = conexion.cursor()

        # Ejecuta una consulta SQL para obtener los roles
        cursor.execute("SELECT id_cargo, descripcion_cargo FROM cargo")

        # Obtiene todos los resultados de la consulta
        roles = cursor.fetchall()


    except Exception as e:
        print(f"Error al obtener los roles desde la base de datos: {str(e)}")

    finally:
        # Cierra el cursor y la conexión
        if cursor:
            cursor.close()
        if conexion.is_connected():
            conexion.close()

    return roles