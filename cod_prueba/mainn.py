from objetos.Gestor import Gestor
from objetos.Pantalla import Pantalla
from objetos.EventoSismico import EventoSismico
from objetos.Estado import Estado

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

    # Instanciar el gestor y la pantalla
    gestor = Gestor(
        eventos_auto_detectado=None,
        eventoSismicoSeleccionado=None,
        eventoBloqueadoEnRevision=None,
        detalleEventoSismico=None,
        usuarioLogueado=None,
        eventoRechazado=None,
        fechaHoraOcurrenciaEvento=None,
        clasificacionEvento=None,
        eventoSismico=None,
        estado=None,
        empleado=None,
        sesion=None,
        pantalla=None  # Se asigna después
    )
    pantalla = Pantalla(
        btnIngresarOpcion=None,
        listaEventosSismicos=lista_eventos,
        btnMapaSismico=None,
        btnModificacionDatos=None,
        listaSeriesTemporales=None,
        grillOpciones=None,
        gestor=gestor
    )
    gestor.pantalla = pantalla  # Asocia la pantalla al gestor

    # Flujo principal
    pantalla.opcRegistrarResultado()
   # pantalla.habilitar()
    eventos_auto_detectados = gestor.buscarEventosAutoDetectados(lista_eventos)
    eventos_ordenados = gestor.ordenarPorFechayHora(eventos_auto_detectados)
    pantalla.presentarEventos(eventos_ordenados)
    pantalla.opcSeleccionarEvento(eventos_ordenados)
    

    evento_seleccionado = gestor.tomarSeleccionarEvento(eventos_auto_detectados)
    print("Evento seleccionado:", evento_seleccionado)

if __name__ == "__main__":
    main()