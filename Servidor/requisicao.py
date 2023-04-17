from flask import Flask, jsonify
import requests
import json
import time

app = Flask(__name__)

checar_resultado = []

@app.route('/resultados')
def obter_resultados():
    global checar_resultado
    
    response = requests.get('https://blaze.com/api/crash_games/recent')
    data = response.json()
    resultado_atual = [game['crash_point'] for game in data][:10]  # seleciona apenas os 10 primeiros valores
    resultado_atual = [float(valor) for valor in resultado_atual]  # converte os valores para float
    resultados = {"results": resultado_atual}
    resultados_json = json.dumps(resultados)
    
    if resultado_atual != checar_resultado:
        checar_resultado = resultado_atual.copy()
    
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True)
