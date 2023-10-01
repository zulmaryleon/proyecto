import tkinter as tk
from customtkinter  import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkCheckBox
from app.utils import c_negro, c_verde, c_morado, c_rojo, c_azul, c_blanco, c_gris, c_azul_e, cambiar_imagen, avanzar_carrusel, redimensionar_imagen, cerrar_sesion, obtener_datos_session
from views.admin.inicio import inicio
from views.admin.usuarios import usuarios
from views.admin.inventario import inventario
from views.admin.proveedor import proveedor
from views.admin.movimientos import movimientos

from views.empleado.inventario import inventario_user
from views.empleado.movimientos import movimientos_user
from views.empleado.inicio import inicio_user

def crear_vista_dashboard(id_usuario):
    ventana_dashboard = CTk() 
    ventana_dashboard.geometry("900x600+350+20")
    ventana_dashboard.minsize(480, 500)
    ventana_dashboard.config(bg = c_negro)
    ventana_dashboard.title("CINELANDIA")

    # Panel vertical izquierdo (Menú)
    panel_izquierdo = tk.Frame(ventana_dashboard, bg=c_negro,  width=300)
    panel_izquierdo.pack(side="left", fill="y")

    # Elementos del menú
    etiqueta_menu = tk.Label(panel_izquierdo, text="Menú", bg=c_verde, fg="white", font=("Arial", 20, "bold"))
    etiqueta_menu.pack(pady=10)

    # Contenedor a la derecha
    contenedor_derecho = tk.Frame(ventana_dashboard, bg=c_azul_e)
    contenedor_derecho.pack(side="right", fill="both", expand=True)

    # Cargar las imágenes
    imagen1 = tk.PhotoImage(file="imagenes/img.png")
    imagen2 = tk.PhotoImage(file="imagenes/img2.png")
    imagen3 = tk.PhotoImage(file="imagenes/img.png")

    ancho_deseado = 200  # Especifica el ancho deseado para las imágenes
    alto_deseado = 250   # Especifica el alto deseado para las imágenes

    # Lista de imágenes para el carrusel
    imagenes = [
        redimensionar_imagen(imagen1, ancho_deseado, alto_deseado),
        redimensionar_imagen(imagen2, ancho_deseado, alto_deseado),
        redimensionar_imagen(imagen3, ancho_deseado, alto_deseado)
    ]

    # Variable para rastrear la imagen actual en el carrusel
    imagen_actual = 0

    # Agregar elementos al contenedor resaltado
    etiqueta_titulo = tk.Label(contenedor_derecho, text="Inicio Inventario cinelandia \n bienvenido al panel de adminsitrador tu rol es rol \n Selecciona una opcion del menu izquierdo.", bg="white", font=("Arial", 16, "bold"))
    etiqueta_titulo.pack(pady=10)

    # Etiqueta para el carrusel
    #imagen_carrusel = tk.Label(contenedor_derecho, image=imagenes[0], bg="#1b2838")
    #imagen_carrusel.pack(pady=5)

    # Indicadores de imágenes (puntos)
    #indicadores = []
    #for i in range(len(imagenes)):
    #    indicador = tk.Label(contenedor_derecho, text="●", font=("Helvetica", 14), bg="#1b2838", fg="white", activebackground="#F50743")
    #    indicador.bind("<Button-1>", lambda event, index=i: cambiar_imagen(index))
    #    indicadores.append(indicador)
    #    indicador.place(relx=0.43 + i * 0.05, rely=0.80)

    # Inicia el carrusel automático
    #avanzar_carrusel(imagen_carrusel, imagenes, imagen_actual, ventana_dashboard)        

    datos = obtener_datos_session(id_usuario)
    id_rol = datos[0]
    username = datos[1]

    if(id_rol == 1):
        # Opción 0
        opcion0 = CTkButton(panel_izquierdo, border_color=c_verde, fg_color = c_negro,
        hover_color=c_rojo,corner_radius=12,border_width=2,
        text='Inicio', command=lambda: inicio(contenedor_derecho)) #inicio(ventana_dashboard)
        opcion0.pack(pady=5)

        # Opción 1
        opcion1 = CTkButton(panel_izquierdo, border_color=c_verde, fg_color = c_negro,
        hover_color=c_rojo,corner_radius=12,border_width=2,
        text='Usuarios', command=lambda: usuarios(contenedor_derecho))
        opcion1.pack(pady=5)

        # Opción 2
        opcion2 = CTkButton(panel_izquierdo, border_color=c_verde, fg_color = c_negro,
        hover_color=c_rojo,corner_radius=12,border_width=2,
        text='Inventario', command=lambda: inventario(contenedor_derecho))
        opcion2.pack(pady=5)

        # Opción 3
        opcion3 = CTkButton(panel_izquierdo, border_color=c_verde, fg_color = c_negro,
        hover_color=c_rojo,corner_radius=12,border_width=2,
        text='Proveedores', command=lambda: proveedor(contenedor_derecho))
        opcion3.pack(pady=5)

        # Opción 4
        opcion4 = CTkButton(panel_izquierdo, border_color=c_verde, fg_color = c_negro,
        hover_color=c_rojo,corner_radius=12,border_width=2,
        text='Movimientos', command=lambda: movimientos(contenedor_derecho))
        opcion4.pack(pady=5)
    else:
        # Opción 0
        opcion1 = CTkButton(panel_izquierdo, border_color=c_verde, fg_color = c_negro,
        hover_color=c_rojo,corner_radius=12,border_width=2,
        text='Inicio', command=lambda:inicio_user(contenedor_derecho)) #, command=lambda: inicio_user(contenedor_derecho)
        opcion1.pack(pady=5)  

        # Opción 2
        opcion2 = CTkButton(panel_izquierdo, border_color=c_verde, fg_color = c_negro,
        hover_color=c_rojo,corner_radius=12,border_width=2,
        text='Inventario', command=lambda:inventario_user(contenedor_derecho)) #, command=lambda: inventario_user(contenedor_derecho)
        opcion2.pack(pady=5)     

        # Opción 4
        opcion3 = CTkButton(panel_izquierdo, border_color=c_verde, fg_color = c_negro,
        hover_color=c_rojo,corner_radius=12,border_width=2,
        text='Movimientos', command=lambda:movimientos_user(contenedor_derecho, id_usuario)) #, command=lambda: movimientos(contenedor_derecho) 
        opcion3.pack(pady=5) 
    # Agregar recuadro inferior
    recuadro_inferior = tk.Frame(panel_izquierdo, bg=c_verde, relief="solid")
    recuadro_inferior.pack(side="bottom", fill="x")

    # Puedes reemplazar 'ruta_imagen.png' con la ruta de tu imagen
    #imagen = tk.PhotoImage(file="imagenes/user.png")
    #imagen = redimensionar_imagen(imagen, 50, 50),
    #imagen_label = tk.Label(recuadro_inferior, image=imagen, bg="#3300FF")
    #imagen_label.image = imagen
    #imagen_label.pack(side="top", padx=10)

    # Agregar icono de configuración
    #icono_configuracion = tk.PhotoImage(file='imagenes/settings.png')
    #icono_configuracion = redimensionar_imagen(icono_configuracion, 25, 25)
    #icono_label = tk.Label(recuadro_inferior, image=icono_configuracion, bg="#3300FF")
    #icono_label.image = icono_configuracion
    #icono_label.pack(side="right", padx=10)

    # Agregar rol
    rol_label = tk.Label(recuadro_inferior, text=f"Username: {str(username)}", bg=c_verde, fg="white", font=("Arial", 14))
    rol_label.pack(padx=10)

    username = tk.Label(recuadro_inferior, text=f"Rol: {str(id_rol)}", bg=c_verde, fg="white", font=("Arial", 14))
    username.pack(padx=10)

    #configuramos el cierre de ventana
    ventana_dashboard.protocol("WM_DELETE_WINDOW", lambda:cerrar_sesion(ventana_dashboard))

    ventana_dashboard.mainloop()

    ventana_dashboard.destroy()
