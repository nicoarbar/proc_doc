import tkinter as tk
import os
import sys


def on_button_click_proc():
    print("¡Has hecho clic en el botón!")
    os.system('proc_doc.py')

# Crea una nueva ventana
root = tk.Tk()

# Crea una etiqueta con texto
label = tk.Label(root, text = "Hola, Felipe!")

# Agrega la etiqueta a la ventana principal
label.pack()

# Crea un nuevo botón
button = tk.Button(root, text = "Haz clic para la automatizacion de documentos", command=on_button_click_proc)

# Añade el botón a la ventana
button.pack()

label = tk.Label(root, text = "Se han procesado tus docs")
label.pack()

# Inicia el bucle principal de la aplicación
#root.mainloop()

class StdOutRedirect:
    def __init__(self, text: tk.Text) -> None:
        self._text = text

    def write(self, out: str) -> None:
        self._text.insert(tk.END, out)

class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.stdout_text = tk.Text(self, bg="black", fg="#00FF00", font=("Consolas", 11))
        self.stdout_text.pack(expand=True, fill=tk.BOTH)
        sys.stdout = StdOutRedirect(self.stdout_text)

if __name__ == "__main__":
    root = tk.Tk()
    App(root).pack(expand=True, fill=tk.BOTH)

    print("Prueba Nicolas")

    root.mainloop()
