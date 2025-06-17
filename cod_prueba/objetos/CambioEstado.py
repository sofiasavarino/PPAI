class CambioEstado:
    def __init__(self, fechaHoraInicio, fechaHoraFin, estado):
        self.fechaHoraInicio = fechaHoraInicio
        self.fechaHoraFin = fechaHoraFin
        self.estado = estado

    def esUltimo(self, listaEstados):
        for estado in listaEstados:
            if estado.fechaHoraFin is None or estado.fechaHoraFin > self.fechaHoraFin:
                return True
    
    def setFechaHoraFin(self):
        from datetime import datetime
        self.fechaHoraFin = datetime.now()
        