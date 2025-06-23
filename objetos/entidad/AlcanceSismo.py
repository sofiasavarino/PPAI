class AlcanceSismo:
    def __init__(self, nombre,descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def getNombre(self):
        print("Saque nombre alcance 4")
        return self.nombre
    
    #Método que se agrega por alternativa 1
    def setNombre(self,alcance):
        self.nombre = alcance