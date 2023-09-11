class Casilla:
    def __init__(self,fila,columna,color):
        self.fila = fila 
        self.columna = columna
        self.color = color 

class NodoCasilla:
    def __init__(self,casilla = None, siguiente= None):
        self.casilla = casilla
        self.siguiente = siguiente
        
