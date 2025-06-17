class Pantalla:
    def __init__(self, btnIngresarOpcion, listaEventosSismicos, btnMapaSismico, btnModificacionDatos, listaSeriesTemporales, grillOpciones, gestor):
        self.btnIngresarOpcion = btnIngresarOpcion
        self.listaEventosSismicos = listaEventosSismicos
        self.btnMapaSismico = btnMapaSismico
        self.btnModificacionDatos = btnModificacionDatos
        self.listaSeriesTemporales = listaSeriesTemporales
        self.grillOpciones = grillOpciones
        self.gestor = gestor

    def opcRegistrarResultado(self):
        #aca va un boton que permite registrar un resultado de un evento sismico
        opcion = input("ingrese la opcion de registrar resultado: ")

    def habilitar(self):
        # Habilita los botones de la pantalla (estos los puse como ej)
        self.btnIngresarOpcion = True
        self.btnMapaSismico = True
        self.btnModificacionDatos = True
        self.gestor.opcRegistrarResultado()

    def presentarEventos(self,eventos_auto_detectados):
        for evento in eventos_auto_detectados:
            print(f"Evento: {evento}")

    def opcSeleccionarEvento(self, eventos_auto_detectados):
        # Permite seleccionar un evento sismico de la lista, esto es con boton
        seleccion = input("Seleccione un evento sismico: ")
        return seleccion 

    def habilitarOpcionMapaSismico(self):
        self.btnMapaSismico = True

    def habilitarOpcionEstacionSismologicas(self):
        self.listaSeriesTemporales = True

    def solicitarOpcionVisualizarMapa(self):
        print("opciones")
        print("elija una opcion para visualizar el mapa sismico")

    def opcMapaSismico(self):
        #esto es todo con botones, hay que mejorarlo
        opcion = input("")
        self.gestor.tomarModificacionDatos()
        return opcion
        

    def habilitarOpcionModificacionDatos(self):
        # Habilita la opción de modificar datos
        self.btnModificacionDatos = True

    def solicitarOpcionModifiacionDatos(self):
        # Solicita al usuario que ingrese una opción para modificar datos
        opcion = input("Ingrese la opción para modificar datos: ")
        if opcion == "modificar":
            self.opcModificacionDatos()
        else:
            print("Opción no válida")
      
    def opcModificacionDatos(self):
        # Lógica para modificar datos
        print("Modificando datos...")
        
    def habilitarOpciones(self):
        # Habilita las opciones de la pantalla
        self.btnIngresarOpcion = True


    def solicitarSeleccionarOpcion(self):
        # Solicita al usuario que ingrese una opción
        opcion = input("Ingrese la opción deseada: ")
        if opcion in self.grillOpciones:
            print(f"Opción seleccionada: {opcion}")
        else:
            print("Opción no válida")
            
    def ingresarSeleccion(self):
        # Permite al usuario ingresar una selección
        seleccion = input("Ingrese su selección: ")
        if seleccion in self.grillOpciones:
            print(f"Selección ingresada: {seleccion}")
        else:
            print("Selección no válida")
