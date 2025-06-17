from datetime import datetime
from Gestor import Gestor
from PantallaRegistrarResultado import PantallaRegistrarResultado
from Estado import Estado
from EventoSismico import EventoSismico
from Sesion import Sesion
from Usuario import Usuario
from Empleado import Empleado

def main():
    # Crear estados de ejemplo
    estado_auto = Estado(nombre="Auto Detectado", ambito="Evento Sismico", descripcion="Detectado automáticamente")
    estado_manual = Estado(nombre="Manual", ambito="Evento Sismico", descripcion="Cargado manualmente")
    estado_bloqueado = Estado(nombre="Bloqueado", ambito="Evento Sismico", descripcion="Bloqueado por el sistema")
    estado_rechazado = Estado(nombre="Rechazado", ambito="Evento Sismico", descripcion="Rechazado por el usuario")

    lista_estados = [estado_auto, estado_manual, estado_bloqueado, estado_rechazado]

    # Crear eventos sísmicos de ejemplo
    evento1 = EventoSismico(
        fechaHoraFin=None,
        fechaHoraOcurrencia="2024-06-01 15:00",
        latitudEpicentro=-34.6,
        latitudHipocentro=-34.7,
        longitudEpicentro=-58.4,
        longitudHipocentro=-58.5,
        valorMagnitud=5.2,
        cambioEstado=[],
        estado=estado_auto,
        serieTemporal=None,
        origenSismo=None,
        clasificacionSismo=None,
        alcanceSismo=None,
        empleado=None
    )
    evento2 = EventoSismico(
        fechaHoraFin=None,
        fechaHoraOcurrencia="2024-06-02 14:30",
        latitudEpicentro=-35.0,
        latitudHipocentro=-35.1,
        longitudEpicentro=-59.0,
        longitudHipocentro=-59.1,
        valorMagnitud=4.8,
        cambioEstado=[],
        estado=estado_manual,
        serieTemporal=None,
        origenSismo=None,
        clasificacionSismo=None,
        alcanceSismo=None,
        empleado=None
    )
    evento3 = EventoSismico(
        fechaHoraFin=None,
        fechaHoraOcurrencia="2024-06-01 13:50",
        latitudEpicentro=-35.6,
        latitudHipocentro=-44.7,
        longitudEpicentro=-58.4,
        longitudHipocentro=-58.5,
        valorMagnitud=5.2,
        cambioEstado=[],
        estado=estado_auto,
        serieTemporal=None,
        origenSismo=None,
        clasificacionSismo=None,
        alcanceSismo=None,
        empleado=None
    )

    lista_eventos = [evento1, evento2, evento3]

    sesion = Sesion(
        fechaHoraDesde=datetime(2024, 6, 1, 12, 0),
        fechaHoraHasta=datetime(2024, 6, 2, 16, 0),
        usuario=usuario1,
    )

    usuario1 = Usuario(
        nombreUsuario="Usuario Test",
        contrasena="contrasena123",
    )

    empleado1 = Empleado(
        nombre="Empleado Test",
        apellido="Apellido Test",
        mail="sjasaijsia",
        telefono="123456789",
        usuario=usuario1,
    )


    gestor = Gestor(sesion, lista_eventos=lista_eventos, lista_estados= lista_estados, estado = Estado, pantalla=None)
    pantalla = PantallaRegistrarResultado(gestor)
    gestor.pantalla = pantalla
    pantalla.opcRegistrarResultado()

    pantalla.root.mainloop()
    print(gestor.eventoSismicoSeleccionado)

if __name__ == "__main__":
    main()
