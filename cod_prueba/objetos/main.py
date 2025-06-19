from datetime import datetime
from Gestor import Gestor
from PantallaRegistrarResultado import PantallaRegistrarResultado
from Estado import Estado
from EventoSismico import EventoSismico
from Sesion import Sesion
from Usuario import Usuario
from Empleado import Empleado
from Sismografo import Sismografo
from EstacionSismologica import EstacionSismologica
from SerieTemporal import SerieTemporal
from MuestraSismica import MuestraSismica
from DetalleMuestra import DetalleMuestra
from TipoDato import TipoDato
from AlcanceSismo import AlcanceSismo
from OrigenDeGeneracion import OrigenDeGeneracion
from ClasificacionSismo import ClasificacionSismo
from CambioEstado import CambioEstado

def main():
    # Crear estados de ejemplo
    estado_auto = Estado(nombre="Auto Detectado", ambito="Evento Sismico", descripcion="Detectado automáticamente")
    estado_manual = Estado(nombre="Manual", ambito="Evento Sismico", descripcion="Cargado manualmente")
    estado_bloqueado = Estado(nombre="Bloqueado", ambito="Evento Sismico", descripcion="Bloqueado por el sistema")
    estado_rechazado = Estado(nombre="Rechazado", ambito="Evento Sismico", descripcion="Rechazado por el usuario")

    lista_estados = [estado_auto, estado_manual, estado_bloqueado, estado_rechazado]

    estacionSismologica1 = EstacionSismologica( 
        codigoEstacion = "EST1",
        documentoCertificacionAdq = "DOC1",
        fechaSolicitudCertificacion = datetime(2024, 1, 1),
        nombre = "Estación 1",
        latitud = -34.6,
        longitud = -58.4,
        nroCertificacionAdquisicion = "CERT1"
    )

    estacionSismologica2 = EstacionSismologica(
        codigoEstacion = "EST2",
        documentoCertificacionAdq = "DOC2",
        fechaSolicitudCertificacion = datetime(2024, 2, 1),
        nombre = "Estación 2",
        latitud = -35.0,
        longitud = -59.0,
        nroCertificacionAdquisicion = "CERT2"       
    )

    sismografo1 = Sismografo(
        fechaAdquisicion = datetime(2022, 6, 1),
        identificadorSismografo = "SIS1",
        nroSerie = 1234,
        estacionSismologica = estacionSismologica1
    )

    sismografo2 = Sismografo(
        fechaAdquisicion = datetime(2023, 7, 15),
        identificadorSismografo = "SIS2",
        nroSerie = 5678,
        estacionSismologica = estacionSismologica2
    )

    lista_sismografos = [sismografo1, sismografo2]
    usuario1 = Usuario(
        nombre_usuario="Usuario Test",
        contrasena="contrasena123",
    )

    usuario2 = Usuario(
        nombre_usuario="Usuario Test 2",
        contrasena="contrasena1234",
    )

    sesion1 = Sesion(
        fechaHoraDesde=datetime(2024, 6, 1, 12, 0),
        fechaHoraHasta=datetime(2024, 6, 2, 16, 0),
        usuario=usuario1,
    )


    empleado1 = Empleado(
        nombre="Empleado Test",
        apellido="Apellido Test",
        mail="sjasaijsia",
        telefono="123456789",
        usuario=usuario1,
    )

    empleado2 = Empleado(
        nombre="Empleado Test 2",
        apellido="Apellido Test 2",
        mail="sjasaijsia2",
        telefono="987654321",
        usuario=usuario2,
    )
    
    lista_empleados = [empleado1, empleado2]

    tipoDato1 = TipoDato(denominacion="Tipo Test", unidadDeMedida="m/s", valorUmbral=10.0)
    tipoDato2 = TipoDato(denominacion="Tipo Test 2", unidadDeMedida="m/s", valorUmbral=15.0)

    lista_tipoDato = [tipoDato1,tipoDato2]

    detalleMuestra1 = DetalleMuestra(
        valor = 5,
        lista_tipoDato = lista_tipoDato
    )

    detalle_muestra2 = DetalleMuestra(
        valor=5.2,  # Valor de la muestra
        lista_tipoDato=lista_tipoDato)

    lista_detalleMuestra = [detalleMuestra1,detalle_muestra2]

    muestraSismica1 = MuestraSismica(
        fechaHoraMuestra = datetime(2024, 6, 1, 12, 0),
        lista_detalleMuestra = lista_detalleMuestra
    )

    muestraSismica2 = MuestraSismica(
            fechaHoraMuestra = datetime(2023, 6, 7, 11, 0),
            lista_detalleMuestra = lista_detalleMuestra
        )
    
    lista_muestras_sismicas = [muestraSismica1,muestraSismica2]

    serieTemporal1 = SerieTemporal(
        condicionAlarma = "Condición de Alarma",
        fechaHoraInicioRegistroMuestras = datetime(2024, 6, 1, 12, 0),
        fechaHoraRegistro = datetime(2024, 6, 1, 12, 0),
        frecuenciaMuestreo=100,
        muestraSismica= None, 
        sismografo = sismografo2,
        lista_muestras_sismicas= lista_muestras_sismicas)
    
    serieTemporal2 = SerieTemporal(
        condicionAlarma = "Condición de Alarma 2",
        fechaHoraInicioRegistroMuestras = datetime(2024, 6, 1, 12, 0),         
        fechaHoraRegistro = datetime(2024, 6, 1, 12, 0),
        frecuenciaMuestreo=200,
        muestraSismica= None,
        sismografo = sismografo1,
        lista_muestras_sismicas= lista_muestras_sismicas)
    
    lista_series_temporales = [serieTemporal1, serieTemporal2]

    alcanceSismo1 = AlcanceSismo(
        nombre= "al",
        descripcion= "descc"
    )

    alcanceSismo2 = AlcanceSismo(
        nombre= "al2",
        descripcion= "descc2"
    )

    alcanceSismo3 = AlcanceSismo(
        nombre= "al3",
        descripcion= "descc3"
    )

    origenSismo1 = OrigenDeGeneracion(
        nombre= "or",
        descripcion= "descc"
    )

    origenSismo2 = OrigenDeGeneracion(
        nombre= "or2",
        descripcion= "descc2"
    )

    origenSismo3 = OrigenDeGeneracion(
        nombre= "or3",
        descripcion= "descc3"
    )

    clasificacionSismo1 = ClasificacionSismo(
        nombre = "c",
        kmProfundidadDesde = 5,
        kmProfundidadHasta = 100
    )

    clasificacionSismo2 = ClasificacionSismo(
        nombre = "c2",
        kmProfundidadDesde = 52,
        kmProfundidadHasta = 102
    )

    clasificacionSismo3 = ClasificacionSismo(
        nombre = "c3",
        kmProfundidadDesde = 53,
        kmProfundidadHasta = 103
    )
    
    # Crear eventos sísmicos de ejemplo
    evento1 = EventoSismico(
        fechaHoraFin=None,
        fechaHoraOcurrencia="2024-06-01 15:00",
        latitudEpicentro=-34.6,
        latitudHipocentro=-34.7,
        longitudEpicentro=-58.4,
        longitudHipocentro=-58.5,
        valorMagnitud=5.2,
        cambioEstado=[
            CambioEstado(
                fechaHoraInicio="2024-06-01 15:00",
                fechaHoraFin=None,
                estado=estado_auto,
            )
        ],
        estado=estado_auto,
        serieTemporal=serieTemporal1,
        origenSismo= origenSismo3,
        clasificacionSismo= clasificacionSismo3,
        alcanceSismo=alcanceSismo3,
        empleado=empleado1,
        lista_Series_temporales=lista_series_temporales
    )
    evento2 = EventoSismico(
        fechaHoraFin=None,
        fechaHoraOcurrencia="2024-06-02 14:30",
        latitudEpicentro=-35.0,
        latitudHipocentro=-35.1,
        longitudEpicentro=-59.0,
        longitudHipocentro=-59.1,
        valorMagnitud=4.8,
        cambioEstado=[
            CambioEstado(
                fechaHoraInicio="2024-06-02 14:30",
                fechaHoraFin=None,
                estado=estado_auto,
            )
        ],
        estado=estado_manual,
        serieTemporal=None,
        origenSismo= origenSismo2,
        clasificacionSismo= clasificacionSismo2,
        alcanceSismo=alcanceSismo2,
        empleado=None,
        lista_Series_temporales=lista_series_temporales
    )
    evento3 = EventoSismico(
        fechaHoraFin=None,
        fechaHoraOcurrencia="2024-06-01 13:50",
        latitudEpicentro=-35.6,
        latitudHipocentro=-44.7,
        longitudEpicentro=-58.4,
        longitudHipocentro=-58.5,
        valorMagnitud=5.2,
        cambioEstado=[
            CambioEstado(
                fechaHoraInicio="2024-06-01 13:50",
                fechaHoraFin=None,
                estado=estado_auto,
            )
        ],
        estado=estado_auto,
        serieTemporal=serieTemporal2,
        origenSismo= origenSismo1,
        clasificacionSismo= clasificacionSismo1,
        alcanceSismo=alcanceSismo1,
        empleado=empleado2,
        lista_Series_temporales=lista_series_temporales
    )

    lista_eventos = [evento1, evento2, evento3]



    

    gestor = Gestor(sesion= sesion1,lista_sismografos=lista_sismografos, lista_empleados=lista_empleados, lista_eventos=lista_eventos, lista_estados= lista_estados, estado = Estado, pantalla=None)
    pantalla = PantallaRegistrarResultado(gestor)
    gestor.pantalla = pantalla
    pantalla.opcRegistrarResultado()

    pantalla.root.mainloop()
    print(gestor.eventoSismicoSeleccionado)

if __name__ == "__main__":
    main()
