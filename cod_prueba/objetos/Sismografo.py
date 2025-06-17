class Sismografo:
    def __init__(self, fechaAdquisicion, identificadorSismografo, nroSerie, estacionSismologica):
        self.fechaAdquisicion = fechaAdquisicion
        self.identificadorSismografo = identificadorSismografo
        self.nroSerie = nroSerie
        self.estacionSismologica = estacionSismologica

    def getEstacionSismologica(self):
        return self.estacionSismologica.getCodigoEstacion()

        