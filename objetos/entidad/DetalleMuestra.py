class DetalleMuestra:
    def __init__(self,valor, tipoDato):
        #Atributo Propio:
        self.valor = valor

        #Relacion con otras clases:
        self.tipoDato = tipoDato

    def getDatos(self):
        print( "estoy en get datos del detalle 10")
        return{
                "denominacion": self.tipoDato.getDenominacion(),
                "unidad": self.tipoDato.getUnidadDeMedida(),
                "valor": self.tipoDato.getValorUmbral()
            } 

        