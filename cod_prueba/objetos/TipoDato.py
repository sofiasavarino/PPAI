class TipoDato:
    def __init__(self, denominacion, unidadDeMedida, valorUmbral):
        self.denominacion = denominacion
        self.unidadDeMedida = unidadDeMedida
        self.valorUmbral = valorUmbral

    def getDenominacion(self):
        print("saque sednominacion 11")
        return self.denominacion

    def getUnidadDeMedida(self):
        print("saque unidade 12")
        return self.unidadDeMedida

    def getValorUmbral(self):
        print("saque valor 13")
        return self.valorUmbral