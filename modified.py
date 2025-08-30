import tkinter as tk
from tkinter import ttk
import clips
import sys
import io

# Redirigir prints a un buffer
class ConsoleRedirect(io.StringIO):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def write(self, msg):
        if msg.strip():  # evitar líneas vacías
            self.text_widget.insert(tk.END, msg + "\n")
            self.text_widget.see(tk.END)  # auto scroll

    def flush(self):
        pass

# Función para ejecutar CLIPS
def ejecutar_clips():
    # Limpiar recomendaciones y logs
    resultado_text.delete("1.0", tk.END)
    detalle_text.delete("1.0", tk.END)

    # Capturar valores seleccionados
    presupuesto = presupuesto_var.get()
    experiencia = experiencia_var.get()
    uso = uso_var.get()
    estilo = estilo_var.get()
    cilindraje = cilindraje_var.get()
    preferencia = preferencia_var.get()

    # Insertar valores en CLIPS
    env = clips.Environment()
    env.load("motos.clp")
    env.reset()

    env.assert_string(f"(usuario (presupuesto {presupuesto}) (experiencia {experiencia}) "
                      f"(uso {uso}) (estilo {estilo}) (cilindraje {cilindraje}) (preferencia {preferencia}))")

    # Mostrar la salida en detalle_text
    old_stdout = sys.stdout
    sys.stdout = ConsoleRedirect(detalle_text)
    
    try:
        env.run()
    finally:
        # Restaurar stdout
        sys.stdout = old_stdout

    # Mostrar recomendaciones en UI
    for fact in env.facts():
        if fact.template.name == "recomendacion":
            moto = fact["moto"]
            razon = fact["razon"]
            resultado_text.insert(tk.END, f"Motocicleta recomendada: {moto}\n")
            resultado_text.insert(tk.END, f"Razón: {razon}\n")
            
    # Mostrar la agenda de CLIPS en el campo agenda_text
    agenda_text.delete("1.0", tk.END)
    for activation in env.activations():
        agenda_text.insert(tk.END, f"{activation.name}\n")

# --- UI Base ---
root = tk.Tk()
root.title("Sistema Experto - Recomendación de Motocicletas")

# Frame principal
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Variables
presupuesto_var = tk.StringVar()
experiencia_var = tk.StringVar()
uso_var = tk.StringVar()
estilo_var = tk.StringVar()
cilindraje_var = tk.StringVar()
preferencia_var = tk.StringVar()

# Opciones
presupuestos = ["Bajo", "Medio", "Alto"]
experiencias = ["Principiante", "Intermedio", "Experto"]
usos = ["Urbano", "Carretera", "Trabajo", "Deportivo", "Trocha"]
estilos = ["Naked", "Deportiva", "Turismo", "Automática", "Doble-Proposito"]
cilindrajes = ["Bajo", "Medio", "Alto"]
preferencias = ["Economía", "Potencia", "Comodidad", "Estética"]

# Campos de entrada
ttk.Label(frame, text="Presupuesto:").grid(row=0, column=0, sticky=tk.W, pady=5)
ttk.Combobox(frame, textvariable=presupuesto_var, values=presupuestos).grid(row=0, column=0, pady=5, padx=80)

ttk.Label(frame, text="Experiencia:").grid(row=1, column=0, sticky=tk.W, pady=5)
ttk.Combobox(frame, textvariable=experiencia_var, values=experiencias).grid(row=1, column=0, pady=5, padx=80)

ttk.Label(frame, text="Uso principal:").grid(row=2, column=0, sticky=tk.W, pady=5)
ttk.Combobox(frame, textvariable=uso_var, values=usos).grid(row=2, column=0, pady=5, padx=80)

ttk.Label(frame, text="Estilo:").grid(row=3, column=0, sticky=tk.W, pady=5)
ttk.Combobox(frame, textvariable=estilo_var, values=estilos).grid(row=3, column=0, pady=5, padx=80)

ttk.Label(frame, text="Cilindraje:").grid(row=4, column=0, sticky=tk.W, pady=5)
ttk.Combobox(frame, textvariable=cilindraje_var, values=cilindrajes).grid(row=4, column=0, pady=5, padx=80)

ttk.Label(frame, text="Preferencia:").grid(row=5, column=0, sticky=tk.W, pady=5)
ttk.Combobox(frame, textvariable=preferencia_var, values=preferencias).grid(row=5, column=0, pady=5, padx=80)

# Botón
ttk.Button(frame, text="Recomendar Moto", command=ejecutar_clips).grid(row=6, column=0, columnspan=1, pady=10)

# ...existing code...

# Resultados
ttk.Label(frame, text="Recomendación:").grid(row=7, column=0, sticky=tk.W, pady=5)
resultado_text = tk.Text(frame, height=3, width=50)  # Cambia width si lo deseas
resultado_text.grid(row=7, column=0, padx=100, sticky=tk.W)

# Reglas activadas y Agenda en la misma fila
ttk.Label(frame, text="Reglas activadas:").grid(row=8, column=0, sticky=tk.W, pady=5)
ttk.Label(frame, text="Agenda:").grid(row=8, column=1, sticky=tk.W, pady=5)

detalle_text = tk.Text(frame, height=10, width=50)
detalle_text.grid(row=9, column=0, padx=5)

agenda_text = tk.Text(frame, height=10, width=50)
agenda_text.grid(row=9, column=1, padx=5)

# ...existing code...

root.mainloop()
