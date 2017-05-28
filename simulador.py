from subSimDeExcavacion import *
from subSimDeExtraccion import *
from subSimDeConstruccion import *
from subSimDeReinyeccion import *
from logger import Logger

class Simulador:
    def __init__(self,rigs,parcelas,politicaCuandoPerforar,politicaCualYCantidaddePozosParcela,politicaEleccionRigs,politicaDeConstruccionDeTanques,politicaDeConstruccionDePlantas):
        # yacimiento = (
        # parcelas = [Listdo de Parcelas] [ [Arcilloso, 20, 20], [Roca, 10, 15], [Roca, 1, 10] ]
        # politicaCuandoPerforar: Todas al Principio
        # politicaCualYCantidadDePozosParcela: De Menor Profundidad: cantidadDePozos (int)
        # politicaEleccionRigs: Random
        # politicaDeConsutrccionTanques: Todas al Principio parametro: cantidad a construir (int)
        # politicaDeConstruccionDePlantas : Todas al principio: cantidad a construir (int)
        # rigs = listado de rigs
        #FALTA!!
        # self.politicaDeFinalizacion: punto critico
        # self.constructorDePlantas
        # self.constructorDeTanques

        self.parcelas = parcelas
        self.logger = Logger("log.txt")
        self.dia = 0
        self.unSubSimDeExcavacion = SubSimDeExcavacion(politicaDeEleccionDeRig,politicaCualYcantidadDePozosParcela,rigs)
        self.unSubSimDeExtraccion = SubSimDeExtraccion(parcelas,politicaDeEleccionDePozos)
        self.unSubSimDeReinyeccion = SubSimDeReinyeccion()
        self.unSubSimDeConstruccion = SubSimDeConstruccion(politicaDeConstruccionDeTanques,politicaDeConstruccionDePlantas, constructorDePlantas, constructorDeTanques)
        self.politicaDeFinalizacion = politicaDeFinalizacion
        parcelas = []
        self.logger = Logger("log.txt")
        self.dia = 0
        self.unSubSimDeExcavacion = SubSimDeExcavacion(politicaDeSeleccionMenorProfundidad(3),politicaCuandoPerforarParcelasTodasAlPrincipio(), parcelas)
        self.unSubSimDeExtraccion = SubSimDeExtraccion(self.logger)
        self.unSubSimDeReinyeccion = SubSimDeReinyeccion(self.logger)

        self.unSubSimDeConstruccion = SubSimDeConstruccion(politicaDeConstruccionDeTanques,politicaDeConstruccionDePlantas,constructorDePlantas,constructorDeTanques)

  def start():
      while self.politicaDeFinalizacion.finalizo():
          self.pasarDeDia()

    def filtrarConPozo(parcela):
        return parcela.listoParaExtraer()

    def filtrarSinPozo(parcela):
        return !parcela.listoParaExtraer()

    def filtrarParcelas(funcionParaFiltrar):
        return list(filter(funcionParaFiltrar,self.parcelas))

    def pasarDeDia(self):
        self.comenzarDia()
        eventos = []
        eventoComienzoDelDia = Evento(0,"Comienzo del dia " + str(self.dia))
        eventos.append(eventoComienzoDelDia)

        #me quedon con las parcelas que quiero perforar
        parcelasSinPozo = self.filtrarParcelas(self.filtrarSinPozo)

        #me quedon con las parcelas que puedo extraer o reinyectar
        parcelasConPozo = self.filtrarParcelas(self.filtrarConPozo)

        tanques =  self.unSubSimDeConstruccion.tanques()
        plantasProcedoras =  self.unSubSimDeConstruccion.plantasProcesadoras()

        if politicaDeReinyeccion.elijoReinyectar(parcelasConPozo,dia):
            eventosDeReinyeccion = self.unSubSimDeReinyeccion.simularReinyeccion(self.dia, parcelasConPozo, plantasProcesadoras, tanques)
        else:
            eventosDeExtraccion = self.unSubSimDeExtraccion.simularExtraccion(self.dia, parcelasConPozo, plantasProcesadoras, tanques)

        eventosDeExcavacion = self.unSubSimDeExcavacion.simularExcavacion(self.dia,parcelasSinPozo)
        eventosDeConstruccion = self.unSubSimDeConstruccion.simularConstruccion(self.dia)
        eventos = eventos + eventosDeExcavacion + eventosDeExtraccion + eventosDeReinyeccion + eventosDeConstruccion
        eventoFinDelDia = Evento(0,"Fin del dia " + str(self.dia))
        eventos.append(eventoFinDelDia)
        self.logger.logearEventos(eventos)  def comenzarDia(self):
        self.dia += 1

sim = Simulador()
sim.pasarDeDia()