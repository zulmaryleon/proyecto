from tkinter import messagebox
from app.database import get_database_connection

# Función para consultar un usuario en MySQL
conexion = get_database_connection()

def datos_tabla_proveedor(tabla):
    #eliminamos todos lo elementos antes de actualizar
    tabla.delete(*tabla.get_children())

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

    finally:
        # Cierra el cursor y la conexión
        if cursor:
            cursor.close()
        if conexion.is_connected():
            conexion.close()

    return prefijo    

