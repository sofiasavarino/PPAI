class Sismografo:
    def __init__(self, fechaAdquisicion, identificadorSismografo, nroSerie, estacionSismologica):
        self.fechaAdquisicion = fechaAdquisicion
        self.identificadorSismografo = identificadorSismografo
        self.nroSerie = nroSerie

        #Relacion con otras clases
        self.estacionSismologica = estacionSismologica

    def getEstacionSismologica(self):
        print("estoy en get estacion 14")
        return self.estacionSismologica.getCodigoEstacion()

        