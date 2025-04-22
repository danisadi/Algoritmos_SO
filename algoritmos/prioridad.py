def prioridades(procesos):
    procesos.sort(key=lambda p: (p.llegada, p.prioridad))
    completados = []
    tiempo = 0
    while procesos:
        disponibles = [p for p in procesos if p.llegada <= tiempo]
        if disponibles:
            actual = min(disponibles, key=lambda p: p.prioridad)
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
