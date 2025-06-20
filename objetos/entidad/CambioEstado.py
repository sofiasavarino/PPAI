class CambioEstado:
    def __init__(self, fechaHoraInicio, fechaHoraFin, estado):
        #Atributos Propios:
        self.fechaHoraInicio = fechaHoraInicio
        self.fechaHoraFin = fechaHoraFin

        #Relaciones con otras clases:
        self.estado = estado
        self.responsableInspeccion = None

    def esUltimo(self):
        if self.fechaHoraFin is None or self.fechaHoraFin == "":
            return True
    
    def setFechaHoraFin(self, fecha):
        self.fechaHoraFin = fecha
        