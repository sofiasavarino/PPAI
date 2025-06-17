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

class Gestor:
    def __init__(self, lista_eventos, pantalla=None):
        # Guardar la lista completa de eventos (auto detectados o no)
        self.lista_eventos = lista_eventos
        self.eventoSismicoSeleccionado = None
        self.pantalla = pantalla
        # Otros atributos inicializados en None o valores por defecto
        self.eventoBloqueadoEnRevision = None
        self.detalleEventoSismico = None
        self.usuarioLogueado = None
        self.eventoRechazado = None
        self.fechaHoraOcurrenciaEvento = None
        self.clasificacionEvento = None
        self.eventoSismico = None
        self.estado = None
        self.empleado = None
        self.sesion = None
        self.accionSeleccionada = None

    def opcRegistrarResultado(self):
        # if self.pantalla:
        #     self.pantalla.opcionRegistrarResultado()
        #     print("Registrar resultado manual")
        # else:
        #     print("No hay pantalla asignada en Gestor")
        if self.pantalla:
            self.buscarEventosAutoDetectados()
        else:
            print("No hay pantalla asignada en Gestor")

    def buscarEventosAutoDetectados(self):
        eventos_auto_detectados = []
        for evento in self.lista_eventos:
            if evento.sosAutoDetectado():
                datosEvento = evento.obtenerDatos()
                eventos_auto_detectados.append(datosEvento)
        self.pantalla.presentarEventos(eventos_auto_detectados)
        return eventos_auto_detectados

    def ordenarPorFechayHora(self, eventos_auto_detectados):
        eventos_auto_detectados.sort(key=lambda x: x["fechaHoraOcurrencia"])
        return eventos_auto_detectados
    
    def bloquearEvento(self):
        if self.eventoSismicoSeleccionado:
            self.eventoSismicoSeleccionado.bloquear()
            print("Evento sísmico bloqueado")
        else:
            print("No hay evento sísmico seleccionado para bloquear")

    def registrarRechazo(self):
        if self.eventoSismicoSeleccionado:
            self.eventoSismicoSeleccionado.rechazar()
            print("Evento rechazado")
        else:
            print("No hay evento seleccionado para rechazar")

    def finCU(self):
        print("Fin del caso de uso")
