from parcela import *
from politicas import *
from simulador import *
from yacimiento import *
from rig import *

#Mock de un main para testear funcionalidad
def main():
	#esto es super mega cabeza, el main/interfaz grafica va a conocer a todo
	politicaCuandoPerforar = politicaCuandoPerforarParcelasTodasAlPrincipio()
	politicaCualYCantidaddePozosParcela = politicaDeSeleccionMenorProfundidad(4)
	politicaEleccionRigs = PoliticaEleccionRigRandom()
	politicaDeEleccionDePozos = politicaDeEleccionDeParcelasParaExtraccion()
	politicaDeConsutrccionTanques = politicaDeConstruccionDeEstructurasAlPrincipio(3)
	politicaDeConsutrccionPlantas = politicaDeConstruccionDeEstructurasAlPrincipio(3)
	yacimiento = Yacimiento(10000,20,30,50)
	parcelas = [ParcelaConcreta(yacimiento,10, TerrenoArcilloso(),10)]
	rigs = [Rig(10, 10,20,10),Rig(10,10,20,4)]
	constructorDePlantas = ConstructorDePlantasProcesadoras(10,10,200)
	constructorDeTanques = ConstructorDeTanques(10,20,100)
	politicaDeFinalizacion = politicaDeFinalizacionVencimientoDeContrato(100)
	politicaDeReinyeccion = PoliticaDeReinyeccionReinyectoEnPuntoCritico(10,20)
	sim = Simulador(rigs,parcelas,politicaDeEleccionDePozos,politicaCuandoPerforar,politicaCualYCantidaddePozosParcela, politicaEleccionRigs,politicaDeConsutrccionTanques,politicaDeConsutrccionPlantas, constructorDeTanques, constructorDePlantas, politicaDeFinalizacion, politicaDeReinyeccion)
	sim.start()

if __name__ == "__main__":
    main()