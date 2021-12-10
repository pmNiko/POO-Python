""" Definición de la clase CuentaCorriente """
from cuentaBancaria import CuentaBancaria
from excepciones import ImposibleRealizarExtraccion

class CuentaCorriente(CuentaBancaria):
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
        super().__init__(titular, saldo)
        self.__descubiertoMaximo = descubiertoMaximo
    
    @property
    def descubiertoMaximo(self): return self.__descubiertoMaximo

    # -------- Metodos de la clase -------- #    
    def puedeExtraer(self, un_monto: int) -> bool:
        """ Devuelve true si se puede realizar la extracción """
        return un_monto <= self.saldo + self.descubiertoMaximo  
            
    
    def realizarExtraccion(self, un_monto: float) -> None:
        self._saldo -= un_monto

    # def extraer(self, un_monto: float):
    #     """ Extrae un monto de la cuenta, sino arroja la excepción: 
    #         -> ImposibleRealizarExtraccion('Imposible realizar la extracción.')"""
    #     if self.puedeExtraer(un_monto):
    #         self._saldo -= un_monto
    #     else:
    #         raise ImposibleRealizarExtraccion('Imposible realizar la extracción.')


if __name__ == "__main__":
    pass
