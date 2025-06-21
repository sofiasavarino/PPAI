from datetime import datetime
from control.GestorRegistrarResultado import GestorRegistrarResultado
from boundary.PantallaRegistrarResultado import PantallaRegistrarResultado
from entidad.Estado import Estado
from entidad.EventoSismico import EventoSismico
from entidad.Sesion import Sesion
from entidad.Usuario import Usuario
from entidad.Empleado import Empleado
from entidad.Sismografo import Sismografo
from entidad.EstacionSismologica import EstacionSismologica
from entidad.SerieTemporal import SerieTemporal
from entidad.MuestraSismica import MuestraSismica
from entidad.DetalleMuestra import DetalleMuestra
from entidad.TipoDato import TipoDato
from entidad.AlcanceSismo import AlcanceSismo
from entidad.OrigenDeGeneracion import OrigenDeGeneracion
from entidad.ClasificacionSismo import ClasificacionSismo
from entidad.CambioEstado import CambioEstado

def main():
    # Crear estados de ejemplo
    estado_auto = Estado(nombre="Auto Detectado", ambito="Evento Sismico", descripcion="Detectado automáticamente")
    estado_manual = Estado(nombre="Manual", ambito="Evento Sismico", descripcion="Cargado manualmente")
    estado_bloqueado = Estado(nombre="Bloqueado", ambito="Evento Sismico", descripcion="Bloqueado por el sistema")
    estado_rechazado = Estado(nombre="Rechazado", ambito="Evento Sismico", descripcion="Rechazado por el usuario")
    estado_derivado= Estado(nombre="Derivado", ambito="Evento Sismico", descripcion="Derivado a analista supervisor")
    estado_aceptado = Estado(nombre="Aceptado", ambito="Evento Sismico", descripcion="")
    estado_pendienteCierre = Estado(nombre="Pendiente de cierre", ambito="Evento Sismico", descripcion="")
    estado_cerrado = Estado(nombre="Cerrado", ambito="Evento Sismico", descripcion="")
    estado_pendienteRevision = Estado(nombre="Sin revision", ambito="Evento Sismico", descripcion="autodetectados pedientes de revision")


    lista_estados = [estado_auto, estado_manual, estado_bloqueado, estado_rechazado, estado_aceptado,estado_derivado,estado_pendienteCierre,estado_cerrado, estado_pendienteRevision]

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
        nombre_usuario="pepito123",
        contrasena="contrasena123",
    )

    usuario2 = Usuario(
        nombre_usuario="juanito321",
        contrasena="contrasena1234",
    )

    usuario3 = Usuario(
        nombre_usuario= "messi10",
        contrasena="goat"
    )

    sesion1 = Sesion(
        fechaHoraDesde=datetime(2024, 6, 1, 12, 0),
        fechaHoraHasta=datetime(2024, 12, 2, 16, 0),
        usuario=usuario1,
    )


    empleado1 = Empleado(
        nombre="Juan",
        apellido="Perez",
        mail="juanitoPerez@gmail.com",
        telefono="123456789",
        usuario=usuario2,
    )

    empleado2 = Empleado(
        nombre="Pepe",
        apellido="Lopez",
        mail="lopezPepito@gmail.com",
        telefono="987654321",
        usuario=usuario1,
    )

    empleado3 = Empleado(
        nombre= "Lionel Andrés",
        apellido="Messi",
        mail= "messi10@gmail.com",
        telefono= "18122022",
        usuario=usuario3
    )
    
    lista_empleados = [empleado1, empleado2,empleado3]

    tipoDato1 = TipoDato(denominacion="Test", unidadDeMedida="m/s", valorUmbral=10.0)
    tipoDato2 = TipoDato(denominacion="Grande", unidadDeMedida="m/s", valorUmbral=15.0)

    detalleMuestra1 = DetalleMuestra(
        valor = 5,
        tipoDato = tipoDato1
    )

    detalle_muestra2 = DetalleMuestra(
        valor=5.2,  
        tipoDato=tipoDato2)

    lista_detalleMuestra = [detalleMuestra1,detalle_muestra2]

    muestraSismica1 = MuestraSismica(
        fechaHoraMuestra = datetime(2024, 6, 1, 12, 0),
        lista_detalleMuestra = lista_detalleMuestra
    )

    muestraSismica2 = MuestraSismica(
            fechaHoraMuestra = datetime(2023, 6, 7, 11, 0),
            lista_detalleMuestra= lista_detalleMuestra
        )
    
    lista_muestras_sismicas = [muestraSismica1,muestraSismica2]

    serieTemporal1 = SerieTemporal(
        condicionAlarma = "Condición de Alarma",
        fechaHoraInicioRegistroMuestras = datetime(2024, 6, 1, 12, 0),
        fechaHoraRegistro = datetime(2024, 6, 1, 12, 0),
        frecuenciaMuestreo=100,
        lista_muestras_sismicas= lista_muestras_sismicas, 
        sismografo = sismografo2,
    )
    
    serieTemporal2 = SerieTemporal(
        condicionAlarma = "Condición de Alarma 2",
        fechaHoraInicioRegistroMuestras = datetime(2024, 6, 1, 12, 0),         
        fechaHoraRegistro = datetime(2024, 6, 1, 12, 0),
        frecuenciaMuestreo=200,
        lista_muestras_sismicas= lista_muestras_sismicas,
        sismografo = sismografo1,
        )
    
    lista_series_temporales = [serieTemporal1, serieTemporal2]

    alcanceSismo1 = AlcanceSismo(
        nombre= "Sismo local", 
        descripcion= "Hasta 100 km"
    )

    alcanceSismo2 = AlcanceSismo(
        nombre= "alSismo regional", 
        descripcion= "Hasta 1000 km2"
    )

    alcanceSismo3 = AlcanceSismo(
        nombre= "Tele sismo",
        descripcion= "Mas de 1000 km"
    )

    origenSismo1 = OrigenDeGeneracion(
        nombre= "Tectonico", 
        descripcion= "Movimiento de placas tectonicas"
    )

    origenSismo2 = OrigenDeGeneracion(
        nombre= "Volcanico", 
        descripcion= "Actividad volcanica"
    )

    origenSismo3 = OrigenDeGeneracion(
        nombre= "Desconocido",
        descripcion= "Origen desconocido"
    )

    clasificacionSismo1 = ClasificacionSismo(
        nombre = "Superficial",
        kmProfundidadDesde = 5,
        kmProfundidadHasta = 70
    )

    clasificacionSismo2 = ClasificacionSismo(
        nombre = "Intermedio",
        kmProfundidadDesde = 71,
        kmProfundidadHasta = 300
    )

    clasificacionSismo3 = ClasificacionSismo(
        nombre = "Profundo",
        kmProfundidadDesde = 301,
        kmProfundidadHasta = 700
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
        empleado=empleado3,
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
        empleado=None,
        lista_Series_temporales=lista_series_temporales
    )

    lista_eventos = [evento1, evento2, evento3]



    

    gestor = GestorRegistrarResultado(sesion= sesion1,lista_sismografos=lista_sismografos, lista_empleados=lista_empleados, lista_eventos=lista_eventos, lista_estados= lista_estados,  pantalla=None)
    pantalla = PantallaRegistrarResultado(gestor)
    gestor.pantalla = pantalla
    pantalla.opcRegistrarResultado()

    pantalla.root.mainloop()
    print(gestor.eventoSismicoSeleccionado)

if __name__ == "__main__":
    main()
