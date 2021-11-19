""" Definición de la clase CuentaCorriente """
# from cuenta_bancaria import CuentaBancaria
from excepciones import ImposibleRealizarExtraccion

class CuentaCorriente(object):
    """ Clase CuentaCorriente

        Atributos:
            titular: Nombre del titular de la cuenta.
            saldo: Saldo con el que se crea la caja de ahorro.
            descuebiertoMaximo: representa el monto maximo en descubierto de la cuenta.
            
        Metodos:
            depositar: permite depositar unmonto en la cuenta.
            puedeExtraer: responde si es posible retirar un monto.
            extraer: extrae un monto de la cuenta, si no es posible arroja una excepción.
    """
    def __init__(self, titular: str, saldo: float, descubiertoMaximo: float) -> None:
        self.__titular = titular
        self.__saldo = saldo
        self.__descubiertoMaximo = descubiertoMaximo
    # def __init__(self, titular: str, saldo: float, descubiertoMaximo: float) -> None:
    #     CuentaBancaria.__init__(self, titular, saldo)
    #     self.__descubiertoMaximo = descubiertoMaximo

    @property
    def titular(self): return self.__titular

    @property
    def saldo(self): return self.__saldo
    
    @property
    def descubiertoMaximo(self): return self.__descubiertoMaximo

    # -------- Metodos de la clase -------- #
    def depositar(self, un_monto: float) -> None: self.__saldo += un_monto
    
    def puedeExtraer(self, un_monto: int) -> bool:
        """ Devuelve true si se puede realizar la extracción """
        return un_monto <= self.saldo + self.descubiertoMaximo  
            

    def extraer(self, un_monto: float):
        """ Extrae un monto de la cuenta, sino arroja la excepción: 
            -> ImposibleRealizarExtraccion('Imposible realizar la extracción.')"""
        if self.puedeExtraer(un_monto):
            self.__saldo -= un_monto
            # self._saldo -= un_monto
        else:
            raise ImposibleRealizarExtraccion('Imposible realizar la extracción.')


if __name__ == "__main__":
    pass
