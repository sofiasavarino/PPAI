class CambioEstado:
    def __init__(self, fechaHoraInicio, fechaHoraFin, estado, responsableInspeccion):
        #Atributos Propios:
        self.fechaHoraInicio = fechaHoraInicio
        self.fechaHoraFin = fechaHoraFin

        #Relaciones con otras clases:
        self.estado = estado
        self.responsableInspeccion = responsableInspeccion

    def esUltimo(self):
        if self.fechaHoraFin is None or self.fechaHoraFin == "":
            return True
    
    def setFechaHoraFin(self, fecha):
        self.fechaHoraFin = fecha


    #Métodos añadidios para mostar listado de eventos
    def getNombreEstado(self):
        return self.estado.getNombre()
        
    def getFecha(self):
        return self.fechaHoraFin
    
    def getResponsable(self):
        if self.responsableInspeccion is not None:
            return self.responsableInspeccion.getNombre()
        return None
    
    def getFechaHoraInicio(self):
        return self.fechaHoraInicio