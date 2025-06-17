class TipoDato:
    def __init__(self, denominacion, unidadDeMedida, valorUmbral):
        self.denominacion = denominacion
        self.unidadDeMedida = unidadDeMedida
        self.valorUmbral = valorUmbral

    def getDenominacion(self):
        return self.denominacion

    def getUnidadDeMedida(self):
        return self.unidadDeMedida

    def getValorUmbral(self):
        return self.valorUmbral