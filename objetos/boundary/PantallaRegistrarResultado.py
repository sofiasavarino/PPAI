import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel

class PantallaRegistrarResultado:
    def __init__(self, gestor):
        # Relación con otras clases:
        self.gestor = gestor

        #Atributos de inicializacion de ventana(ya viene creada)
        self.root = tk.Tk()
        self.root.title("Registrar Resultado de Revisión Manual")
        self.root.configure(bg="#F5F5DC")  # Fondo oscuro elegante
        self.root.state('zoomed')  # Pantalla completa al iniciar
        self.root.focus_force()


        # Atributos propios:
        self.btn_iniciar = None
        self.btnSeleccionarEvento = None
        self.listaEventosSismicos = None
        self.btnMapaSismico = None
        self.btnModificacionDatos = None
        self.listaSeriesTemporales = None



        # Título principal grande
        self.titulo = tk.Label(
            self.root,
            text="Sistema de Gestión de Eventos Sísmicos",
            font=("Arial", 28, "bold"),
            bg="#F5F5DC",
            fg="#654321"
        )
        self.titulo.pack(pady=30)
         # Cargar la imagen PNG
        self.logo_img = tk.PhotoImage(file="/Users/sofiasavarino/Downloads/Materias 3ro/DSI/CODIGO_git/PPAI/objetos/img-principal.png")
        # Mostrar la imagen en la ventana principal
        self.logo_label = tk.Label(self.root, image=self.logo_img, bg="#232946")
        self.logo_label.pack(pady=20)


        #No seria grilla, es mas facil hacerlo con botones independientes
        #self.grillOpciones = None
        self.btnIngresarOpcion = None
        self.evento_dict = None
        self.btnListar_eventos = None



    def opcRegistrarResultado(self):
        # Habilita el botón para registrar resultado manual
        if not self.btn_iniciar:
            self.btn_iniciar = tk.Button(
                self.root,
                text="Registrar resultado manual",
                command=self.habilitar,
                font=("Arial", 16, "bold"),
                bg="#654321",
                fg="#654321",
                relief=tk.FLAT,
                bd = 0
            )
            self.btn_iniciar.pack(pady=20)
        else:
            self.btn_iniciar.config(state="normal")

        if not self.btnListar_eventos:
            self.btnListar_eventos = tk.Button(
                self.root,
                text="Listar Todos los Eventos sismicos",
                command=self.mostrar_lista_eventos,
                font=("Arial", 16, "bold"),
                bg="#654321",
                fg="#654321",
                relief=tk.FLAT,
                bd = 0
            )
            self.btnListar_eventos.pack(pady=20)
        else:
            self.btnListar_eventos.config(state="normal")


    def habilitar(self):
        self.gestor.opcRegistrarResultado()


    def presentarEventos(self, eventos_auto_detectados):
        # Limpia widgets anteriores excepto el título y el botón principal
        for widget in self.root.winfo_children():
            if widget not in [self.titulo, self.btnListar_eventos]:
                widget.destroy()
        if eventos_auto_detectados:
            tk.Label(
                self.root,
                text="Seleccione un evento:",
                font=("Arial", 18, "bold"),
                bg="#F5F5DC",
                fg="#654321"
            ).pack(pady=10)
            for idx, evento in enumerate(eventos_auto_detectados):
                texto = (
                    f"Evento {idx+1}:\n"
                    f"  Fecha/Hora: {evento['fechaHoraOcurrencia']}\n"
                    f"  Latitud Epicentro: {evento['latitudEpicentro']}\n"
                    f"  Longitud Epicentro: {evento['longitudEpicentro']}\n"
                    f"  Latitud Hipocentro: {evento['latitudHipocentro']}\n"
                    f"  Longitud Hipocentro: {evento['longitudHipocentro']}\n"
                    f"  Magnitud: {evento['valorMagnitud']}\n"
                )
                frame = tk.Frame(self.root, relief=tk.RIDGE, borderwidth=2, bg="#F5F5DC")
                frame.pack(fill=tk.X, padx=40, pady=10)
                tk.Label(frame, text=texto, justify=tk.LEFT, anchor="w", font=("Consolas", 15),
                    bg="#F5F5DC",
                    fg="#000000"
                ).pack(side=tk.LEFT, padx=10, pady=10)

                btn = tk.Button(frame, text="Seleccionar",
                    command=lambda i=idx: self.opcSeleccionarEvento(eventos_auto_detectados, i),
                    font=("Arial", 12, "bold"),bg="#654321", fg="#654321", activebackground="#654321", activeforeground="#654321",
                    relief=tk.FLAT,   # Quita el efecto de relieve
                    bd=0,             # Grosor del borde en 0
                    highlightthickness=0,  # Elimina borde de foco
                    highlightbackground="#F5F5DC",  # Color del fondo del borde de foco (por si lo muestra igual)
                    highlightcolor="#F5F5DC"
                    )
                btn.pack(side=tk.RIGHT, padx=15, pady=15)
        else:
            messagebox.showinfo("Sin eventos", "No hay eventos sísmicos para revisar.")


    def opcSeleccionarEvento(self, eventos, idx):
        self.evento_dict = eventos[idx]
        evento_obj = self.evento_dict.get("objeto")  # Obtiene el objeto real
        if evento_obj is None:
            messagebox.showerror("Error", "No se encontró el objeto EventoSismico en el diccionario.")
            return
        #messagebox.showinfo("Evento seleccionado", f"Seleccionaste el evento {idx+1}")
        self.gestor.seleccionarEvento(evento_obj)


    def mostrarDatosEventoSismico(self, detalleEventoSismico):

        ventana = tk.Toplevel(self.root)
        ventana.title("Detalle del Evento Sísmico")
        ventana.geometry("700x600")
        ventana.configure(bg="#654321")

        # Título principal
        tk.Label(ventana,text="Detalle de Evento Sismico",font=("Arial", 28, "bold"),
            bg="#654321",
            fg="#F5F5DC",
        ).grid(row=0, column=0, columnspan=2, padx=10, pady=20)

        alcanceSismo = detalleEventoSismico[0]
        clasificacion = detalleEventoSismico[1]
        origenSismo = detalleEventoSismico[2]
        series = detalleEventoSismico[3]

        fila = 3
        tk.Label(ventana,text="Alcance:",font=('Arial', 16, 'bold'),bg="#654321",fg="#F5F5DC",anchor="w",width=20,relief="solid",bd=0
        ).grid(row=fila, column=0, sticky="w", padx=5, pady=5)

        self.entry_alcanceSismo = tk.Entry(ventana, width=40,
                                   disabledbackground="#e0e0e0",
                                   disabledforeground="#654321")
        self.entry_alcanceSismo.insert(0, str(alcanceSismo))
        self.entry_alcanceSismo.config( state="disabled")
        self.entry_alcanceSismo.grid(row=fila, column=1, sticky="w", padx=5, pady=5)
        fila += 1

        tk.Label(
            ventana,
            text="Clasificación:",
            font=('Arial', 16, 'bold'),
            bg="#654321",
            fg="#F5F5DC",
            anchor="w",
            width=20,
            relief="solid",
            bd=0
        ).grid(row=fila, column=0, sticky="w", padx=5, pady=5)
        self.entry_clasificacion = tk.Entry(ventana, width=40, disabledbackground="#e0e0e0", disabledforeground="#654321")
        self.entry_clasificacion.insert(0, str(clasificacion))
        self.entry_clasificacion.config(state="disabled")
        self.entry_clasificacion.grid(row=fila, column=1, sticky="w", padx=5, pady=5)
        fila += 1

        tk.Label(
            ventana,
            text="Origen:",
            font=('Arial', 16, 'bold'),
            bg="#654321",
            fg="#F5F5DC",
            anchor="w",
            width=20,
            relief="solid",
            bd=0
        ).grid(row=fila, column=0, sticky="w", padx=5, pady=5)
        self.entry_origen = tk.Entry(ventana, width=40,  disabledbackground="#e0e0e0", disabledforeground="#654321")
        self.entry_origen.insert(0, str(origenSismo))
        self.entry_origen.config( state="disabled")
        self.entry_origen.grid(row=fila, column=1, sticky="w", padx=5, pady=5)
        fila += 1

        tk.Label(
            ventana,
            text="Series:",
            font=('Arial', 16, 'bold'),
            bg="#654321",
            fg="#F5F5DC",
            anchor="w",
            width=20,
            relief="solid",
            bd=0
        ).grid(row=fila, column=0, sticky="nw", padx=5, pady=5)
         # Construir el string de series
        series_text = ""
        for estacion, muestras in series:
            series_text += f"Estación: {estacion}\n"
            for muestra in muestras:
                series_text += f"  - {muestra['denominacion']} ({muestra['unidad']}): {muestra['valor']}\n"
            series_text += "\n"

        tk.Label(
            ventana,
            text="Series:",
            font=('Arial', 16, 'bold'),
            bg="#654321",
            fg="#F5F5DC",
            anchor="nw",
            width=20,
            relief="solid",
            bd=0,
            justify="left"
        ).grid(row=fila, column=0, sticky="nw", padx=5, pady=5)
        tk.Label(
            ventana,
            text=series_text,
            bg="#654321",
            fg="#F5F5DC",
            anchor="nw",
            width=40,
            relief="solid",
            bd=2,
            justify="left"
        ).grid(row=fila, column=1, sticky="w", padx=5, pady=5)
        self.btn_guardar = tk.Button(
            ventana,
            text="Guardar cambios",
            font=("Arial", 12, "bold"),
            bg="#F5F5DC",
            fg="#654321",
            activebackground="#654321",
            activeforeground="#654321",
            relief=tk.FLAT,   # Quita el efecto de relieve
            bd=0,             # Grosor del borde en 0
            highlightthickness=0,  # Elimina borde de foco
            highlightbackground="#F5F5DC",  # Color del fondo del borde de foco (por si lo muestra igual)
            highlightcolor="#F5F5DC",
            state="disabled",  # 👈 Deshabilitado al principio
            command=self.guardarCambiosEvento
            
    
        )
        self.btn_guardar.grid(row=fila + 1, column=1, sticky="e", padx=10, pady=10)
        self.habilitarYSolicitarOpciones(ventana)
        ventana.update_idletasks()
        ventana.after(200, self.habilitarYSolicitarOpcionMapaSismico)


    def habilitarYSolicitarOpcionMapaSismico(self):
        print("Se habilita opción para mapa sísmico")
        respuesta = messagebox.askyesno("Visualizar mapa", "¿Desea visualizar en un mapa el evento sísmico y las estaciones sismológicas involucradas?")
        self.opcMapaSismico(respuesta)


    def opcMapaSismico(self, respuesta):
        if respuesta:
            self.gestor.tomarMapaSismico()
        else:
            self.gestor.tomarMapaSismico()


    def habilitarYSolicitarOpcionModifiacionDatos(self):
        rta = messagebox.askyesno("Datos evento", "¿Desea Modificar los datos?")
        self.opcModificarDatos(rta)


    def opcModificarDatos(self, rta):
        if rta:
            # Habilitar los campos para edición
            self.entry_alcanceSismo.config(state="normal")
            self.entry_clasificacion.config(state="normal")
            self.entry_origen.config(state="normal")
            self.btn_guardar.config(state="normal")

        self.gestor.tomarModificacionDatos(rta)

    #Método añadido para alternativa 1(modificar datos)
    def guardarCambiosEvento(self):
        alcance = self.entry_alcanceSismo.get()
        clasificacion = self.entry_clasificacion.get()
        origen = self.entry_origen.get()

        self.gestor.actualizarDatosEvento(alcance, clasificacion, origen)
        
        self.entry_alcanceSismo.config(state="disabled")
        self.entry_clasificacion.config(state="disabled")
        self.entry_origen.config(state="disabled")
        self.btn_guardar.config(state="disabled")

        messagebox.showinfo("Cambios guardados", "Los datos fueron actualizados correctamente.")


    def habilitarYSolicitarOpciones(self, ventana):
        print("Opciones habilitadas: Confirmar / Rechazar / Solicitar revisión a experto")
        btn_frame = tk.Frame(ventana, bg="#654321")
        btn_frame.grid(row=10, column=0, columnspan=2, pady=40 )

        btn_aceptar = tk.Button(
            btn_frame,
            text="Confirmar",
            width=18,
            font=("Arial", 12, "bold"),
            bg="#023C0C",
            fg="#654321",
            activebackground="#654321",
            activeforeground="#654321",
            relief=tk.FLAT,   # Quita el efecto de relieve
            bd=0,             # Grosor del borde en 0
            highlightthickness=0,  # Elimina borde de foco
            highlightbackground="#F5F5DC",  # Color del fondo del borde de foco (por si lo muestra igual)
            highlightcolor="#F5F5DC",
            command=lambda: self.ingresarSeleccion(
                "Confirmar",
                ventana,
            )
        )
        btn_aceptar.pack(side=tk.LEFT, padx=15)

        btn_rechazar = tk.Button(
            btn_frame,
            text="Rechazar",
            width=18,
            font=("Arial", 12, "bold"),
            bg="#DA6363",
            fg="#654321",
            activebackground="#654321",
            activeforeground="#654321",
            relief=tk.FLAT,   # Quita el efecto de relieve
            bd=0,             # Grosor del borde en 0
            highlightthickness=0,  # Elimina borde de foco
            highlightbackground="#F5F5DC",  # Color del fondo del borde de foco (por si lo muestra igual)
            highlightcolor="#F5F5DC",
            command=lambda: self.ingresarSeleccion(
                "Rechazar",
                ventana,
            )
        )
        btn_rechazar.pack(side=tk.LEFT, padx=15)

        btn_derivar = tk.Button(
            btn_frame,
            text="Solicitar revisión a experto",
            width=18,
            font=("Arial", 12, "bold"),
            bg="#2DB6DC",
            fg="#654321",
            activebackground="#654321",
            activeforeground="#654321",
            relief=tk.FLAT,   # Quita el efecto de relieve
            bd=0,             # Grosor del borde en 0
            highlightthickness=0,  # Elimina borde de foco
            highlightbackground="#F5F5DC",  # Color del fondo del borde de foco (por si lo muestra igual)
            highlightcolor="#F5F5DC",
            command=lambda: self.ingresarSeleccion(
                "derivar",
                ventana,
            )
        )
        btn_derivar.pack(side=tk.LEFT, padx=15)


    def ingresarSeleccion(self, opcion, ventana):
        self.gestor.tomarSeleccion(opcion)
        ventana.destroy()
        self.gestor.buscarEventosAutoDetectados()


    #Método añadido para mostrar todos los eventos(con todos sus datos) y verificar la funcionalidad del código
    def mostrar_lista_eventos(self):
        eventos = self.gestor.getTodosLosEventos()
        texto = ""
        if not eventos:
            texto = "No hay eventos registrados"
        else:
            for i, e in enumerate(eventos, start=1):
                texto += (
                    f"{i}. Fecha Inicio: {e['fechaHoraOcurrencia']}\n"
                    f"   Fecha fin: {e['fechaHoraFin']}\n"
                    f"   Epicentro: ({e['latitudEpicentro']}, {e['longitudEpicentro']})\n"
                    f"   Hipocentro: ({e['latitudHipocentro']}, {e['longitudHipocentro']})\n"
                    f"   Magnitud: {e['valorMagnitud']}\n"
                    f"   Estado Actual: {str(e['estado'])}\n"
                    f"   Alcance Sismo: {e.get('alcanceSismo', '-')}\n"
                    f"   Origen Sismo: {e.get('origenSismo', '-')}\n"
                    f"   Clasificación: {e.get('clasificacion', '-')}\n"
                    f"   Analista supervisor: {e.get('analistaSupervisor', '-')}\n"
                    f"   Estado anterior: {e.get('ultimoEstado', '-')}\n\n"
                )

        # Crear ventana nueva
        ventana = tk.Toplevel(self.root)
        ventana.title("Listado de Eventos Sísmicos")
        ventana.geometry("700x500")

        frame = tk.Frame(ventana)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")

        text_area = tk.Text(frame, wrap="word", yscrollcommand=scrollbar.set, font=("Arial", 11))
        text_area.pack(side="left", fill="both", expand=True)

        scrollbar.config(command=text_area.yview)

        text_area.insert("end", texto)
        text_area.config(state="disabled")