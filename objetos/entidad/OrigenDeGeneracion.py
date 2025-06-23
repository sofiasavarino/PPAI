class OrigenDeGeneracion:
    def __init__(self, nombre,descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def getNombre(self):
        print("saque nombre ori 6")
        return self.nombre
    
    #Método que se agrega por alternativa 1
    def setNombre(self,origen):
        self.nombre = origen