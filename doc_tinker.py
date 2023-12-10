import tkinter as tk

def on_button_click():
    print("¡Has hecho clic en el botón!")

# Crea una nueva ventana
root = tk.Tk()

# Crea un nuevo botón
button = tk.Button(root, text="Haz clic en mí", command=on_button_click)

# Añade el botón a la ventana
button.pack()

# Inicia el bucle principal de la aplicación
root.mainloop()
