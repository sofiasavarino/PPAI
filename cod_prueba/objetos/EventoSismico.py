from CambioEstado import CambioEstado
from datetime import datetime

class EventoSismico:
    def __init__(self, fechaHoraFin,fechaHoraOcurrencia,latitudEpicentro,latitudHipocentro,longitudEpicentro,longitudHipocentro,valorMagnitud, cambioEstado, estado, serieTemporal, origenSismo, clasificacionSismo, alcanceSismo, empleado):
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
        nombreSismo = self.alcanceSismo.getNombre()
        clasificacionSismo = self.clasificacionSismo.getNombre()
        origenSismo = self.origenSismo.getNombre()
        return nombreSismo, clasificacionSismo, origenSismo

    def bloquear(self):
        self.eventoSismicoSeleccionado.buscarCambioEstadoEvento()
    
    def buscarCambioEstadoEvento(self, lista_cambio_estado):
        for cambio in lista_cambio_estado:
            if cambio.esUltimo(cambio):
                cambio.setFechaHoraFin()
        self.eventoSismicoSeleccionado.crearCambioEstado(self.estado)
                
    def crearCambioEstado(self, estado):
        nuevo_cambio = CambioEstado(
            fechaHoraInicio=datetime.now(),
            fechaHoraFin=None,
            estado= self.estado
        )
        self.cambioEstado.append(nuevo_cambio)
        return nuevo_cambio

    def buscarDatosSismicosRegistrados(self, lista_sismografos):
        for sismografo in lista_sismografos:
            sismografo.getDatos(self)

    def buscarDatosSeriesTemporales(self, lista_series_temporales):
        series = []
        for serie in lista_series_temporales:
            series.append(serie.getSerieTemporal(self))
        return series

    
    def rechazar(self):
        self.eventoSismicoSeleccionado.buscarCambioEstadoEvento()
