import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel
from PIL import Image, ImageTk

# Función para abrir la ventana con la imagen al hacer clic en el botón "Consultar"
def abrir_ventana_imagen():
    ventana_imagen = Toplevel(ventana)
    ventana_imagen.title("Imagen")
    # Mostrar la ventana emergente
    ventana_imagen.mainloop()
    

# Crear una ventana
ventana = tk.Tk()
ventana.title("Sistema experto")
ventana.geometry("700x655")  # Aumentar el ancho de la ventana
ventana.configure(background="#F08080")  # Cambiar el color de fondo
ventana.resizable(False, False)  # Hacer que la ventana no sea redimensionable


# Crear frames para organizar elementos

frame_imagen = tk.Frame(ventana, bg="#F08080")
frame_imagen.pack()

frame_izquierda = tk.Frame(ventana, bg="#F08080")
frame_izquierda.pack(side="left", padx=20, pady=20, fill="y")

frame_derecha = tk.Frame(ventana, bg="#F08080")
frame_derecha.pack(side="right", padx=20, pady=20, fill="y")




# Carga de la imagen
imagen = Image.open("LOGO.png")  # Reemplaza con la ruta de tu imagen
imagen_tk = ImageTk.PhotoImage(imagen)

# Mostrar la imagen en un label dentro del Frame
etiqueta_imagen = tk.Label(frame_imagen, image=imagen_tk)
etiqueta_imagen.pack()

# Elementos en la columna izquierda
etiqueta_encabezado = tk.Label(frame_imagen, text="SISTEMA EXPERTO COMIDAS", font=("OCR A Extended", 24, "bold"), foreground="black", background="#F08080")
etiqueta_encabezado.pack(pady=7)

# Lista desplegable (Caliente/Frío)
etiqueta_texto2 = tk.Label(frame_izquierda, text="Temperatura de la comida", font=("OCR A Extended", 14, "bold"), foreground="black", background="#F08080")
etiqueta_texto2.pack()
opciones_caliente_frio = ["Caliente", "Frío"]
lista_desplegable_caliente_frio = ttk.Combobox(frame_izquierda, values=opciones_caliente_frio, state='readonly')
lista_desplegable_caliente_frio.set("Seleccionar opción")
lista_desplegable_caliente_frio.config(font=("OCR A Extended", 14, "bold"))
lista_desplegable_caliente_frio.pack(pady=7)


# Texto 3 y Lista desplegable (Dulce/Salado)
etiqueta_texto3 = tk.Label(frame_izquierda, text="Sabor de la comida", font=("OCR A Extended", 14, "bold"), foreground="black", background="#F08080")
etiqueta_texto3.pack()
opciones_caliente_frio = ["Caliente", "Frío"]
lista_desplegable_caliente_frio = ttk.Combobox(frame_izquierda, values=opciones_caliente_frio, state='readonly')
lista_desplegable_caliente_frio.set("Seleccionar opción")
lista_desplegable_caliente_frio.config(font=("OCR A Extended", 14, "bold"),foreground="black", background="#F08080")
lista_desplegable_caliente_frio.pack(pady=7)

# Texto 4 y Lista desplegable (Mañana/Tarde/Noche)
etiqueta_texto4 = tk.Label(frame_izquierda, text="Tiempo libre para comer", font=("OCR A Extended", 14, "bold"), foreground="black", background="#F08080")
etiqueta_texto4.pack()
opciones_mtn = ["Mañana", "Tarde", "Noche"]
lista_desplegable_mtn = ttk.Combobox(frame_izquierda, values=opciones_mtn)
lista_desplegable_mtn.set("Seleccionar opción")
lista_desplegable_mtn.config(font=("OCR A Extended", 14, "bold"), foreground="black", background="#F08080")
lista_desplegable_mtn.pack(pady=7)

# Texto 5 y Lista desplegable (Vegano/Vegetariano/Omnívoro)
etiqueta_texto5 = tk.Label(frame_izquierda, text="Restriccion alimenticia", font=("OCR A Extended", 14, "bold"), foreground="black", background="#F08080")
etiqueta_texto5.pack()
opciones_comida = ["Vegano", "Vegetariano", "Omnívoro"]
lista_desplegable_comida = ttk.Combobox(frame_izquierda, values=opciones_comida)
lista_desplegable_comida.set("Seleccionar opción")
lista_desplegable_comida.config(font=("OCR A Extended", 14, "bold"), foreground="black", background="#F08080")
lista_desplegable_comida.pack(pady=7)


# Texto 6 y Lista desplegable (Si/No)
etiqueta_texto6 = tk.Label(frame_izquierda, text="Le gusta el picante?", font=("OCR A Extended", 14, "bold"), foreground="black", background="#F08080")
etiqueta_texto6.pack()
opciones_si_no = ["Si", "No"]
lista_desplegable_si_no = ttk.Combobox(frame_izquierda, values=opciones_si_no)
lista_desplegable_si_no.set("Seleccionar opción")
lista_desplegable_si_no.config(font=("OCR A Extended", 14, "bold"), foreground="black", background="#F08080")
lista_desplegable_si_no.pack(pady=7)


boton_consultar = tk.Button(frame_izquierda, text="Consultar", font=("OCR A Extended", 14, "bold"), command=abrir_ventana_imagen, bg="#9C33FF")
boton_consultar.pack(pady=7)

# ... (Puedes agregar más elementos aquí siguiendo un patrón similar)

# Elementos en la columna derecha

etiqueta_respuesta = tk.Label(frame_derecha, text="Respuesta", font=("OCR A Extended", 14, "bold"), foreground="black", background="#F08080")
etiqueta_respuesta.pack(pady=10)

campo_texto = tk.Entry(frame_derecha, font=("OCR A Extended", 14, "bold"))
campo_texto.pack()

etiqueta_imagen = tk.Label(frame_derecha, text="Imagen", font=("OCR A Extended", 14, "bold"), foreground="black", background="#F08080")
etiqueta_imagen.pack()

campo_texto2 = tk.Entry(frame_derecha, font=("OCR A Extended", 14, "bold"))
campo_texto2.pack(pady=5)

boton1 = tk.Button(frame_derecha, text="Explicar respuesta", font=("OCR A Extended", 14, "bold"))
boton1.pack(pady=10)

boton2 = tk.Button(frame_derecha, text="Siguiente consulta", font=("OCR A Extended", 14, "bold"))
boton2.pack(pady=10)

# Iniciar el bucle principal
ventana.mainloop()
