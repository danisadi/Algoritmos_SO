def fcfs(procesos):
    procesos.sort(key=lambda p: p.llegada)

    tiempo = 0
    for p in procesos:
        p.espera = max(0, tiempo - p.inicio)
        p.retorno  = p.espera + p.duracion
        tiempo += p.duracion
    
    prom_espera = sum(p.espera for p in procesos) / len(procesos)
    prom_retorno = sum(p.retorno for p in procesos) / len(procesos)
    
    print(f"\nTiempo medio de espera: {prom_espera:.2f}")
    print(f"Tiempo medio de retorno: {prom_retorno:.2f}")
    

    return procesos
