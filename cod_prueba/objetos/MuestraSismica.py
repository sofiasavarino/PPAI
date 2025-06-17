class MuestraSismica:
    def __init__(self,fechaHoraMuestra, detalleMuestra):
        self.fechaHoraMuestra = fechaHoraMuestra
        self.detalleMuestra = detalleMuestra

    def getDatos(self):
        pass
        
    def getDetalle(self):
        for detalle in self.detalleMuestra:
            return detalle.getDatos()