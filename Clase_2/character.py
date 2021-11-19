""" Definición de la clase Character """
from magnitud_lineal import MagnitudLineal

class Character(MagnitudLineal):
    def __init__(self, character) -> None:
        self.__character = character
        
    @property
    def character(self): return self.__character
    
    # Metodo definido por la subclase
    def __eq__(self, character):
        return self.character == character
    
    # Metodo definido por la subclase
    def __lt__(self, character):
        return self.character < character