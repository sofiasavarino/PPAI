from entidad.CambioEstado import CambioEstado
class EventoSismico:
    def __init__(self,lista_Series_temporales,fechaHoraFin,fechaHoraOcurrencia,latitudEpicentro,latitudHipocentro,longitudEpicentro,longitudHipocentro,valorMagnitud, cambioEstado, estado, origenSismo, clasificacionSismo, alcanceSismo, empleado, serieTemporal):
        #Atributos Propios:
        self.fechaHoraFin = fechaHoraFin
        self.fechaHoraOcurrencia = fechaHoraOcurrencia
        self.latitudEpicentro = latitudEpicentro
        self.longitudEpicentro = longitudEpicentro
        self.latitudHipocentro = latitudHipocentro
        self.longitudHipocentro = longitudHipocentro
        self.valorMagnitud = valorMagnitud

        #Relaciones con otras clases:
        self.cambioEstado = cambioEstado if cambioEstado is not None else []
        self.estadoActual = estado
        self.analistaSupervisor = empleado
        self.origenDeCreacion = origenSismo
        self.alcanceSismo = alcanceSismo
        self.clasificacion = clasificacionSismo
        self.serieTemporal = lista_Series_temporales

    
    def sosAutoDetectado(self):
        return self.estadoActual.esAutoDetectado()

    def getFechaHoraOcurrencia(self):
        return self.fechaHoraOcurrencia

    def getLatitudEpicentro(self):
        return self.latitudEpicentro

    def getLongitudEpicentro(self):
        return self.longitudEpicentro

    def getLatitudHipocentro(self):
        return self.latitudHipocentro

    def getLongitudHipocentro(self):
        return self.longitudHipocentro

    def getValorMagnitud(self):
        return self.valorMagnitud

    def getEstado(self):
        return self.estadoActual.getNombre()

    def obtenerDatos(self):
        return {
        "fechaHoraOcurrencia": self.getFechaHoraOcurrencia(),
        "latitudEpicentro": self.getLatitudEpicentro(),
        "longitudEpicentro": self.getLongitudEpicentro(),
        "latitudHipocentro": self.getLatitudHipocentro(),
        "longitudHipocentro": self.getLongitudHipocentro(),
        "valorMagnitud": self.getValorMagnitud(),
        }
    

    def getDatos(self):
        print("estoy en get datos de eventos 3")
        nombreSismo = self.alcanceSismo.getNombre()
        clasificacion = self.clasificacion.getNombre()
        origenSismo = self.origenDeCreacion.getNombre()
        series = self.buscarDatosSeriesTemporales()
        return nombreSismo, clasificacion, origenSismo, series


    def bloquear(self, estado_bloqueado, fechaHora,empleadoLog):
        self.estadoActual = estado_bloqueado
        self.buscarCambioEstadoEvento(fechaHora,empleadoLog)
        return self

    def rechazar(self, estado_rechazado, fechaHora,empleadoLog):
        self.estadoActual = estado_rechazado
        self.buscarCambioEstadoEvento(fechaHora,empleadoLog)
        return self

    def buscarCambioEstadoEvento(self, fechaHora,empleadoLog):
        for cambio in self.cambioEstado:
            if cambio.esUltimo():
                cambio.setFechaHoraFin(fechaHora)
        self.crearCambioEstado(self.estadoActual, fechaHora,empleadoLog)

    def crearCambioEstado(self, estadoActual, fechaHora,empleadoLog):
        nuevo_cambio = CambioEstado(
            fechaHoraInicio=fechaHora,
            fechaHoraFin=None,
            estado = estadoActual,
            responsableInspeccion = empleadoLog
        )
        self.cambioEstado.append(nuevo_cambio)
        print("Cambio hecho")
          
    def buscarDatosSismicosRegistrados(self):
        print("estoy en buscar datos sismicos registrados de evento 2")
        series = []
        series = self.getDatos()
        print(series)
        return series

    def buscarDatosSeriesTemporales(self):
        print("estoy en buscar series temporales 7")
        series = []
        for serie in self.serieTemporal:
            series.append(serie.getSerieTemporal())
        return series


    def getFechaHoraFin(self):
        return self.fechaHoraFin
    

    #Método añadido para alternativa 1: modificar datos   
    def actualizarDatos(self, alcance, clasificacion, origen):
        self.alcanceSismo.setNombre(alcance)
        self.clasificacion.setNombre(clasificacion)
        self.origenDeCreacion.setNombre(origen)

    #Método añadidio por alternativa 2: confirmar evento
    def confirmar(self, estado_confirmado, fechaHora, empleadoLog):
        print("confirmando evento")
        self.estadoActual = estado_confirmado
        self.buscarCambioEstadoEvento(fechaHora, empleadoLog)
        return self

    #Método añadido para listar eventos y comprobar funcionalidad del sistema
    def datosEventos(self):
        datos = {
            "fechaHoraOcurrencia": self.getFechaHoraOcurrencia(),
            "fechaHoraFin": self.getFechaHoraFin(),
            "latitudEpicentro": self.getLatitudEpicentro(),
            "longitudEpicentro": self.getLongitudEpicentro(),
            "latitudHipocentro": self.getLatitudHipocentro(),
            "longitudHipocentro": self.getLongitudHipocentro(),
            "valorMagnitud": self.getValorMagnitud(),
            "estado": self.getEstado(),
            "alcanceSismo": self.alcanceSismo.getNombre() ,
            "origenSismo": self.origenDeCreacion.getNombre(),
            "clasificacion": self.clasificacion.getNombre(),
        }
        
        
        if self.cambioEstado:
            estado_anterior = max(
                (cambio for cambio in self.cambioEstado if cambio.getFecha() is not None),
                key=lambda cambio: cambio.getFecha(),
                default=None)
            for cambio in self.cambioEstado:
                if cambio.esUltimo():
                    datos["cambioEstadoFechaHora"] = cambio.getFechaHoraInicio()
                    responsable = cambio.getResponsable()
                    if responsable is not None:
                        datos["cambioEstadoResponsable"] = responsable
                    else:
                        datos["cambioEstadoResponsable"] = "No se encontró responsable"
                    datos['fechaHoraFin'] = cambio.getFecha()

        datos["ultimoEstado"] = estado_anterior.getNombreEstado() if estado_anterior else "No tiene"
        return datos
    
            
        