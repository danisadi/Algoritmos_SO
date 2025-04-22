def fcfs(procesos):
    procesos.sort(key=lambda p: p.llegada)
    tiempo = 0
    for p in procesos:
        if tiempo < p.llegada:
            tiempo = p.llegada
        p.inicio = tiempo
        p.final = tiempo + p.duracion
        p.espera = p.inicio - p.llegada
        p.retorno = p.final - p.llegada
        tiempo = p.final
    return procesos
