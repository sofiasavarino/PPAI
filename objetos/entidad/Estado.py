class Estado:
    def __init__(self, nombre, ambito, descripcion):
        self.nombre = nombre
        self.ambito = ambito
        self.descripcion = descripcion

    def esAmbitoEventoSismico(self):
        if self.ambito == "Evento Sismico":
            return True
        else:
            return False
    
    def esAutoDetectado(self):
        if self.nombre == "Auto Detectado":
            return True
        return False

    def esBloqueado(self):
        if self.nombre == "Bloqueado En Revisión":
            return True
        return False
    
    def esRechazado(self):
        if self.nombre == "Rechazado":
            return True
        return False

   #Metodo añadido por alternativa 1     
    def getNombre(self):
        return self.nombre
    
    #Método añadido por alternativa 2
    def esConfirmado(self):
        if self.nombre == "Confirmado":
            return True
        return False
 


