""" Definición de la superclaseclase abstracta CeuentaBancaria """

from abc import ABC, abstractmethod
from excepciones import ImposibleRealizarExtraccion


class CuentaBancaria(ABC):
    """ 
        Clase Abstracta CuentaBancaria
        
        Atributos:
            ✅ titular: nombre del titular de la cuenta
            ✅ saldo: saldo de la cuenta bancaria
        
        Metodos:
            📚 titular: guetter
            📚 saldo: guetter
            📚 depositar(un_monto): deposita un monto en la cuenta
            📚 puedeExtraer(un_monto): metodo abstracto
            📚 extraer(un_monto): metodo abstracto
    """
    def __init__(self, titular: str, saldo: float) -> None:
        self._titular = titular      # Convertimos las props en protected
        self._saldo = saldo
        
    
    @property
    def titular(self): return self._titular

    @property
    def saldo(self): return self._saldo
    
    # -------- Metodo público-------- #
    def depositar(self, un_monto: float) -> None: self._saldo += un_monto
    
    
    def extraer(self, un_monto: float) -> None: 
        """ Extrae un monto de la cuenta, sino debe arrojar la excepción: 
            -> ImposibleRealizarExtraccion('Imposible realizar la extracción.')"""
        if self.puedeExtraer(un_monto):
            self.realizarExtraccion(un_monto)
        else:
            raise ImposibleRealizarExtraccion('Imposible realizar la extracción.')
    
    # -------- Metodos abstractos-------- #
    @abstractmethod
    def puedeExtraer(self, un_monto: int) -> bool: 
        """ Devuelve true si se puede realizar la extracción """
        raise NotImplementedError
    
    
    @abstractmethod
    def realizarExtraccion(self, un_monto: float) -> None:
        """ La subclase sabe como debe realizar la extraccion de la cuenta """
        raise NotImplementedError