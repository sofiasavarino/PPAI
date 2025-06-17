class EstacionSismologica:
    def __init__(self, codigoEstacion, documentoCertificacionAdq, fechaSolicitudCertificacion, nombre, latitud, longitud, nroCertificacionAdquisicion):
        self.codigoEstacion = codigoEstacion
        self.documentoCertificacionAdq = documentoCertificacionAdq
        self.fechaSolicitudCertificacion = fechaSolicitudCertificacion
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.nroCertificacionAdquisicion = nroCertificacionAdquisicion

    def getCodigoEstacion(self):
        return self.codigoEstacion
