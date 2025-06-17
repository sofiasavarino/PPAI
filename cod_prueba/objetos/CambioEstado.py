class CambioEstado:
    def __init__(self, fechaHoraInicio, fechaHoraFin, estado, lista_estado):
        self.fechaHoraInicio = fechaHoraInicio
        self.fechaHoraFin = fechaHoraFin
        self.estado = estado
        self.lista_estado = lista_estado

    def esUltimo(self):
        for estado in self.lista_estado:
            if estado.fechaHoraFin is None or estado.fechaHoraFin > self.fechaHoraFin:
                return True
    
    def setFechaHoraFin(self):
        from datetime import datetime
        self.fechaHoraFin = datetime.now()
        