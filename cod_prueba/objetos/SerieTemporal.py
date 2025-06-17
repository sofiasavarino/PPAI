class SerieTemporal:
    def __init__(self, condicionAlarma,fechaHoraInicioRegistroMuestras,fechaHoraRegistro,frecuenciaMuestreo,muestraSismica, sismografo):
        self.condicionAlarma = condicionAlarma
        self.fechaHoraInicioRegistroMuestras = fechaHoraInicioRegistroMuestras
        self.fechaHoraRegistro = fechaHoraRegistro
        self.frecuenciaMuestreo = frecuenciaMuestreo
        self.muestraSismica = muestraSismica
        self.sismografo = sismografo

    def getSerieTemporal(self, lista_muestras_sismicas):
        series = []
        for muestra in lista_muestas_sismicas:
            series.append(muestra.getDatos())

        return self.sismografo.getEstacionSismologica(), series
