from flask import Flask, render_template, request
from algoritmos import fcfs, sjf, round_robin, prioridad
from modelos.proceso import Proceso

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/planificar', methods=['POST'])
def planificar():
    datos = request.json
    procesos = [Proceso(p['nombre'], int(p['llegada']), int(p['duracion']), int(p.get('prioridad', 0))) for p in datos['procesos']]
    algoritmo = datos['algoritmo']
    quantum = int(datos.get('quantum', 2))

    if algoritmo == 'FCFS':
        resultado = fcfs.fcfs(procesos)
    elif algoritmo == 'SJF':
        resultado = sjf.sjf(procesos)
    elif algoritmo == 'Round Robin':
        resultado = round_robin.rr(procesos, quantum)
    elif algoritmo == 'Prioridades':
        resultado = prioridad.prioridades(procesos)
    else:
        return {"error": "Algoritmo no válido"}, 400

    return {
        "procesos": [
            {
                "nombre": p.nombre,
                "inicio": p.inicio,
                "final": p.final,
                "espera": p.espera,
                "retorno": p.retorno
            } for p in resultado
        ]
    }

if __name__ == '__main__':
    app.run(debug=True)
