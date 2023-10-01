from tkinter import messagebox
from app.database import get_database_connection

# Función para consultar un usuario en MySQL
conexion = get_database_connection()

def datos_tabla_proveedor(tabla):
    global conexion
    #eliminamos todos lo elementos antes de actualizar
    tabla.delete(*tabla.get_children())
    if not conexion.is_connected():
            conexion = get_database_connection()  # Vuelve a crear la conexión si es necesario

    cursor = conexion.cursor()
    cursor.execute("select id_proveedor, nombre, codigo, id_prefijo_documento from proveedor")
    resultado= cursor.fetchall()
    for id_proveedor, nombre, codigo, id_prefijo_documento in resultado:

        #insercion de datos
        tabla.insert("", "end", values=(id_proveedor, nombre, codigo, id_prefijo_documento))


def obtener_id_de_descripcion(descripcion):
    global conexion  # Asegúrate de que la variable 'conexion' esté configurada correctamente

    try:
        if not conexion.is_connected():
            conexion = get_database_connection()  # Vuelve a crear la conexión si es necesario

        # Abrir cursor
        cursor = conexion.cursor()

        # Consulta SQL para obtener el ID de un cargo basado en la descripción
        consulta = "SELECT id_prefijo_cedula FROM prefijo_documento WHERE descripcion_prefijo_cedula = %s"
        cursor.execute(consulta, (descripcion,))

        # Obtener el resultado
        resultado = cursor.fetchone()

        if resultado:
            id_prefijo = resultado[0]
            return id_prefijo
        else:
            return None  # Devolver None si no se encuentra la descripción

    except Exception as e:
        print(f"Error al obtener ID de descripción: {str(e)}")
        return None
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()  

def guardar_proveedor(proveedor_crear, codigo_entry, selected_prefijo, ventana_crear_proveedor, tabla_proveedor):
    global conexion #definimos la variable conexion como global
    nombre = proveedor_crear.get()
    codigo= codigo_entry.get()
    prefijo_documento=obtener_id_de_descripcion(selected_prefijo.get())
    #creamos una sentencia para guardar los datos en la base de datos
    try:
        if not conexion.is_connected():
            conexion = get_database_connection()  # Vuelve a crear la conexión si es necesario

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
        


def editar_datos_proveedor(id_proveedor, proveedor_editar,codigo_editar, prefijo_documento_entry, tabla_proveedor, ventana_editar_proveedor):
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

# Función para eliminar el usuario
def confirmar_eliminar(id_proveedor, ventana_confirmacion, tabla_proveedor, nombre_proveedor):
    #creamos una sentencia para guardar los datos en la base de datos
    global conexion  # Asegúrate de que la variable 'conexion' esté configurada correctamente

    try:
        if not conexion.is_connected():
            conexion = get_database_connection()  # Vuelve a crear la conexión si es necesario
        
        cursor = conexion.cursor()

        # Consulta para eliminar al usuario
        consulta_eliminar = f"DELETE FROM proveedor WHERE id_proveedor = {id_proveedor}"
        cursor.execute(consulta_eliminar)

        conexion.commit()
        
        #actualizar tabla
        datos_tabla_proveedor(tabla_proveedor)

        cursor.close()
    except Exception as e:
        conexion.rollback()
        messagebox.showerror("Error", f"No se ha podido editar el usuario: {str(e)}")
    
    messagebox.showinfo("Información", f"Proveedor '{nombre_proveedor}' (ID: {id_proveedor}) ha sido eliminado.")
    ventana_confirmacion.destroy()

# Función para cancelar la eliminación
def cancelar_eliminar(ventana_confirmacion):
    messagebox.showinfo("Información", "Operación de eliminación cancelada.")
    ventana_confirmacion.destroy()

def obtener_prefijo():
    prefijo = []
    try:
        # Crea un cursor
        cursor = conexion.cursor()

        # Ejecuta una consulta SQL para obtener los roles
        cursor.execute("SELECT  id_prefijo_cedula, descripcion_prefijo_cedula    FROM prefijo_documento")

        # Obtiene todos los resultados de la consulta
        prefijo = cursor.fetchall()
    except Exception as e:
        print(f"Error al obtener los roles desde la base de datos: {str(e)}")

    return prefijo    

