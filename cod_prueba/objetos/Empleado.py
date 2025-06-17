class Empleado:
    def __init__(self, apellido, nombre, mail, telefono, usuario):
        self.apellido = apellido
        self.nombre = nombre
        self.mail = mail
        self.telefono = telefono
        self.usuario = usuario

    def esTuUsuario(self, nombre_usuario):
        # if self.usuario == usuario:
        #     return True
        # else:
        #     return False
        
        return self.usuario.getNombre() == nombre_usuario