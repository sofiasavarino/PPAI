from CambioEstado import CambioEstado
class EventoSismico:
    def __init__(self,lista_Series_temporales,fechaHoraFin,fechaHoraOcurrencia,latitudEpicentro,latitudHipocentro,longitudEpicentro,longitudHipocentro,valorMagnitud, cambioEstado, estado, serieTemporal, origenSismo, clasificacionSismo, alcanceSismo, empleado):
        self.lista_Series_temporales = lista_Series_temporales
        self.fechaHoraFin = fechaHoraFin
        self.fechaHoraOcurrencia = fechaHoraOcurrencia 
        self.longitudEpicentro = longitudEpicentro
        self.valorMagnitud = valorMagnitud
        self.latitudHipocentro = latitudHipocentro
        self.longitudHipocentro = longitudHipocentro
        self.cambioEstado = cambioEstado
        self.estado = estado
        self.serieTemporal = serieTemporal
        self.origenSismo = origenSismo
        self.clasificacionSismo = clasificacionSismo
        self.alcanceSismo = alcanceSismo
        self.empleado = empleado
        self.latitudEpicentro = latitudEpicentro
    
    def sosAutoDetectado(self):
        return self.estado.esAutoDetectado()

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

    def obtenerDatos(self):
        return {
        "fechaHoraOcurrencia": self.getFechaHoraOcurrencia(),
        "latitudEpicentro": self.getLatitudEpicentro(),
        "longitudEpicentro": self.getLongitudEpicentro(),
        "latitudHipocentro": self.getLatitudHipocentro(),
        "longitudHipocentro": self.getLongitudHipocentro(),
        "valorMagnitud": self.getValorMagnitud()
    }

    def getDatos(self):
        print("estoy en get datos de eventos 3")
        nombreSismo = self.alcanceSismo.getNombre()
        clasificacionSismo = self.clasificacionSismo.getNombre()
        origenSismo = self.origenSismo.getNombre()
        series = self.buscarDatosSeriesTemporales()
        return nombreSismo, clasificacionSismo, origenSismo, series

    # def bloquear(self):
    #     self.buscarCambioEstadoEvento()}
    def bloquear(self, estado_bloqueado,fechaHora):
    # Crear un nuevo cambio de estado y asociarlo
        

        # self.cambioEstado.append(nuevo_cambio)
        # self.estado = estado_bloqueado
        # nuevo_cambio = self.buscarCambioEstadoEvento(estado_bloqueado,fechaHora)
        self.estado = estado_bloqueado
        self.cambioEstado = self.buscarCambioEstadoEvento(fechaHora)

    def buscarCambioEstadoEvento(self, fechaHora):
        for cambio in self.cambioEstado:
            if cambio.esUltimo(cambio):
                cambio.setFechaHoraFin(fechaHora)
        
        self.crearCambioEstado(self.estado,self.cambioEstado, fechaHora)

    def crearCambioEstado(self, estado, cambioEstado, fechaHora):
        nuevo_cambio = CambioEstado(
            fechaHoraInicio=fechaHora,
            fechaHoraFin=None,
            estado= estado,
            lista_estado= cambioEstado 
        )
        self.cambioEstado.append(nuevo_cambio)
        print("Cambio hecho")
        
        

    def buscarDatosSismicosRegistrados(self):
        print("estoy en buscar datos sismicos registrados de evento 2")
        return self.getDatos()
       
        # for sismografoo in lista_sismografos:
        #     self.getDatos(sismografoo)
        #     print(f"Datos del sismógrafo {self.getDatos(sismografoo)}:")
        #self.buscarDatosSeriesTemporales(self.lista_Series_temporales)


    def buscarDatosSeriesTemporales(self):
        print("estoy en buscar series temporales 7")
        series = []
        for serie in self.lista_Series_temporales:
            series.append(serie.getSerieTemporal())
        return series

    
    def rechazar(self):
        self.buscarCambioEstadoEvento()
