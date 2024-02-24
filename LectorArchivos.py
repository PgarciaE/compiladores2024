import tkinter as tk
from tkinter import filedialog

def seleccionar_y_leer_archivo():
    # Limpiar el widget Text antes de agregar nuevos elementos
    text_widget.delete('1.0', tk.END)
    
    # Mostrar el cuadro de diálogo para seleccionar un archivo y almacenar la ruta del archivo seleccionado
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if ruta_archivo:  # Verificar si se seleccionó un archivo
        # Abrir el archivo en modo de solo lectura ('r') y leer su contenido
        with open(ruta_archivo, 'r') as archivo:
            contenido_completo = archivo.read()
            text_widget.insert(tk.END, contenido_completo)  # Mostrar el contenido en el widget de texto

def crear_ventana():
    global text_widget
    ventana = tk.Tk()
    ventana.title("Visualizador de Archivos TXT")
    ventana.geometry("800x600")  # Ajustar las dimensiones de la ventana

    # Crear un widget Text para el contenido del archivo
    text_widget = tk.Text(ventana)
    text_widget.pack(expand=True, fill=tk.BOTH)

    # Crear un botón para seleccionar archivo
    boton_seleccionar = tk.Button(ventana, text="Seleccionar archivo TXT", command=seleccionar_y_leer_archivo)
    boton_seleccionar.pack(pady=10)

    # Ejecutar el bucle principal de la interfaz gráfica
    ventana.mainloop()

# Llamar a la función para crear y mostrar la ventana
crear_ventana()
