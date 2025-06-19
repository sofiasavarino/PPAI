class CambioEstado:
    def __init__(self, fechaHoraInicio, fechaHoraFin, estado):
        self.fechaHoraInicio = fechaHoraInicio
        self.fechaHoraFin = fechaHoraFin
        self.estado = estado

    def esUltimo(self):
        if self.fechaHoraFin is None or self.fechaHoraFin == "":
            return True
    
    def setFechaHoraFin(self, fecha):
        self.fechaHoraFin = fecha
        