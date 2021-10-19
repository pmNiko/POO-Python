""" Modelemos la clase MagnitudLineal 

   Protocolo:
      👉🏻 <= otra_magnitud   # metodo concreto
      👉🏻 > otra_magnitud    # metodo concreto
      👉🏻 >= otra_magnitud   # metodo concreto
      👉🏻 entreDosMagnitudes(una_magnitud, otra_magnitud)   # metodo concreto


      👉🏻 == otra_magnitud    # metodo abstracto
      👉🏻 <  otra_magnitud    # metodo abstracto """
      
from abc import ABC, abstractmethod

class MagnitudLineal(ABC):
    """ Clase abstracta: 
        - Metodos concretos: <=, >=, >, entre
        - Metodos abstractos: == , < """
    # Overloading del operador "<="
    def __le__(self, una_magnitud):
        return ( 
                    (   self <  una_magnitud ) 
                    or 
                    ( 
                        self == una_magnitud
                    ) 
                )
        
    # Overloading del operador ">="
    def __ge__(self, una_magnitud):
        return not self <  una_magnitud 
    
    # Overloading del operador ">"
    def __gt__(self, una_magnitud):
        return not  self <=  una_magnitud 
    
    def entre(self, magnitud_inicio, magnitud_fin):
        """ Devuelve un booleano si se encuentra entre
            dos magnitudes que recibe como parametro."""
        return magnitud_inicio <= self and magnitud_fin >= self
    
    # Overloading del operador "=="
    @abstractmethod
    def __eq__(self, una_magnitud): pass
    
    # Overloading del operador "<"
    @abstractmethod
    def __lt__(self, una_magnitud): raise NotImplementedError