import tkinter as tk
from tkinter import messagebox

class PantallaRegistrarResultado:
    def __init__(self, gestor):
        self.gestor = gestor
        self.root = tk.Tk()
        self.root.title("Registrar Resultado de Revisión Manual")
        self.root.focus_force()
        self.btn_iniciar = None
 

    def opcRegistrarResultado(self):
        # Habilita el botón para registrar resultado manual
        if not self.btn_iniciar:
            self.btn_iniciar = tk.Button(self.root, text="Registrar resultado manual", command=self.habilitar)
            self.btn_iniciar.pack(pady=10)
        else:
            self.btn_iniciar.config(state="normal")


    def habilitar(self):
        # Llama al gestor para obtener la lista ordenada y la muestra
        # eventos = self.gestor.buscarEventosAutoDetectados()
        # eventos_ordenados = self.gestor.ordenarPorFechayHora(eventos)
        # self.presentarEventos(eventos_ordenados)
        self.gestor.opcRegistrarResultado()


    def presentarEventos(self, eventos_auto_detectados):
        # Limpia widgets anteriores excepto el botón principal
        for widget in self.root.winfo_children():
            if widget != self.btn_iniciar:
                widget.destroy()
        if eventos_auto_detectados:
            tk.Label(self.root, text="Seleccione un evento:").pack(pady=5)
            for idx, evento in enumerate(eventos_auto_detectados):
                texto = (
                    f"Evento {idx+1}:\n"
                    f"  Fecha/Hora: {evento['fechaHoraOcurrencia']}\n"
                    f"  Lat Epicentro: {evento['latitudEpicentro']}\n"
                    f"  Long Epicentro: {evento['longitudEpicentro']}\n"
                    f"  Lat Hipocentro: {evento['latitudHipocentro']}\n"
                    f"  Long Hipocentro: {evento['longitudHipocentro']}\n"
                    f"  Magnitud: {evento['valorMagnitud']}\n"
                )
                
                frame = tk.Frame(self.root, relief=tk.RIDGE, borderwidth=2)
                frame.pack(fill=tk.X, padx=10, pady=5)
                tk.Label(frame, text=texto, justify=tk.LEFT, anchor="w").pack(side=tk.LEFT, padx=5)
                btn = tk.Button(frame, text="Seleccionar", command=lambda i=idx: self.opcSeleccionarEvento(eventos_auto_detectados, i))
                btn.pack(side=tk.RIGHT, padx=5)
        else:
            messagebox.showinfo("Sin eventos", "No hay eventos sísmicos para revisar.")

    def opcSeleccionarEvento(self, eventos, idx):
        #self.gestor.eventoSismicoSeleccionado = eventos[idx]
        messagebox.showinfo("Evento seleccionado", f"Seleccionaste el evento {idx+1}")
        self.gestor.seleccionarEventoSismico(eventos[idx])
        
    
    def habilitarOpcionMapaSismico(self):
        messagebox.showinfo("Se habilita opción para mapa sísmico")

    def solicitarOpcionVisualizarMapa(self):
        messagebox.showinfo("Mapa sísmico mostrado (simulado)")

    def habilitarOpcionModificacionDatos(self):
        messagebox.showinfo("Se habilita opción para modificar magnitud, alcance u origen")

    def solicitarOpcionModifiacionDatos(self):
        print("Simular modificación de datos del evento (opcional)")

    def habilitarOpciones(self):
        print("Opciones habilitadas: Confirmar / Rechazar / Solicitar revisión a experto")

    def solicitarSeleccionarOpcion(self):
        opciones = ["Confirmar evento", "Rechazar evento", "Solicitar revisión a experto"]
        seleccion = simpledialog.askinteger("Acción", f"Seleccione una acción:\n" + "\n".join(f"{i}: {opciones[i]}" for i in range(len(opciones))))
        if seleccion == 1:
            self.gestor.registrarRechazo()
        elif seleccion == 0:
            print("Evento confirmado (simulado)")
        elif seleccion == 2:
            print("Evento derivado a experto (simulado)")
        self.gestor.finCU()

    def ingresarSeleccion(self):
        return simpledialog.askstring("Ingreso", "Ingrese selección (texto libre)")

