class SerieTemporal:
    def __init__(self, condicionAlarma,fechaHoraInicioRegistroMuestras,fechaHoraRegistro,frecuenciaMuestreo, sismografo, lista_muestras_sismicas):
        #Atributos Propios:
        self.condicionAlarma = condicionAlarma
        self.fechaHoraInicioRegistroMuestras = fechaHoraInicioRegistroMuestras
        self.fechaHoraRegistro = fechaHoraRegistro
        self.frecuenciaMuestreo = frecuenciaMuestreo

        #Relaciones con otras clases:
        self.muestraSismica = lista_muestras_sismicas
        self.sismografo = sismografo
       

    def getSerieTemporal(self):
        print("estoy en getSerieTemporal 8 ")
        series = []
        for muestra in self.muestraSismica:
            series.append(muestra.getDatos())
        
        print("AHora deberia retorna estacion sismologia de sismohgrafo")
        return self.sismografo.getEstacionSismologica(), series
