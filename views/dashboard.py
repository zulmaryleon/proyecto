import tkinter as tk
from customtkinter  import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkCheckBox
from app.utils import c_negro, c_verde, c_morado, c_rojo, c_azul, c_blanco, c_gris, cambiar_imagen, avanzar_carrusel, redimensionar_imagen, cerrar_sesion
from views.admin.inicio import inicio
from views.admin.usuarios import usuarios
from views.admin.inventario import inventario
from views.admin.proveedor import proveedor
from views.admin.movimientos import movimientos

def crear_vista_dashboard(id_rol):
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
    contenedor_derecho = tk.Frame(ventana_dashboard, bg=c_negro)
    contenedor_derecho.pack(side="right", fill="both", expand=True)
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
        text='Inicio') #, command=lambda: inicio_user(contenedor_derecho)
        opcion1.pack(pady=5)  

        # Opción 2
        opcion2 = CTkButton(panel_izquierdo, border_color=c_verde, fg_color = c_negro,
        hover_color=c_rojo,corner_radius=12,border_width=2,
        text='Inventario') #, command=lambda: inventario_user(contenedor_derecho)
        opcion2.pack(pady=5)     

        # Opción 4
        opcion3 = CTkButton(panel_izquierdo, border_color=c_verde, fg_color = c_negro,
        hover_color=c_rojo,corner_radius=12,border_width=2,
        text='Movimientos') #, command=lambda: movimientos(contenedor_derecho)
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
    rol_label = tk.Label(recuadro_inferior, text="Username: Admin", bg=c_verde, fg="white", font=("Arial", 14))
    rol_label.pack(padx=10)

    username = tk.Label(recuadro_inferior, text="Rol: Administrador", bg=c_verde, fg="white", font=("Arial", 14))
    username.pack(padx=10)

    #configuramos el cierre de ventana
    ventana_dashboard.protocol("WM_DELETE_WINDOW", lambda:cerrar_sesion(ventana_dashboard))

    ventana_dashboard.mainloop()

    ventana_dashboard.destroy()
