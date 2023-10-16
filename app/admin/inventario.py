from tkinter import messagebox
from app.database import get_database_connection
import datetime
# Función para consultar un producto en MySQL
conexion = get_database_connection()

def obtener_id_de_descripcion_categoria(descripcion):
    global conexion  # Asegúrate de que la variable 'conexion' esté configurada correctamente

    try:
        if not conexion.is_connected():
            conexion = get_database_connection()  # Vuelve a crear la conexión si es necesario

        # Abrir cursor
        cursor = conexion.cursor()

        # Consulta SQL para obtener el ID de un cargo basado en la descripción
        consulta = "SELECT id_categoria FROM categoria WHERE descripcion_categoria = %s"
        cursor.execute(consulta, (descripcion,))

        # Obtener el resultado
        resultado = cursor.fetchone()

        if resultado:
            id_categoria = resultado[0]
            return id_categoria
        else:
            return None  # Devolver None si no se encuentra la descripción

    except Exception as e:
        print(f"Error al obtener ID de descripción: {str(e)}")
        return None
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close() 

def obtener_id_de_descripcion_proveedores(descripcion):
    global conexion  # Asegúrate de que la variable 'conexion' esté configurada correctamente

    try:
        if not conexion.is_connected():
            conexion = get_database_connection()  # Vuelve a crear la conexión si es necesario

        # Abrir cursor
        cursor = conexion.cursor()

        # Consulta SQL para obtener el ID de un cargo basado en la descripción
        consulta = "SELECT id_proveedor FROM proveedor WHERE nombre = %s"
        cursor.execute(consulta, (descripcion,))

        # Obtener el resultado
        resultado = cursor.fetchone()

        if resultado:
            id_proveedor = resultado[0]
            return id_proveedor
        else:
            return None  # Devolver None si no se encuentra la descripción

    except Exception as e:
        print(f"Error al obtener ID de descripción: {str(e)}")
        return None
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()             

def datos_tabla_inventario(tabla):
    #eliminamos todos lo elementos antes de actualizar
    tabla.delete(*tabla.get_children())

    cursor = conexion.cursor()
    cursor.execute("select i.id_producto, i.descripcion_producto, i.cantidad_total, i.fecha_vencimiento, p.nombre, i.costo_mayor, i.precio_unitario  from productos i INNER JOIN proveedor p ON i.id_proveedor = p.id_proveedor")
    resultado= cursor.fetchall()
    for id_producto, descripcion_producto, cantidad_total, fecha_vencimiento, id_proveedor, costo_mayor, precio_unitario in resultado:
        precio_unitario_con_signo = str(precio_unitario) + "$"
        costo_mayor = str(costo_mayor) + "$"

        #insercion de datos
        tabla.insert("", "end", values=(id_producto, descripcion_producto, cantidad_total, fecha_vencimiento, id_proveedor, costo_mayor, precio_unitario_con_signo)) 

         # Asignar etiquetas (tags) según las reglas definidas
        if cantidad_total < 1:  # Si hay menos de 1 productos, etiquetar como "rojo"
            tabla.item(tabla.get_children()[-1], tags=("rojo",))
        elif cantidad_total >= 1 and cantidad_total <= 10:  # Por ejemplo, si quedan 10 o menos productos, etiquetar como "amarillo"
            
            tabla.item(tabla.get_children()[-1], tags=("amarillo",))
        else:   # Si quedan entre 6 y 10 productos, etiquetar como "verde"
            tabla.item(tabla.get_children()[-1], tags=("verde",))

# Función para consultar un producto en MySQL
def consultar_producto(id_producto):
    cursor = conexion.cursor(dictionary=True)  # Utiliza dictionary=True para obtener un diccionario
    # Consultar el inventario por ID
    try:
        consulta = "SELECT descripcion_producto, id_categoria, cantidad_total, costo_mayor, precio_unitario, fecha_vencimiento, id_proveedor FROM productos WHERE id_producto = %s"
        cursor.execute(consulta, (id_producto,))
        producto = cursor.fetchone()

        cursor.close()

        return producto

    except Exception as e:
        conexion.rollback()
        messagebox.showerror("Error", f"No se ha podido consultar el producto: {str(e)}")


def confirmar_eliminar(id_producto, ventana_confirmacion, tabla, descripcion_producto):
    #creamos una sentencia para guardar los datos en la base de datos
    global conexion  # Asegúrate de que la variable 'conexion' esté configurada correctamente

    try:
        if not conexion.is_connected():
            conexion = get_database_connection()  # Vuelve a crear la conexión si es necesario
        
        cursor = conexion.cursor()

        # Consulta para eliminar al producto
        consulta_eliminar = f"DELETE FROM productos WHERE id_producto = {id_producto}"
        cursor.execute(consulta_eliminar)

        conexion.commit()

        #actualizar tabla
        datos_tabla_inventario(tabla)

        cursor.close()
    except Exception as e:
        conexion.rollback()
        messagebox.showerror("Error", f"No se ha podido editar el producto: {str(e)}")

    messagebox.showinfo("Información", f"producto '{descripcion_producto}' (ID: {id_producto}) ha sido eliminado.")
    ventana_confirmacion.destroy()

def cancelar_eliminar(ventana_confirmacion):
    messagebox.showinfo("Información", "Operación de eliminación cancelada.")
    ventana_confirmacion.destroy()
    
def guardar_producto(producto_crear, categoria, precio_crear, cantidad_crear, precio_unitario_crear, fecha_vencimiento_crear, tabla_inventario, ventana_crear_producto, selected_proveedor):
    global conexion #definimos la variable conexion como global
    
    producto = producto_crear.get()
    categoria = obtener_id_de_descripcion_categoria(categoria.get())
    cantidad = cantidad_crear.get()
    precio_mayor=precio_crear.get()
    precio_unitario = precio_unitario_crear.get()
    fecha_vencimiento= fecha_vencimiento_crear.get()
    proveedor = obtener_id_de_descripcion_proveedores(selected_proveedor.get())
    fecha_actual = datetime.date.today()

    print(f"Id proveedor: {str(proveedor)}")
    print(f"Id categoria: {str(categoria)}")
    print(f"cantidad: {str(cantidad)}")
    print(f"precio_mayor: {str(precio_mayor)}")
    print(f"precio_unitario: {str(precio_unitario)}")
    #creamos una sentencia para guardar los datos en la base de datos
    try:
        if not conexion.is_connected():
            conexion = get_database_connection()  # Vuelve a crear la conexión si es necesario
        #abrir cursor

        cursor=conexion.cursor()

        consulta="INSERT INTO productos (descripcion_producto, id_categoria, cantidad_total, costo_mayor, precio_unitario, fecha_vencimiento, id_proveedor) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(consulta, (producto, categoria, cantidad, precio_mayor, precio_unitario, fecha_vencimiento, proveedor))

        conexion.commit()
        #actualizar tabla
        datos_tabla_inventario(tabla_inventario)

        cursor.close()

        ventana_crear_producto.destroy()
        
        messagebox.showinfo("Producto creado", 'Se ha registrado el producto correctamente')
    except Exception as e:
        conexion.rollback()
        messagebox.showerror("Error", f"No se ha podido registrar el producto: {str(e)}")


def editar_datos_producto(id_producto, producto_editar,cantidad_editar, fecha_vencimiento, selected_proveedor, precio_compra_editar, precio_venta_editar, ventana_editar_producto, tabla_producto):
    nombre_producto = producto_editar.get()
    cantidad = cantidad_editar.get()
    vencimiento = fecha_vencimiento.get()
    proveedor = obtener_id_de_descripcion_proveedores(selected_proveedor.get())
    precio_compra  = precio_compra_editar.get()
    precio_venta = precio_venta_editar.get()
    id_producto = id_producto
    categoria = '2'

    #creamos una sentencia para guardar los datos en la base de datos
    global conexion  # Asegúrate de que la variable 'conexion' esté configurada correctamente

    try:
        if not conexion.is_connected():
            conexion = get_database_connection()  # Vuelve a crear la conexión si es necesario

        # Crear la sentencia SQL para actualizar el producto en la base de datos
        sentencia = "UPDATE productos SET descripcion_producto = %s, cantidad_total = %s, fecha_vencimiento	= %s, id_proveedor = %s, id_categoria = %s, precio_unitario = %s, costo_mayor = %s WHERE id_producto = %s"
        datos = (nombre_producto, cantidad, vencimiento, proveedor, categoria, precio_venta, precio_compra, id_producto)

        cursor = conexion.cursor()
        cursor.execute(sentencia, datos)
        conexion.commit()

        #actualizar tabla
        datos_tabla_inventario(tabla_producto)

        cursor.close()
        ventana_editar_producto.destroy()

        messagebox.showinfo("Producto editar", 'Se ha editado el producto correctamente')
    except Exception as e:
        conexion.rollback()
        messagebox.showerror("Error", f"No se ha podido editar el producto: {str(e)}")  


def obtener_categorias():
    categoria = []
    try:
        # Crea un cursor
        cursor = conexion.cursor()

        # Ejecuta una consulta SQL para obtener los roles
        cursor.execute("SELECT  id_categoria, descripcion_categoria FROM categoria")

        # Obtiene todos los resultados de la consulta
        categoria = cursor.fetchall()
    except Exception as e:
        print(f"Error al obtener las categorias desde la base de datos: {str(e)}")

    return categoria              

def obtener_proveedores():
    proveedores = []
    try:
        # Crea un cursor
        cursor = conexion.cursor()

        # Ejecuta una consulta SQL para obtener los roles
        cursor.execute("SELECT id_proveedor, nombre FROM proveedor")

        # Obtiene todos los resultados de la consulta
        proveedores = cursor.fetchall()
    except Exception as e:
        print(f"Error al obtener los proveedores desde la base de datos: {str(e)}")

    return proveedores 