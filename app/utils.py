#Colores
c_negro = '#010101'
c_verde = '#2cb67d'
c_morado = '#7f5af0'
c_rojo = '#F50743'
c_azul = '#3300FF'
c_blanco = '#fff'
c_gris = 'gray90'
c_azul_e  = '#1b2838'

# Función para cambiar la imagen en el carrusel
def cambiar_imagen(imagen_carrusel, imagenes, imagen_actual):
    siguiente_indice = (imagen_actual + 1) % len(imagenes)
    imagen = imagenes[siguiente_indice]
    imagen_carrusel.configure(image=imagen)
    imagen_carrusel.image = imagen
    imagen_actual = siguiente_indice

# Función para avanzar automáticamente el carrusel
def avanzar_carrusel(imagen_carrusel, imagenes, imagen_actual, ventana):
    siguiente_indice = (imagen_actual + 1) % len(imagenes)
    cambiar_imagen(imagen_carrusel, imagenes, imagen_actual)
    ventana.after(3000, lambda: avanzar_carrusel(imagen_carrusel, imagenes, imagen_actual, ventana))

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