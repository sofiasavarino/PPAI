class Empleado:
    def __init__(self, apellido, nombre, mail, telefono):
        self.apellido = apellido
        self.nombre = nombre
        self.mail = mail
        self.telefono = telefono

    def getEmpleado(self):
        return self.empleado