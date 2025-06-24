from tkinter import messagebox
from datetime import datetime

class GestorRegistrarResultado:
    def __init__(self,sesion,lista_empleados, lista_eventos,lista_estados, pantalla):
        #Atributos propios:
        self.eventoAutoDetectado = None
        self.eventoSismicoSeleccionado = None
        self.eventoBloqueadoEnRevision = None
        self.detalleEventoSismico = []
        self.usuarioLogueado = None
        self.eventoRechazado = None
        self.eventoConfirmado = None
        self.fechaHoraOcurrenciaEvento = None
        self.clasificacionEvento = None
        self.empleadoLogueado = None
        self.accionSeleccionada = None

        #Relaciones con otras clases:
        self.pantalla = pantalla
        self.eventoSismico = lista_eventos
        self.empleado = lista_empleados
        self.sesion = sesion
        self.estado = lista_estados
    

    def opcRegistrarResultado(self):
        if self.pantalla:
            self.buscarEventosAutoDetectados()
        else:
            print("No hay pantalla asignada en Gestor")


    def buscarEventosAutoDetectados(self):
        self.eventoAutoDetectado = []
        for evento in self.eventoSismico:
            if evento.sosAutoDetectado():
                datosEvento = evento.obtenerDatos()
                datosEvento["objeto"] = evento
                self.eventoAutoDetectado.append(datosEvento)

        self.ordenarPorFechayHora(self.eventoAutoDetectado)
        self.pantalla.presentarEventos(self.eventoAutoDetectado)
        return self.eventoAutoDetectado


    def ordenarPorFechayHora(self,eventoAutoDetectado):
        return eventoAutoDetectado.sort(key=lambda x: x["fechaHoraOcurrencia"])

           
    def seleccionarEvento(self, evento_sismico):
        self.eventoSismicoSeleccionado = evento_sismico

        self.buscarEstadoBloqueados(self.estado)

        # llamados al resto de funciones
        self.buscarEmpleadoLogueado()
        self.fechaHoraOcurrenciaEvento = self.obtenerFechaHora()
        self.bloquearEvento(self.eventoSismicoSeleccionado)
        self.buscarDatosSismicosRegistrados()
        self.llamarCasoDeUsoGenerarSismograma()


    def buscarEstadoBloqueados(self, estado):
        for estado in self.estado:
            if estado.esAmbitoEventoSismico() and estado.esBloqueado():
                self.estado_bloqueado = estado
                print("Estado bloqueado:", self.estado_bloqueado)


    def buscarEmpleadoLogueado(self):
        self.usuarioLogueado = self.sesion.getNombreUsuario()
        for empleado in self.empleado:
            if empleado.esTuUsuario(self.usuarioLogueado):
                self.empleadoLogueado = empleado
                print(f"Empleado \n Nombre: {self.empleadoLogueado.getNombre()}")
                print(f"Usuario logueado:",self.usuarioLogueado)
                break
        else:
            print("no se encontro el empleado")



    def obtenerFechaHora(self):
        fechaHoraOcurrenciaEvento =  datetime.now()
        return fechaHoraOcurrenciaEvento
    
        
    def bloquearEvento(self, eventoSismicoSeleccionado):
        if eventoSismicoSeleccionado:
            self.eventoBloqueadoEnRevision = eventoSismicoSeleccionado.bloquear(self.estado_bloqueado, self.fechaHoraOcurrenciaEvento,self.empleadoLogueado)
            print("EVENTO BLOQUEADO:",self.eventoBloqueadoEnRevision)
        else:
            messagebox.showinfo("No hay evento sísmico seleccionado para bloquear")

    
    def buscarDatosSismicosRegistrados(self):
        print("VA a funcion  buscar datos sismicos")
        self.detalleEventoSismico = self.eventoSismicoSeleccionado.buscarDatosSismicosRegistrados()
        print(self.detalleEventoSismico)
        detalle_clasificado = self.clasificarPorEstacion(self.detalleEventoSismico)
        self.habilitarOpcionSismico(detalle_clasificado)
        

    def clasificarPorEstacion(self, detalle_evento):
        print("Clasificando por estación sismológica...")
        print("detalle_evento:", detalle_evento)
        alcanceSismo = detalle_evento[0]
        clasificacion = detalle_evento[1]
        origenSismo = detalle_evento[2]
        series = detalle_evento[3]

        #Ordena las series por codigo de estación (su índice es 0)
        series_ordenadas = sorted(series, key=lambda x: x[0])

        return (alcanceSismo, clasificacion, origenSismo, series_ordenadas)


    def llamarCasoDeUsoGenerarSismograma(self):
        messagebox.showinfo("Llamar caso de uso Generar Sismograma", "llamarCasoDeUsoGenerarSismograma()")


    def habilitarOpcionSismico(self,detalle_clasificado):
        self.pantalla.mostrarDatosEventoSismico(detalle_clasificado)


    def tomarMapaSismico(self):
        self.pantalla.habilitarYSolicitarOpcionModifiacionDatos()


    def tomarModificacionDatos(self,rta):
        if rta:
            print("si modifica datos")
        else:
            print("no modifica datos")


    def tomarSeleccion(self, seleccion):
        if not self.validarExistencia(seleccion):
            messagebox.showwarning("Advertencia", "Faltan datos obligatorios del evento o no se seleccionó una acción.")
            return False
        self.buscarEmpleadoLogueado()
        self.fechaHoraOcurrenciaEvento = self.obtenerFechaHora()

        if seleccion == "Rechazar":
            print("se guardo opc rechazar")
            self.buscarEstadoRechazado(self.estado)
            self.rechazarEvento(self.eventoSismicoSeleccionado)
        elif seleccion == "Confirmar":
            #Alternativa 2: se selecciona confirmar evento
            print("se seleccionó conf")
            self.buscarEstadoConfirmado(self.estado)
            self.confirmarEvento(self.eventoSismicoSeleccionado)
            print("se selecciono confirmar")
        elif seleccion == "derivar":
            print("evento derivado")

        self.finCU()
        return True


    def validarExistencia(self, seleccion):
        self.accionSeleccionada = seleccion

        if (
            self.eventoSismicoSeleccionado is not None and
            self.eventoSismicoSeleccionado.valorMagnitud not in [None, ""] and
            self.eventoSismicoSeleccionado.alcanceSismo.getNombre().strip() != "" and
            self.eventoSismicoSeleccionado.origenDeCreacion.getNombre().strip() != "" and
            self.eventoSismicoSeleccionado.clasificacion.getNombre().strip() !="" and
            self.accionSeleccionada not in [None, ""]
        ):
            return True
        else:
            print("❌ FALTAN DATOS OBLIGATORIOS")
            return False



    def buscarEstadoRechazado(self,estado):
        for estado in self.estado:
            if estado.esAmbitoEventoSismico() and estado.esRechazado():
                self.estado_rechazado = estado
                print("Estado recha:",self.estado_rechazado)


    def rechazarEvento(self, eventoSismicoSeleccionado):
        if eventoSismicoSeleccionado:
            self.eventoRechazado =  eventoSismicoSeleccionado.rechazar(self.estado_rechazado, self.fechaHoraOcurrenciaEvento,self.empleadoLogueado)
            print("EVENTO RECHAZADO:",self.eventoRechazado)
        else:
            messagebox.showinfo("No hay evento sísmico seleccionado para rechazar")
        

    def finCU(self):
        print("Fin del caso de uso")
        messagebox.showinfo("Fin", f"Fin del caso de uso.")


    #Métodos por alternativa 2: se selecciona confirmar evento
    def buscarEstadoConfirmado(self,estado):
        print("buscando estado confirmdo")
        for estado in self.estado:
            if estado.esAmbitoEventoSismico() and estado.esConfirmado():
                self.estado_confirmado = estado
    

    def confirmarEvento(self,eventoSismicoSeleccionado):
        print("por confirmar evento)")
        if eventoSismicoSeleccionado:
            self.eventoConfirmado =  eventoSismicoSeleccionado.confirmar(self.estado_confirmado, self.fechaHoraOcurrenciaEvento,self.empleadoLogueado)
        else:
            messagebox.showinfo("No hay evento sísmico seleccionado para confirmar")


    #Método añadido por alternativa 1: modificar datos
    def actualizarDatosEvento(self, alcance, clasificacion, origen):
        self.eventoSismicoSeleccionado.actualizarDatos(alcance, clasificacion, origen)
        print("Datos del evento actualizados desde botón 'Guardar'")


    #Método añadido para listar todos los eventos y comprobar funcionalidad de código
    def getTodosLosEventos(self):
        lista_eventos = []
        for evento in self.eventoSismico:
            datosEvento = evento.datosEventos()
            lista_eventos.append(datosEvento)
        
        return lista_eventos