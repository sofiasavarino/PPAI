class MuestraSismica:
    def __init__(self,fechaHoraMuestra, lista_detalleMuestra):
        self.fechaHoraMuestra = fechaHoraMuestra
        self.detalleMuestra = lista_detalleMuestra

    def getDatos(self):
        return self.getDetalle()
        
    def getDetalle(self):
        print("estoy en a metodo get datos y a get detalle 9 ")
        for detalle in self.detalleMuestra:
            return detalle.getDatos()