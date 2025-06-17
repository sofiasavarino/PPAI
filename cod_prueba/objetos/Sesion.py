class Sesion:
    def __init__(self, fechaHoraDesde, fechaHoraHasta,usuario):
        self.fechaHoraDesde = fechaHoraDesde
        self.fechaHoraHasta = fechaHoraHasta
        self.usuario = usuario

    def getNombreUsuario(self):
        return self.usuario.getNombre()