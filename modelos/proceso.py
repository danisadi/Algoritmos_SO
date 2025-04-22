class Proceso:
    def __init__(self, nombre, llegada, duracion, prioridad=0):
        self.nombre = nombre
        self.llegada = llegada
        self.duracion = duracion
        self.prioridad = prioridad
        self.inicio = 0
        self.final = 0
        self.espera = 0
        self.retorno = 0
        self.restante = duracion
