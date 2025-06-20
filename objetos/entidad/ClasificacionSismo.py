class ClasificacionSismo:
    def __init__(self, nombre, kmProfundidadDesde,kmProfundidadHasta):
        self.nombre = nombre
        self.kmProfundidadDesde = kmProfundidadDesde
        self.kmProfundidadHasta = kmProfundidadHasta

    def getNombre(self):
        print("saque nombre clasi 5")
        return self.nombre