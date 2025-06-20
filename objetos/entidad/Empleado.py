class Empleado:
    def __init__(self, apellido, nombre, mail, telefono, usuario):
        self.apellido = apellido
        self.nombre = nombre
        self.mail = mail
        self.telefono = telefono

        #Relacion con otra clase
        self.usuario = usuario

    def esTuUsuario(self, nombre_usuario):
        return self.usuario.getNombre() == nombre_usuario