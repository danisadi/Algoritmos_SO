def sjf(procesos):
    procesos.sort(key=lambda p: (p.llegada, p.duracion))
    completados = []
    tiempo = 0
    while procesos:
        disponibles = [p for p in procesos if p.llegada <= tiempo]
        if disponibles:
            actual = min(disponibles, key=lambda p: p.duracion)
            procesos.remove(actual)
            actual.inicio = tiempo
            actual.final = tiempo + actual.duracion
            actual.espera = actual.inicio - actual.llegada
            actual.retorno = actual.final - actual.llegada
            tiempo = actual.final
            completados.append(actual)
        else:
            tiempo += 1
    return completados
