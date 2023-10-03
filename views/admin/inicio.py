import tkinter as tk
from tkinter import PhotoImage
from app.admin.inicio import obtener_ventas, obtener_compras
from app.utils import c_negro, c_verde, c_morado, c_rojo, c_azul, c_blanco, c_gris, redimensionar_imagen
global imagen_actual

def inicio(contenedor_derecho):
    # Limpia el contenido anterior
    for widget in contenedor_derecho.winfo_children():
        widget.destroy()

    # Cargar las imágenes
    imagen1 = tk.PhotoImage(file="imagenes/img.png")
    imagen2 = tk.PhotoImage(file="imagenes/img2.png")
    imagen3 = tk.PhotoImage(file="imagenes/img.png")

    ancho_deseado = 250  # Especifica el ancho deseado para las imágenes
    alto_deseado = 250   # Especifica el alto deseado para las imágenes

    # Lista de imágenes para el carrusel
    imagenes = [
        redimensionar_imagen(imagen1, ancho_deseado, alto_deseado),
        redimensionar_imagen(imagen2, ancho_deseado, alto_deseado),
        redimensionar_imagen(imagen3, ancho_deseado, alto_deseado)
    ]
    
    etiqueta_titulo = tk.Label(contenedor_derecho, text="Inicio", fg=c_blanco, bg=c_negro, font=("Arial", 16, "bold"))
    etiqueta_titulo.pack(pady=10)

   # Variable para rastrear la imagen actual en el carrusel
    imagen_actual = 0

    # Etiqueta para el carrusel
    imagen_carrusel = tk.Label(contenedor_derecho, image=imagenes[0], bg=c_negro)
    imagen_carrusel.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    # Indicadores de imágenes (puntos)
    indicadores = []
    for i in range(len(imagenes)):
        indicador = tk.Label(contenedor_derecho, text="●", font=("Helvetica", 14), bg="#1b2838", fg="white", activebackground="#F50743")
        indicador.bind("<Button-1>", lambda event, index=i: cambiar_imagen(index))
        indicadores.append(indicador)
        indicador.place(relx=0.43 + i * 0.05, rely=0.80)
    # Función para cambiar la imagen en el carrusel
    def cambiar_imagen(index):
        imagen_actual = index
        imagen = imagenes[0]
        imagen_carrusel.configure(image=imagen)
        imagen_carrusel.image = imagen

    # Función para avanzar automáticamente el carrusel
    def avanzar_carrusel():
        # Calcula el índice de la siguiente imagen
        siguiente_indice = (0 + 1) % len(imagenes)
        cambiar_imagen(siguiente_indice)
        contenedor_derecho.after(3000, avanzar_carrusel)  # Cambia la imagen cada 3000 milisegundos (3 segundos)

   # Inicia el carrusel automático
    avanzar_carrusel()

    # Etiqueta y entrada para agregar producto
    # Contenedor de gráficos (a la derecha de los recuadros)
    #contenedor_graficos = tk.Frame(contenedor_derecho, bg=c_blanco, borderwidth=2, relief="solid")
    #contenedor_graficos.pack(side="right", fill="both", expand=True)

    # Crear un recuadro grande para la gráfica
    #recuadro_grafica = tk.Frame(contenedor_graficos, width=300, height=300, bg="white", borderwidth=2, relief="solid")
    #recuadro_grafica.pack(padx=10, pady=10)    
