class SerieTemporal:
    def __init__(self, condicionAlarma,fechaHoraInicioRegistroMuestras,fechaHoraRegistro,frecuenciaMuestreo,muestraSismica, sismografo, lista_muestras_sismicas):
        #Atributos Propios:
        self.condicionAlarma = condicionAlarma
        self.fechaHoraInicioRegistroMuestras = fechaHoraInicioRegistroMuestras
        self.fechaHoraRegistro = fechaHoraRegistro
        self.frecuenciaMuestreo = frecuenciaMuestreo

        #Relaciones con otras clases:
        self.muestraSismica = muestraSismica
        self.sismografo = sismografo

        #esta deberia ser solo muestras sismicas, y eos deberia ser la lista
        self.lista_muestras_sismicas = lista_muestras_sismicas

    def getSerieTemporal(self):
        print("estoy en getSerieTemporal 8 ")
        series = []
        for muestra in self.lista_muestras_sismicas:
            series.append(muestra.getDatos())
        
        print("AHora deberia retorna estacion sismologia de sismohgrafo")
        return self.sismografo.getEstacionSismologica(), series
