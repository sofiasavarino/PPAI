from tkinter import messagebox
from datetime import datetime
class Gestor:
    def __init__(self,sesion,lista_sismografos,lista_empleados, lista_eventos,lista_estados, pantalla=None, estado = None):
        # Guardar la lista completa de eventos (auto detectados o no)
        self.lista_eventos = lista_eventos
        self.eventoSismicoSeleccionado = None
        self.pantalla = pantalla
        self.lista_estados = lista_estados
        self.lista_empleados = lista_empleados
        self.lista_sismografos = lista_sismografos
        # Otros atributos inicializados en None o valores por defecto
        self.eventoBloqueadoEnRevision = None
        self.detalleEventoSismico = None
        self.usuarioLogueado = None
        self.eventoRechazado = None
        self.fechaHoraOcurrenciaEvento = None
        self.clasificacionEvento = None
        self.eventoSismico = None
        self.estado = estado
        self.empleado = None
        self.sesion = sesion
        self.accionSeleccionada = None
        
    def opcRegistrarResultado(self):
        if self.pantalla:
            self.buscarEventosAutoDetectados()
        else:
            print("No hay pantalla asignada en Gestor")

    def buscarEventosAutoDetectados(self):
        eventos_auto_detectados = []
        for evento in self.lista_eventos:
            if evento.sosAutoDetectado():
                datosEvento = evento.obtenerDatos()
                datosEvento["objeto"] = evento
                eventos_auto_detectados.append(datosEvento)
        self.ordenarPorFechayHora(eventos_auto_detectados)
        self.pantalla.presentarEventos(eventos_auto_detectados)

    def ordenarPorFechayHora(self, eventos_auto_detectados):
        eventos_auto_detectados.sort(key=lambda x: x["fechaHoraOcurrencia"])
           
    def seleccionarEvento(self, evento_sismico):
        self.eventoSismicoSeleccionado = evento_sismico
        print(self.eventoSismicoSeleccionado)

        self.buscarEstadoBloqueados(self.lista_estados)
        # llamados al resto de funciones
        self.buscarEmpleadoLogueado()
        fechaHora = self.obtenerFechaHora()
        self.bloquearEvento(self.eventoSismicoSeleccionado, fechaHora)
        nombreSismo, clasificacionSismo, origenSismo, series = self.buscarDatosSismicosRegistrados()

        print( f"nombreSismo: {nombreSismo}\nclasificacionSismo: {clasificacionSismo}\norigenSismo: {origenSismo}\nseries: {series}\n\n")

        self.clasificarPorEstacion(series)
        self.llamarCasoDeUsoGenerarSismograma()
        self.habilitarOpcionSismico()



    def buscarEstadoBloqueados(self, lista_estados):
        for estado in lista_estados:
            if estado.esAmbitoEventoSismico() and estado.esBloqueado():
                self.eventoBloqueadoEnRevision = estado


    def buscarEmpleadoLogueado(self):
        self.usuarioLogueado = self.sesion.getNombreUsuario()

        for empleado in self.lista_empleados:
            if empleado.esTuUsuario(self.usuarioLogueado):
                self.empleado = empleado
                messagebox.showinfo("Empleado encontrado", f"Empleado \n Nombre: {empleado.nombre} \n Apellido: {empleado.apellido}")
                break
        else:
            messagebox.showinfo("Empleado no encontrado", "No se encontró el empleado logueado")

        # self.obtenerFechaHora()

    def obtenerFechaHora(self):
        fechaHora=  datetime.now()
        return fechaHora
        #ESTO NO ESTARIA BIEN
        # self.bloquearEvento(self.eventoSismicoSeleccionado, fechaHora)

    def bloquearEvento(self, eventoSismicoSeleccionado, fechaHora):
        if eventoSismicoSeleccionado:
            estado_bloqueado = self.eventoBloqueadoEnRevision
            eventoSismicoSeleccionado.bloquear(estado_bloqueado,fechaHora)
            # messagebox.showinfo("Evento sísmico bloqueado", f"Evento bloqueado en: {fechaHora}")
        else:
            messagebox.showinfo("No hay evento sísmico seleccionado para bloquear")

        # self.buscarDatosSismicosRegistrados()
    
    def buscarDatosSismicosRegistrados(self):
        print("VA a funcion  buscar datos sismicos")
        #self.clasificarPorEstacion(lista_sismografos)
        return self.eventoSismicoSeleccionado.buscarDatosSismicosRegistrados()

    def clasificarPorEstacion(self, series):
        #este hay que hacerlo
        print("Clasificando por estación sismológica...")
        pass

    def llamarCasoDeUsoGenerarSismograma(self):
        messagebox.showinfo("Llamar caso de uso Generar Sismograma", "llamarCasoDeUsoGenerarSismograma()")

    def habilitarOpcionSismico(self):
        self.pantalla.habilitarOpcionMapaSismico()
        self.pantalla.habilitarOpcionEstacionSismologica()
        self.pantalla.solicitarOpcionVisualizarMapa()

    def tomarMapaSismico(self):
        self.pantalla.habilitarOpcionModificacionDatos()
        self.pantalla.solicitarOpcionModifiacionDatos()

    def tomarModificacionDatos(self):
        self.pantalla.habilitarOpciones()
        self.pantalla.solicitarSeleccionarOpcion()

    def tomarSeleccion(self, seleccion):
        messagebox.showinfo("Donde Estoy??", f"tomarSeleccion()\nSeleccion: {seleccion}")
        self.accionSeleccionada = seleccion
        self.validarExistencia(seleccion=seleccion)
        self.buscarEstadoRechazado(self.lista_estados)
        self.buscarEmpleadoLogueado()
        fecha = self.obtenerFechaHora()
        self.rechazarEvento(self.eventoSismicoSeleccionado, fecha)
        self.finCU()



    def validarExistencia(self, seleccion):
        
    # Verifica que el evento y sus atributos clave existan
        if (
            self.eventoSismicoSeleccionado is not None and
            self.eventoSismicoSeleccionado.valorMagnitud is not None and
            self.eventoSismicoSeleccionado.alcanceSismo is not None and
            self.eventoSismicoSeleccionado.origenSismo is not None and
            hasattr(self, 'accionSeleccionada') and
            self.accionSeleccionada is not None
        ):
            return True
        else:
            print("Faltan datos obligatorios del evento o no se seleccionó una acción.")
            return False

    def buscarEstadoRechazado(self, lista_estados):
        estados_rechazados = None
        for estado in lista_estados:
            if estado.esAmbitoEventoSismico() and estado.esRechazado():
                estados_rechazados = estado
        return estados_rechazados


    def rechazarEvento(self, eventoSismicoSeleccionado, fechaHora):
        if eventoSismicoSeleccionado:
            estado_rechazado = self.eventoRechazado
            eventoSismicoSeleccionado.rechazar(estado_rechazado, fechaHora)
        else:
            messagebox.showinfo("No hay evento sísmico seleccionado para rechazar")
        

    def finCU(self):
        print("Fin del caso de uso")
        messagebox.showinfo("Fin", f"Fin del caso de uso.")

