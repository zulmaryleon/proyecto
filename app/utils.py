from app.database import get_database_connection
from tkinter import messagebox

#Colores
c_negro = '#010101'
c_verde = '#2cb67d'
c_morado = '#7f5af0'
c_rojo = '#F50743'
c_azul = '#3300FF'
c_blanco = '#fff'
c_gris = 'gray90'
c_azul_e  = '#1b2838'
c_gris_oscuro = '#333333'
blanco_gris = '#FFFFFF'
plata = '#D3D3D3'
azul_claro = '#6699FF'
rojo_claro = '#FF6666'
verde = '#00FF00'

logo_img = 'imagenes/logo.png'

conexion = get_database_connection()

def obtener_datos_session(id_usuario):
    global conexion  # Asegúrate de que la variable 'conexion' esté configurada correctamente

    try:
        if not conexion.is_connected():
            conexion = get_database_connection()  # Vuelve a crear la conexión si es necesario

        # Abrir cursor
        cursor = conexion.cursor()

        # Consulta SQL para obtener el ID de un cargo basado en la descripción
        consulta = "SELECT id_cargo, usuario, id_usuario FROM usuario WHERE id_usuario = %s"
        cursor.execute(consulta, (id_usuario,))

        # Obtener el resultado
        resultado = cursor.fetchone()

        if resultado:
            datos = resultado
            return datos
        else:
            return None  # Devolver None si no se encuentra la descripción

    except Exception as e:
        print(f"Error al obtener ID de descripción: {str(e)}")
        return None          

# Función para redimensionar una imagen
def redimensionar_imagen(imagen, ancho, alto):
    return imagen.subsample(int(imagen.width() / ancho), int(imagen.height() / alto))


#metodo de cerrar ventanas
def cerrar_sesion(ventana):
    ventana.destroy()

def buscar(tabla, entrada_busqueda):
    valor_busqueda = entrada_busqueda.get()
    # Itera sobre los elementos de la tabla y muestra solo los que coinciden con la búsqueda
    for row_id in tabla.get_children():
        values = tabla.item(row_id, 'values')
        if valor_busqueda.lower() in [str(value).lower() for value in values]:
            tabla.selection_set(row_id)
        else:
            tabla.selection_remove(row_id)
          
# Función para verificar si la cédula ya existe en la base de datos
def campo_existe(tabla, campo, valor):
    try:
        cursor = conexion.cursor()
        consulta = f"SELECT COUNT(*) FROM {str(tabla)} WHERE {str(campo)} = {str(valor)}"
        cursor.execute(consulta)
        resultado = cursor.fetchone()[0]
        cursor.close()
        return resultado > 0
    except Exception as e:
        print(f"Error al verificar cédula: {str(e)}")
        return False          