""" Ejercicio:
      Clases:
         Suma
         Reata
         Multiplicacion
         Division

      Clase Abstracta OperacionMatematica
        metodo abstracto:
            👉🏻 operar() 
        metodo concreto:
            👉🏻 restablecer() 
            

"""

from abc import ABC, abstractmethod


class OperacionMatematica(ABC):
    def __init__(self) -> None:
        self._resultado = 0

    @property
    def resultado(self): return self._resultado

    def restablecer(self): self._resultado = 0

    @abstractmethod
    def operar():
        """ Debe definir como opera la subclase """
        pass


class Suma(OperacionMatematica):
    def operar(self, sumando1, sumando2):
        self._resultado = sumando1 + sumando2


class Resta(OperacionMatematica):
    def operar(self, minuendo, sustraendo):
        self._resultado = minuendo - sustraendo


class Division(OperacionMatematica):
    def operar(self, dividendo, divisor):
        if divisor == 0:
            raise ZeroDivisionError('No se puede divdir por 0.')
        else:
            self._resultado = dividendo / divisor


class Multiplicacion(OperacionMatematica):
    def operar(self, multiplicando, multiplicador):
        self._resultado = multiplicando * multiplicador
