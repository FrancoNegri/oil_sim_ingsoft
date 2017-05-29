from flask import Flask, render_template, request
app = Flask(__name__)
import json
from parcela import *
from politicas import *
from simulador import *
from yacimiento import *
from rig import *

@app.route("/")
def index():
	return render_template("index.html")

@app.route('/log', methods=['POST'])
def log():
	data = request.form.to_dict()
	#return data

	#Yacimiento
	volumen_inicial = data['data[volumen_inicial]']
	pr_gas = data['data[pr_gas]']
	pr_agua = data['data[pr_agua]']
	pr_petroleo = data['data[pr_petroleo]']
	yacimiento = Yacimiento(volumen_inicial,pr_gas,pr_agua,pr_petroleo)

	#Constructor de Plantas
	plantas_tiempoDeConstruccion = data['data[plantas_duracion]']
	plantas_costo = data['data[plantas_precio]']
	plantas_capacidadMax = data['data[plantas_capacidad]']
	constructorDePlantas = ConstructorDePlantasProcesadoras(plantas_tiempoDeConstruccion, plantas_costo, plantas_capacidadMax)
	#Constructor de Tanques
	tanques_tiempoDeConstruccion = data['data[tanques_duracion]']
	tanques_costo = data['data[tanques_precio]']
	tanques_capacidadMax = data['data[tanques_capacidad]']
	constructorDeTanques = ConstructorDeTanques(tanques_tiempoDeConstruccion, tanques_costo, tanques_capacidadMax)

	#Politicas
	if data['data[pol_final]'] == 'Contrato':
		politicaDeFinalizacion = politicaDeFinalizacionVencimientoDeContrato(100)

	if data['data[pol_reinyectar]'] == 'PuntoCritico':
		politicaDeReinyeccion = PoliticaDeReinyeccionReinyectoEnPuntoCritico(10,20)

	if data['data[pol_cuando_perforar]'] == 'Principio':
		politicaCuandoPerforar = politicaCuandoPerforarParcelasTodasAlPrincipio()

	cant_pozos = data['data[cant_pozos]']
	if data['data[pol_cual_perforar]'] == 'MenorProfundidad':
		politicaCualYCantidaddePozosParcela = politicaDeSeleccionMenorProfundidad(cant_pozos)
	
	if data['data[pol_eleccion_rigs]'] == 'Random':
		politicaEleccionRigs = PoliticaEleccionRigRandom()

	if data['data[pol_cual_extraer]'] == 'Todos':
		politicaDeEleccionDePozos = politicaDeEleccionDeParcelasParaExtraccion()

	if data['data[pol_tanques]'] == 'Principio':
		politicaDeConsutrccionTanques = politicaDeConstruccionDeEstructurasAlPrincipio(2)

	if data['data[pol_plantas]'] == 'Principio':
		politicaDeConsutrccionPlantas = politicaDeConstruccionDeEstructurasAlPrincipio(3)

	#Parcelas
	cant_parcelas = data['data[cant_parcelas]'] 
	parcelas = []

	for i in range(1,int(cant_parcelas)):
		
		if data['data[tipo_terreno][' + str(i) + ']'] == 'roca':
			terreno = TerrenoRocoso()
		elif data['data[tipo_terreno][' + str(i) + ']'] == 'arcilla':
			terreno = TerrenoArcilloso()

		presion = data['data[presion][' + str(i) + ']'] 
		profundidad = data['data[profundidad][' + str(i) + ']'] 

		parcela = ParcelaConcreta(yacimiento,presion,terreno,profundidad)
		parcelas.append(parcela)

	#Rigs
	rigs_standard = data['data[rigs_standard]']
	rigs_premium = data['data[rigs_premium]']
	rigs_superpremium = data['data[rigs_superpremium]']
	rigs = []

	for i in range(1,int(rigs_standard)):
		rig = Rig(10, 50, 2, 15)
		rigs.append(rig)

	for i in range(1,int(rigs_premium)):
		rig = Rig(20, 70, 4, 25)
		rigs.append(rig)

	for i in range(1,int(rigs_superpremium)):
		rig = Rig(40, 90, 4, 35)
		rigs.append(rig)


	sim = Simulador(rigs,parcelas,politicaDeEleccionDePozos,politicaCuandoPerforar,politicaCualYCantidaddePozosParcela, politicaEleccionRigs,politicaDeConsutrccionTanques,politicaDeConsutrccionPlantas, constructorDeTanques, constructorDePlantas, politicaDeFinalizacion, politicaDeReinyeccion)
	return sim.start()

if __name__ == "__main__":
	app.run(debug=True)