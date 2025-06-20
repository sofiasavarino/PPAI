class Sesion:
    def __init__(self, fechaHoraDesde, fechaHoraHasta,usuario):
        self.fechaHoraDesde = fechaHoraDesde
        self.fechaHoraHasta = fechaHoraHasta

        #Relacion con otra clase
        self.usuario = usuario

    def getNombreUsuario(self):
        return self.usuario.getNombre()