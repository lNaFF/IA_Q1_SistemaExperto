import tkinter as tk
from tkinter import ttk, scrolledtext
from clips import Environment

# Inicializar CLIPS
env = Environment()
env.load("motos.clp")  # Carga tu base de conocimiento
env.reset()

# ---------------- INTERFAZ ----------------
root = tk.Tk()
root.title("Sistema Experto: Recomendador de Motocicletas")
root.geometry("1200x550")  # Ajusta el tamaño de la ventana

# Variables de usuario
nombre_var = tk.StringVar(value='')
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

def actualizar_agenda(*args):
    """Actualiza la agenda cuando cambian los valores seleccionados"""
    # Crear nuevo ambiente temporal para no afectar la ejecución principal
    temp_env = Environment()
    temp_env.load("motos.clp")
    temp_env.reset()

    # Solo crear el hecho si todos los campos tienen valor
    if (presupuesto_var.get() and experiencia_var.get() and uso_var.get() 
        and estilo_var.get() and cilindraje_var.get() and preferencia_var.get()):
        
        fact_str = f"""
        (usuario
            (presupuesto {presupuesto_var.get()})
            (experiencia {experiencia_var.get()})
            (uso {uso_var.get()})
            (estilo {estilo_var.get()})
            (cilindraje {cilindraje_var.get()})
            (preferencia {preferencia_var.get()}))
        """
        temp_env.assert_string(fact_str)

        # Actualizar agenda
        agenda_box.delete("1.0", tk.END)
        agenda_box.insert(tk.END, "Reglas que se activarán:\n")
        for activation in temp_env.activations():
            agenda_box.insert(tk.END, f"- {activation.name}\n")

# Modificar las variables para que llamen a actualizar_agenda
presupuesto_var.trace_add("write", actualizar_agenda)
experiencia_var.trace_add("write", actualizar_agenda)
uso_var.trace_add("write", actualizar_agenda)
estilo_var.trace_add("write", actualizar_agenda)
cilindraje_var.trace_add("write", actualizar_agenda)
preferencia_var.trace_add("write", actualizar_agenda)

# Función para recomendar
def recomendar():
    # Limpiar el log antes de mostrar nuevas reglas
    log_box.delete("1.0", "end")
    # Resetear entorno
    env.clear()   
    env.load("motos.clp")
    env.reset()

    # Insertar hechos de usuario
    fact_str = f"""
    (usuario
        (nombre "{nombre_var.get()}")
        (presupuesto {presupuesto_var.get()})
        (experiencia {experiencia_var.get()})
        (uso {uso_var.get()})
        (estilo {estilo_var.get()})
        (cilindraje {cilindraje_var.get()})
        (preferencia {preferencia_var.get()}))
    """
    env.assert_string(fact_str)
    
        # Limpiar agenda después de ejecutar las reglas
    agenda_box.delete("1.0", tk.END)
    agenda_box.insert(tk.END, "Agenda vacía - Reglas ejecutadas")
    
    # Ejecutar reglas
    env.run()

    # Buscar recomendaciones
    recomendaciones = []
    for fact in env.facts():
        if fact.template.name == "recomendacion":
            recomendaciones.append(fact["moto"] + " → " + fact["razon"])

    # Mostrar resultado
    nombre = nombre_var.get() if nombre_var.get() else "Usuario"
    if recomendaciones:
        resultado_label.config(text=f"{nombre}, te recomendamos la: {'. '.join(recomendaciones)}")
    else:
        resultado_label.config(text=f"Lo siento {nombre}, no encontramos una recomendación para tu perfil.")

    reglas = env.eval("(find-all-facts ((?f regla-activa)) TRUE)")
    
    for r in reglas:
        print("Se activó la regla:", r["nombre"])
        log_box.insert("end", f"Se activó la regla: {r['nombre']}\n")
        


# ---------------- UI ----------------
frame = ttk.Frame(root, padding=20)
frame.grid()

# Widgets
# Campos de entrada - Agregar el campo de nombre al inicio
ttk.Label(frame, text="Nombre:").grid(row=0, column=0, sticky=tk.W, pady=5)
ttk.Entry(frame, textvariable=nombre_var).grid(row=0, column=0, pady=5, padx=80)

ttk.Label(frame, text="Presupuesto:").grid(row=0, column=1, sticky="w")
ttk.OptionMenu(frame, presupuesto_var, presupuestos[0], *presupuestos).grid(row=0, column=1, padx=100)

ttk.Label(frame, text="Experiencia:").grid(row=1, column=1, sticky="w")
ttk.OptionMenu(frame, experiencia_var, experiencias[0], *experiencias).grid(row=1, column=1, padx=100)

ttk.Label(frame, text="Uso principal:").grid(row=2, column=1, sticky="w")
ttk.OptionMenu(frame, uso_var, usos[0], *usos).grid(row=2, column=1, padx=100)

ttk.Label(frame, text="Estilo:").grid(row=3, column=1, sticky="w")
ttk.OptionMenu(frame, estilo_var, estilos[0], *estilos).grid(row=3, column=1, padx=100)

ttk.Label(frame, text="Cilindraje:").grid(row=4, column=1, sticky="w")
ttk.OptionMenu(frame, cilindraje_var, cilindrajes[0], *cilindrajes).grid(row=4, column=1, padx=100)

ttk.Label(frame, text="Preferencia:").grid(row=5, column=1, sticky="w")
ttk.OptionMenu(frame, preferencia_var, preferencias[0], *preferencias).grid(row=5, column=1, padx=100)

ttk.Button(frame, text="Recomendar Moto", command=recomendar).grid(row=6, column=0, columnspan=1, pady=10)

resultado_label = ttk.Label(frame, text="", foreground="blue", wraplength=400)
resultado_label.grid(row=7, column=0, columnspan=2)

ttk.Label(frame, text="Reglas activadas:").grid(row=8, column=0, sticky="w")
log_box = scrolledtext.ScrolledText(frame, width=75, height=10)
log_box.grid(row=9, column=0, pady=5)

ttk.Label(frame, text="Agenda:").grid(row=8, column=1, sticky="w")
agenda_box = scrolledtext.ScrolledText(frame, width=75, height=10)
agenda_box.grid(row=9, column=1, pady=5)

root.mainloop()
