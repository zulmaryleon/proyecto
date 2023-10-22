from tkinter import messagebox
from app.database import get_database_connection
from app.utils import campo_existe
import datetime, time

# Función para consultar un usuario en MySQL
conexion = get_database_connection()

#Funcion de la data de usuario
def datos_tabla_usuarios(tabla):
    #conexion global

    #eliminamos todos lo elementos antes de actualizar
    tabla.delete(*tabla.get_children())

    cursor = conexion.cursor()
    cursor.execute("SELECT u.id_usuario, u.usuario, u.fecha_ingreso, c.descripcion_cargo FROM usuario u INNER JOIN cargo c ON u.id_cargo = c.id_cargo")
    resultado= cursor.fetchall()
    for id_usuario, usuario, fecha_ingreso, id_cargo in resultado:

        #insercion de datos
        tabla.insert("", "end", values=(id_usuario, usuario, id_cargo, fecha_ingreso))   

def consultar_usuario(id_usuario):
    cursor = conexion.cursor(dictionary=True)  # Utiliza dictionary=True para obtener un diccionario
    # Consultar el usuario por ID
    try:
        consulta = "SELECT ci_usuario, usuario, fecha_ingreso FROM usuario WHERE id_usuario = %s"
        cursor.execute(consulta, (id_usuario,))
        usuario = cursor.fetchone()

        cursor.close()

        return usuario

    except Exception as e:
        conexion.rollback()
        messagebox.showerror("Error", f"No se ha podido consultar el usuario: {str(e)}")


def editar_usuario_consulta(id_usuario, ventana_editar_usuario, usuario_editar, ci_editar, rol_entry, tabla_usuarios):
    usuario = usuario_editar.get()
    rol= rol_entry.get()
    ci= ci_editar.get()
    #creamos una sentencia para guardar los datos en la base de datos
    global conexion  # Asegúrate de que la variable 'conexion' esté configurada correctamente

    try:
        if not conexion.is_connected():
            conexion = get_database_connection()  # Vuelve a crear la conexión si es necesario

        # Crear la sentencia SQL para actualizar el usuario en la base de datos
        sentencia = "UPDATE usuario SET usuario = %s, id_cargo = %s, ci_usuario = %s WHERE id_usuario = %s"
        datos = (usuario, rol, ci, id_usuario)

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


# Función para eliminar el usuario
def confirmar_eliminar(id_usuario, tabla_usuarios, ventana_confirmacion, nombre_usuario):
    #creamos una sentencia para guardar los datos en la base de datos
    global conexion  # Asegúrate de que la variable 'conexion' esté configurada correctamente

    try:
        if not conexion.is_connected():
            conexion = get_database_connection()  # Vuelve a crear la conexión si es necesario
        
        cursor = conexion.cursor()

        # Consulta para eliminar al usuario
        consulta_eliminar = f"DELETE FROM usuario WHERE id_usuario = {id_usuario}"
        cursor.execute(consulta_eliminar)

        conexion.commit()

        #actualizar tabla
        datos_tabla_usuarios(tabla_usuarios)

        cursor.close()
    except Exception as e:
        conexion.rollback()
        messagebox.showerror("Error", f"No se ha podido editar el usuario: {str(e)}")

    messagebox.showinfo("Información", f"Usuario '{nombre_usuario}' (ID: {id_usuario}) ha sido eliminado.")
    ventana_confirmacion.destroy()

# Función para cancelar la eliminación
def cancelar_eliminar(ventana_confirmacion):
    messagebox.showinfo("Información", "Operación de eliminación cancelada.")
    ventana_confirmacion.destroy()

            
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

    # Verificar si la cédula ya existe en la base de datos
    if campo_existe("usuario", "ci_usuario",  ci_valor):
        messagebox.showerror("Error al registrar", "La cédula ya existe en la base de datos")
        return

    # Verificar si el nombre de usuario ya existe en la base de datos
    if campo_existe("usuario", "usuario", f"'{usuario}'"):
        messagebox.showerror("Error al registrar", "El nombre de usuario ya existe en la base de datos")
        return

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

    return roles