import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel


class PantallaRegistrarResultado:
    def __init__(self, gestor):
        #Relacion otras clases:
        self.gestor = gestor

        self.root = tk.Tk()
        self.root.title("Registrar Resultado de Revisión Manual")
        self.root.focus_force()

        #Atributos propios:
        self.btn_iniciar = None
        self.btnSeleccionarEvento = None
        self.listaEventosSismicos = None
        self.btnMapaSismico = None
        self.btnModificacionDatos = None
        self.listaSeriesTemporales = None
        self.grillOpciones = None
        self.btnIngresarOpcion = None
        self.evento_dict = None
 

    def opcRegistrarResultado(self):
        # Habilita el botón para registrar resultado manual
        if not self.btn_iniciar:
            self.btn_iniciar = tk.Button(self.root, text="Registrar resultado manual", command=self.habilitar)
            self.btn_iniciar.pack(pady=10)
        else:
            self.btn_iniciar.config(state="normal")


    def habilitar(self):
        # Llama al gestor para obtener la lista ordenada y la muestra
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
        print(f"Llamado a opcSeleccionarEvento con idx={idx}")
        self.evento_dict = eventos[idx]
        print(f"evento_dict: {self.evento_dict}")
        evento_obj = self.evento_dict.get("objeto") # Obtiene el objeto real
        if evento_obj is None:
            messagebox.showerror("Error", "No se encontró el objeto EventoSismico en el diccionario.")
            return
        messagebox.showinfo("Evento seleccionado", f"Seleccionaste el evento {idx+1}")
        self.gestor.seleccionarEvento(evento_obj)
        
    
    def habilitarOpcionMapaSismico(self):
        print("Se habilita opción para mapa sísmico") 

    def habilitarOpcionEstacionSismologica(self):
        print("Se habilita opción para visualizar estación sismológica")

    def solicitarOpcionVisualizarMapa(self):
        # messagebox.showinfo("Mapa sísmico mostrado (simulado)")
        messagebox.askyesno("Visualizar mapa", "¿Desea visualizar el mapa sísmico?")
        self.opcMapaSismico()

    def opcMapaSismico(self):
        self.gestor.tomarMapaSismico()



    def habilitarOpcionModificacionDatos(self):
        print("Se habilita opción para modificar magnitud, alcance u origen")

    def solicitarOpcionModifiacionDatos(self):
        messagebox.askyesno("Datos evento", "¿Desea Modificar los datos?")
        self.opcModificarDatos()

    def opcModificarDatos(self):
        self.gestor.tomarModificacionDatos()


    def habilitarOpciones(self):
        print("Opciones habilitadas: Confirmar / Rechazar / Solicitar revisión a experto")

       
    # def solicitarSeleccionarOpcion(self):
    #     opciones = ["aceptar", "rechazar", "derivar"]
    #     seleccion = simpledialog.askinteger("Acción", f"Seleccione una acción:\n" + "\n".join(f"{i}: {opciones[i]}" for i in range(len(opciones))))
    #     if seleccion == 1:
    #         self.gestor.registrarRechazo()
    #     elif seleccion == 0:
    #         print("Evento confirmado (simulado)")
    #     elif seleccion == 2:
    #         print("Evento derivado a experto (simulado)")
    #     self.gestor.finCU()

    # def ingresarSeleccion(self):
    #     return simpledialog.askstring("Ingreso", "Ingrese selección (texto libre)")
    def solicitarSeleccionarOpcion(self):
        ventana = Toplevel()
        ventana.title("Revision de Evento Sismico")
        ventana.geometry("300x200")
        ventana.resizable(True, True)

        label = tk.Label(ventana, text="Datos de evento seleccionado")
        label.pack(pady=10)
        datos_evento = (
            f"  Fecha/Hora: {self.evento_dict['fechaHoraOcurrencia']}\n"
            f"  Lat Epicentro: {self.evento_dict['latitudEpicentro']}\n"
            f"  Long Epicentro: {self.evento_dict['longitudEpicentro']}\n"
            f"  Lat Hipocentro: {self.evento_dict['latitudHipocentro']}\n"
            f"  Long Hipocentro: {self.evento_dict['longitudHipocentro']}\n"
            f"  Magnitud: {self.evento_dict['valorMagnitud']}\n"
        )
        frame = tk.Frame(ventana, relief=tk.RIDGE, borderwidth=2)  # Usar 'ventana' en vez de 'self.root'
        frame.pack(fill=tk.X, padx=10, pady=5)
        tk.Label(frame, text=datos_evento, justify=tk.LEFT, anchor="w").pack(side=tk.LEFT, padx=5)

        label = tk.Label(ventana, text="¿Qué desea hacer con el evento?")
        label.pack(pady=10)

        # Botón Aceptar
        btn_aceptar = tk.Button(ventana, text="Aceptar", width=20, command=lambda: self.opcion_seleccionada("aceptar", ventana))
        btn_aceptar.pack(pady=5)

        # Botón Rechazar
        btn_rechazar = tk.Button(ventana, text="Rechazar", width=20, command=lambda: self.opcion_seleccionada("rechazar", ventana))
        btn_rechazar.pack(pady=5)

        # Botón Derivar
        btn_derivar = tk.Button(ventana, text="Derivar", width=20, command=lambda: self.opcion_seleccionada("derivar", ventana))
        btn_derivar.pack(pady=5)

    def opcion_seleccionada(self, opcion, ventana):
        ventana.destroy()  # Cierra la ventana 
        self.gestor.tomarSeleccion(opcion)
        
        # self.gestor.finCU()