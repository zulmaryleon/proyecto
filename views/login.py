import tkinter as tk
from customtkinter  import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkCheckBox
from tkinter import messagebox, ttk
from app.login import iniciar_sesion, on_enter
from app.utils import c_negro, c_verde, c_morado, c_rojo, c_azul, c_blanco, c_gris, redimensionar_imagen

def crear_vista_login():
    root = CTk() 
    root.geometry("500x600+350+20")
    root.minsize(480, 500)
    root.config(bg = c_negro)
    root.title("Iniciar Sesion")

    frame = CTkFrame(root, fg_color= c_negro)
    frame.grid(column=0, row = 0, sticky='nsew',padx=50, pady=50)

    frame.columnconfigure([0,1], weight=1)
    frame.rowconfigure([0,1,2,3,4,5], weight=1)

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    logo = tk.PhotoImage(file='imagenes/logo.png') 
    img_google = tk.PhotoImage(file='imagenes/user.png')
    img_facebook = tk.PhotoImage(file='imagenes/user.png')

    imagen_central = redimensionar_imagen(logo, 225, 225),

    imagen_label = tk.Label(frame, image=imagen_central, bg=c_negro).grid(columnspan=2, row=0)

    usuario_entry = CTkEntry(frame, placeholder_text= 'Usuario', 
        border_color=c_azul, fg_color= c_blanco, width =220,height=40)
    usuario_entry.grid(columnspan=2, row=1,padx=4, pady =4)

    password_entry = CTkEntry(frame,show="*", placeholder_text= 'Contraseña',
     border_color= c_azul, fg_color= c_blanco, width =220,height=40)
    password_entry.grid(columnspan=2, row=2,padx=4, pady =4)

    checkbox = CTkCheckBox(frame, text="Recordarme",hover_color= c_rojo, 
        border_color=c_azul, fg_color=c_azul)
    checkbox.grid(columnspan=2, row=3,padx=4, pady =4)

    bt_iniciar = CTkButton(frame, border_color=c_azul, fg_color = c_negro,
        hover_color=c_azul,corner_radius=12,border_width=2,
        text='INICIAR SESIÓN', command=lambda: iniciar_sesion(usuario_entry, password_entry, root))
    bt_iniciar.grid(columnspan=2, row=4,padx=4, pady =4)

    # Configura el evento Enter en la ventana principal
    root.bind("<Return>", lambda event: on_enter(event, usuario_entry, password_entry, root))

    # Inicia el carrusel automático
    #avanzar_carrusel()

    root.call('wm', 'iconphoto', root._w, logo)
    root.mainloop()

