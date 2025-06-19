# class Gestor:
#     def __init__(self, eventos_auto_detectado, eventoSismicoSeleccionado, eventoBloqueadoEnRevision, detalleEventoSismico, usuarioLogueado, eventoRechazado, fechaHoraOcurrenciaEvento, clasificacionEvento,eventoSismico, estado, empleado, sesion, pantalla):
#         self.eventos_auto_detectado = eventos_auto_detectado
#         self.eventoSismicoSeleccionado = eventoSismicoSeleccionado
#         self.eventoBloqueadoEnRevision = eventoBloqueadoEnRevision
#         self.detalleEventoSismico = detalleEventoSismico
#         self.usuarioLogueado = usuarioLogueado
#         self.eventoRechazado = eventoRechazado
#         self.fechaHoraOcurrenciaEvento = fechaHoraOcurrenciaEvento
#         self.clasificacionEvento = clasificacionEvento
#         self.eventoSismico = eventoSismico
#         self.estado = estado
#         self.empleado = empleado
#         self.sesion = sesion
#         self.pantalla = pantalla

#     def opcRegistrarResultado(self):
#         self.pantalla.opcionRegistrarResultado()
#         print("Registrar resultado manual")


#     def buscarEventosAutoDetectados(self, lista_eventos):
#         eventos_auto_detectados = []
#         for evento in lista_eventos:
#             if evento.sosAutoDetectado():
#                 datosEvento = evento.obtenerDatos()
#                 eventos_auto_detectados.append(datosEvento)
#         return eventos_auto_detectados

#     def ordenarPorFechayHora(self, eventos_auto_detectados):
#         eventos_auto_detectados.sort(key=lambda x: x["fechaHoraOcurrencia"])
#         return eventos_auto_detectados

#     def tomarSeleccionarEvento(self,eventos_auto_detectados):
#         eventoSismicoSeleccionado = self.pantalla.opcSeleccionarEvento(eventos_auto_detectados)
#         return eventoSismicoSeleccionado

#     def buscarEstadoBloqueados(self, lista_estados):
#         #aca no se bien si es de los estados en general o de los eventos auto detectados(su estado)
#         estados_bloqueados = []
#         for estado in lista_estados:
#             if estado.esAmbitoEventoSismico() and estado.esBloqueado():
#                 estados_bloqueados.append(estado)
#         return estados_bloqueados

#     def buscarEmpleadoLogueado(self):
#         return self.sesion.getEmpleado()

#     def obtenerFechaHora(self):
#         return datetime.now()

#     def bloquearEvento(self):
#         if self.eventoSismicoSeleccionado:
#             self.eventoSismicoSeleccionado.bloquear()
#             return print("Evento sismico bloqueado")
#         else:
#             return print("No hay evento sismico seleccionado para bloquear")

#     def buscarDatosSismicosRegistrados(self, lista_sismografos):
#         return self.eventoSismicoSeleccionado.buscarDatosSismicosRegistrados(lista_sismografos)

#     def clasificarPorEstacion(self, series):
#         #este hay que hacerlo
#         pass

#     def llamarCasoDeUsoGenerarSismograma(self):
#         return print("Llamar caso de uso Generar Sismograma")

#     def habilitarMapaSismico(self):
#         self.pantalla.habilitarOpcionMapaSismico()
#         self.pantalla.solicitarOpcionVisualizarMapa()
#         self.pantalla.habilitarOpcionEstacionSismologicas()

#     def tomarMapaSismico(self):
#         opcion = pantalla.opcMapaSismico()
#         pantalla.habilitarOpcionModificacionDatos()
#         pantalla.solicitarOpcionModifiacionDatos()

#     def tomarModificacionDatos(self):
#         opcion_modificacion = pantalla.opcModificacionDatos()
#         pantalla.habilitarOpciones()
#         pantalla.solicitarSeleccionarOpcion()

#     def tomarSeleccion(self):
#         seleccion = pantalla.ingresarSeleccion()

#     def validarExistencia(self, seleccion):
#         evento = seleccion
#     # Verifica que el evento y sus atributos clave existan
#         if (
#             evento is not None and
#             evento.valorMagnitud is not None and
#             evento.alcanceSismo is not None and
#             evento.origenSismo is not None and
#             hasattr(self, 'accionSeleccionada') and
#             self.accionSeleccionada is not None
#         ):
#             return True
#         else:
#             print("Faltan datos obligatorios del evento o no se seleccionó una acción.")
#             return False

#     def buscarEstadoRechazado(self, lista_estados):
#         estados_rechazados = []
#         for estado in lista_estados:
#             if estado.esAmbitoEventoSismico() and estado.esRechazado():
#                 estados_rechazados.append(estado)
#         return estados_rechazados

#     def registrarRechazo(self):
#         self.eventoSismicoSeleccionado.rechazar()

#     def finCU(self):
#         return print("Fin del caso de uso")
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
                # messagebox.showinfo("Empleado encontrado", f"Empleado \n Nombre: {empleado.nombre} \n Apellido: {empleado.apellido}")
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
        self.validarExistencia(seleccion=seleccion)


    def validarExistencia(self, seleccion):
        evento = seleccion
    # Verifica que el evento y sus atributos clave existan
        if (
            evento is not None and
            evento.valorMagnitud is not None and
            evento.alcanceSismo is not None and
            evento.origenSismo is not None and
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


    def registrarRechazo(self):
        if self.eventoSismicoSeleccionado:
            self.eventoSismicoSeleccionado.rechazar()
            print("Evento rechazado")
        else:
            print("No hay evento seleccionado para rechazar")

    def finCU(self):
        print("Fin del caso de uso")
