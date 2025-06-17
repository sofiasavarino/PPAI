class Usuario:
    def __init__(self, nombre_usuario, contrasena,empleado):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.empleado = empleado
      
    def getEmpleado(self):
       return self.empleado