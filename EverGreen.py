from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import statistics as stats

app = Flask(__name__)
CORS(app)

tipo_medicion = { 'sensor' : 'DS18B20', 'variable' : 'Temperatura', 'unidades' : 'Centigrados'}

mediciones = [
    {'fecha' : '2019-08-21 15:38:43', **tipo_medicion, 'valor' : 100},
    {'fecha' : '2019-08-22 15:37:56', **tipo_medicion, 'valor' : 98},
    {'fecha' : '2019-08-23 15:41:16', **tipo_medicion, 'valor' : 101},
    {'fecha' : '2019-08-24 15:43:18', **tipo_medicion, 'valor' : 101},    
    {'fecha' : '2019-08-25 15:41:16', **tipo_medicion, 'valor' : 98},    
    {'fecha' : '2019-08-26 15:40:20', **tipo_medicion, 'valor' : 98},    
    {'fecha' : '2019-08-27 15:31:16', **tipo_medicion, 'valor' : 101},
    {'fecha' : '2019-08-28 15:53:18', **tipo_medicion, 'valor' : 101},
]

@app.route("/")
def get():
    return jsonify(tipo_medicion)


@app.route('/mediciones', methods = ['GET'])
def getAll():
    return jsonify(mediciones)


@app.route('/mediciones', methods = ['POST'])
def postOne():
    now = datetime.now()
    body = request.json
    body['fecha'] = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
    mediciones.append({**body, **tipo_medicion})
    return jsonify(mediciones)

"""
@app.route('mediciones/<string:fecha>', methods=['DELETE'])
def deleteOne(fecha):
    x = False
    for medicion in mediciones:
        if (fecha in medicion['fecha']):
            x = True
            mediciones.remove(medicion)
    return 'Eliminado' if x else "No Encontrado"


@app.route('/mediciones/<string:fecha>', methods=['PUT'])
def putOne(fecha):
    body = request.json
    x = False
    for medicion in mediciones:
        if(fecha in medicion['fecha']):
            x = True
            medicion['valor'] = body['valor']
    return 'Modificado' if x else 'No Encontrado'
""" 

@app.route('/mediciones/moda', methods = ['GET'])
def getModa():
    repetir = 0
    for medicion in mediciones:
        aparece = mediciones.count(medicion)
        if aparece > repetir:
            repetir = aparece

    moda = []
    for medicion in mediciones:
        aparece = mediciones.count(medicion)
        if aparece == repetir and medicion not in moda:
            moda.append(medicion)
            
    return jsonify(medicion['valor'])


app.run(port=5000, debug=True)


