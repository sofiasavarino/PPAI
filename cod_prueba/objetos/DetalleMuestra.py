class DetalleMuestra:
    def __init__(self,valor, lista_tipoDato):
        self.valor = valor
        self.tipoDato = lista_tipoDato

    def getDatos(self):
        print( "estoy en get datos del detalle 10")
        for dato in self.tipoDato:
            return{
                "denominacion": dato.getDenominacion(),
                "unidad": dato.getUnidadDeMedida(),
                "valor": dato.getValorUmbral()
            } 

        