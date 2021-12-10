""" Definición de la clase CajaDeAhorro """
from cuentaBancaria import CuentaBancaria
from excepciones import ImposibleRealizarExtraccion

class CajaDeAhorro(CuentaBancaria):
    """ Clase CajaDeAhorro

        Atributos:
            titular: Nombre del titular de la cuenta.
            saldo: Saldo con el que se crea la caja de ahorro.
            extracciones: cantidad de extracciones mensuales permitidas.
            
        Metodos:
            depositar: permite depositar unmonto en la cuenta.
            puedeExtraer: responde si es posible retirar un monto.
            extraer: extrae un monto de la cuenta, si no es posible arroja una excepción.
            reastaurarEtracciones: restaura la cantidad de extracciones mensuales.
    """
    def __init__(self, titular: str, saldo: float, extracciones_posibles: int) -> None:
        super().__init__(titular, saldo)
        self.__extraccionesPosibles = extracciones_posibles
        self.__extraccionesRealizadas = 0
   
    @property
    def extraccionesPosibles(self): return self.__extraccionesPosibles
    @property
    def extraccionesRealizadas(self): return self.__extraccionesRealizadas

    # -------- Metodos de la clase -------- #
    
    def puedeExtraer(self, un_monto: int) -> bool:
        """ Devuelve true si se puede realizar la extracción """
        return (
            un_monto <= self.saldo 
            and 
            self.extraccionesRealizadas < self.extraccionesPosibles
            )

    # def extraer(self, un_monto: float):
    #     """ Extrae un monto de la cuenta, sino arroja la excepción: 
    #         -> ImposibleRealizarExtraccion('Imposible realizar la extracción.')"""
    #     if self.puedeExtraer(un_monto):
    #         self._saldo -= un_monto
    #         self.__extraccionesRealizadas += 1
    #     else:
    #         raise ImposibleRealizarExtraccion('Imposible realizar la extracción.')
    
    def realizarExtraccion(self, un_monto: float) -> None:
        self._saldo -= un_monto
        self.__extraccionesRealizadas += 1
        
    def restaurarExtraciones(self) -> None:
        """ Reataura la cantidad de extraciones """
        self.__extraccionesRealizadas = 0
        
        

if __name__ == "__main__":
    pass
