from tkinter import messagebox
from datetime import datetime

class GestorRegistrarResultado:
    def __init__(self,sesion,lista_sismografos,lista_empleados, lista_eventos,lista_estados, pantalla):
        #Atributos propios:
        self.eventoAutoDetectado = None
        self.eventoSismicoSeleccionado = None
        self.eventoBloqueadoEnRevision = None
        self.detalleEventoSismico = []
        self.usuarioLogueado = None
        self.eventoRechazado = None
        self.fechaHoraOcurrenciaEvento = None
        self.clasificacionEvento = None

        #agregar al diagrama de clases:
        self.empleadoLogueado = None

        #Relaciones con otras clases:
        self.pantalla = pantalla
        self.eventoSismico = lista_eventos
        self.empleado = lista_empleados
        self.sesion = sesion
        self.estado = lista_estados

        #Otros atributos
        #self.lista_eventos = l
        #self.lista_estados = lista_estados
       # self.lista_empleados = lista_empleados
        self.lista_sismografos = lista_sismografos
        self.accionSeleccionada = None
        

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
        print("eventoAutoDetectado:", eventoAutoDetectado)
        eventoAutoDetectado.sort(key=lambda x: x["fechaHoraOcurrencia"])

           
    def seleccionarEvento(self, evento_sismico):
        self.eventoSismicoSeleccionado = evento_sismico
        print(self.eventoSismicoSeleccionado)

        self.buscarEstadoBloqueados(self.estado)
        # llamados al resto de funciones
        self.buscarEmpleadoLogueado()
        self.fechaHoraOcurrenciaEvento = self.obtenerFechaHora()
        self.bloquearEvento(self.eventoSismicoSeleccionado, self.fechaHoraOcurrenciaEvento)
        self.buscarDatosSismicosRegistrados()

        #print( f"nombreSismo: {nombreSismo}\nclasificacionSismo: {clasificacionSismo}\norigenSismo: {origenSismo}\nseries: {series}\n\n")

        #self.clasificarPorEstacion(series)
        self.llamarCasoDeUsoGenerarSismograma()
        #self.habilitarOpcionSismico()


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
                print(f"Empleado \n Nombre: {self.empleadoLogueado.nombre} \n Apellido: {self.empleadoLogueado.apellido}")                #messagebox.showinfo("Empleado encontrado", f"Empleado \n Nombre: {empleado.nombre} \n Apellido: {empleado.apellido}")
                break
        else:
            print("no se encontro el empleado")
            #messagebox.showinfo("Empleado no encontrado", "No se encontró el empleado logueado")


    def obtenerFechaHora(self):
        fechaHoraOcurrenciaEvento =  datetime.now()
        return fechaHoraOcurrenciaEvento
    
        
    def bloquearEvento(self, eventoSismicoSeleccionado, fechaHoraOcurenciaEvento):
        if eventoSismicoSeleccionado:
            self.eventoBloqueadoEnRevision = eventoSismicoSeleccionado.bloquear(self.estado_bloqueado, self.fechaHoraOcurrenciaEvento)
            print("EVENTO BLOQUEADO:",self.eventoBloqueadoEnRevision)
        else:
            messagebox.showinfo("No hay evento sísmico seleccionado para bloquear")

    
    def buscarDatosSismicosRegistrados(self):
        print("VA a funcion  buscar datos sismicos")
        self.detalleEventoSismico = self.eventoSismicoSeleccionado.buscarDatosSismicosRegistrados()
        print(self.detalleEventoSismico)
        self.habilitarOpcionSismico()
        
    

    def clasificarPorEstacion(self, series):
        #este hay que hacerlo
        print("Clasificando por estación sismológica...")
        pass


    def llamarCasoDeUsoGenerarSismograma(self):
        messagebox.showinfo("Llamar caso de uso Generar Sismograma", "llamarCasoDeUsoGenerarSismograma()")


    def habilitarOpcionSismico(self):
        self.pantalla.mostrarDatosEventoSismico(self.detalleEventoSismico)
        #self.pantalla.habilitarOpcionMapaSismico()
        #self.pantalla.habilitarOpcionEstacionSismologica()
        #self.pantalla.solicitarOpcionVisualizarMapa()


    def tomarMapaSismico(self):
        #self.pantalla.habilitarOpcionModificacionDatos()
        self.pantalla.solicitarOpcionModifiacionDatos()


    def tomarModificacionDatos(self):
        #self.pantalla.habilitarOpciones()
        #self.pantalla.solicitarSeleccionarOpcion()
        print("hola")


    def tomarSeleccion(self, seleccion):
        messagebox.showinfo("Donde Estoy??", f"tomarSeleccion()\nSeleccion: {seleccion}")
        self.accionSeleccionada = seleccion
        self.validarExistencia(seleccion)
        self.buscarEstadoRechazado(self.estado)
        self.buscarEmpleadoLogueado()
        fechaHoraOcurrenciaEvento = self.obtenerFechaHora()
        self.rechazarEvento(self.eventoSismicoSeleccionado, fechaHoraOcurrenciaEvento)
        self.finCU()


    def validarExistencia(self, seleccion):
    # Verifica que el evento y sus atributos clave existan
        if (
            self.eventoSismicoSeleccionado is not None and
            self.eventoSismicoSeleccionado.valorMagnitud is not None and
            self.eventoSismicoSeleccionado.alcanceSismo is not None and
            self.eventoSismicoSeleccionado.origenDeCreacion is not None and
            hasattr(self, 'accionSeleccionada') and
            self.accionSeleccionada is not None
        ):
            return True
        else:
            print("Faltan datos obligatorios del evento o no se seleccionó una acción.")
            return False


    def buscarEstadoRechazado(self, estado):
        for estado in self.estado:
            if estado.esAmbitoEventoSismico() and estado.esRechazado():
                self.estado_rechazado = estado
                print("Estado recha:",self.estado_rechazado)

    def rechazarEvento(self, eventoSismicoSeleccionado, fechaHoraOcurrenciaEvento):
        if eventoSismicoSeleccionado:
            self.eventoRechazado =  eventoSismicoSeleccionado.bloquear(self.estado_rechazado,self.fechaHoraOcurrenciaEvento)
            print("EVENTO RECHAZADO:",self.eventoRechazado)
        else:
            messagebox.showinfo("No hay evento sísmico seleccionado para rechazar")
        


    

    def finCU(self):
        print("Fin del caso de uso")
        messagebox.showinfo("Fin", f"Fin del caso de uso.")

