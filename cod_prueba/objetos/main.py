from datetime import datetime
from Gestor import Gestor
from PantallaRegistrarResultado import PantallaRegistrarResultado
from Estado import Estado
from EventoSismico import EventoSismico

def main():
    # Crear estados de ejemplo
    estado_auto = Estado(nombre="Auto Detectado", ambito="EventoSismico", descripcion="Detectado automáticamente")
    estado_manual = Estado(nombre="Manual", ambito="EventoSismico", descripcion="Cargado manualmente")

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

    gestor = Gestor(lista_eventos=lista_eventos, pantalla=None)
    pantalla = PantallaRegistrarResultado(gestor)
    gestor.pantalla = pantalla
    pantalla.opcRegistrarResultado()

    pantalla.root.mainloop()

if __name__ == "__main__":
    main()
