# app/database.py
import mysql.connector

# Configuración de la conexión a la base de datos
def get_database_connection():
    try:
        # Configura los parámetros de conexión a tu base de datos MySQL
        config = {
            'user': 'root',
            'password': '',
            'host': 'localhost',
            'database': 'cinelandia',
            'raise_on_warnings': True,
        }

        # Crea una conexión a la base de datos
        conexion = mysql.connector.connect(**config)

        return conexion

    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None

# Ejemplo de consulta a la base de datos
def ejecutar_consulta(sql_query):
    conexion = get_database_connection()
    
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute(sql_query)
            resultados = cursor.fetchall()
            cursor.close()
            conexion.close()
            return resultados
        except mysql.connector.Error as err:
            print(f"Error en la consulta: {err}")
            return []
    else:
        return []

# Ejemplo de inserción en la base de datos
def ejecutar_insercion(sql_query, data):
    conexion = get_database_connection()
    
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute(sql_query, data)
            conexion.commit()
            cursor.close()
            conexion.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error al insertar en la base de datos: {err}")
            return False
    else:
        return False