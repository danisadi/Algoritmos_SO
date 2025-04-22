def rr(procesos, quantum):
    cola = sorted(procesos, key=lambda p: p.llegada)
    tiempo = 0
    cola_ejecucion = []
    completados = []

    while cola or cola_ejecucion:
        cola_ejecucion += [p for p in cola if p.llegada <= tiempo]
        cola = [p for p in cola if p.llegada > tiempo]

        if cola_ejecucion:
            p = cola_ejecucion.pop(0)
            if p.restante == p.duracion:
                p.inicio = tiempo
            ejecutar = min(quantum, p.restante)
            p.restante -= ejecutar
            tiempo += ejecutar
            if p.restante == 0:
                p.final = tiempo
                p.retorno = p.final - p.llegada
                p.espera = p.retorno - p.duracion
                completados.append(p)
            else:
                cola_ejecucion += [p]
        else:
            tiempo += 1
    return completados
