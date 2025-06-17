class DetalleMuestra:
    def __init__(self,valor, tipoDato):
        self.valor = valor
        self.tipoDato = tipoDato

    def getDatos(self):
        for dato in self.tipoDato:
            return{
                "denominacion": tipoDato.getDenominacion(),
                "unidad": tipoDato.getUnidad(),
                "valor": tipoDato.getValor()
            }
        