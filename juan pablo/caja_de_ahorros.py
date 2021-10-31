"""
    Ejercicio 1:
        Modelar el objeto caja de ahorro:
            - un titular
            - un saldo
        
        y debera poder:
            - depositar un monto
            - puedeExtraer un monto
            - extraer un monto
            - en el caso de querer extraer un monto superior 
              al monto disponible arrojara una 
              excepcion ValueError("Imposible realizar extracción.")

        Realizar los test necesarios que validen 
        el comportamiento.  
"""


class CajaDeAhorro(object):
    def __init__(self, titular, saldo) -> None:  
        self.__titular = titular
        self.__saldo = saldo  

    @property
    def titular(self): return self.__titular

    # @titular.setter
    # def titular(self, un_nombre): self.__titular = un_nombre
    
    @property
    def saldo(self): return self.__saldo 

    # @saldo.setter
    # def saldo(self, valor): self.__saldo = valor

    

    def depositarMonto(self, monto: int) -> None:
        """ Deposita monto ingresado a la caja de ahorros """        
        self.__saldo += monto

    def extraerUnMonto(self, monto: int) -> None:
        """ Extrae un monto de la caja de ahorros """
        if self.puedeExtraer(monto):
            self.__saldo -= monto
        else:
            raise ValueError("Imposible realizar extracción.")
        

    def puedeExtraer(self, monto: int) -> bool:
        """ Responde true si se puede extraer un monto """
        return  monto <= self.saldo



if __name__ == '__main__':
    caja_de_ahorro = CajaDeAhorro(100, 'Juampi')

    # caja_de_ahorro.titular = "juan pablo"

    print(caja_de_ahorro.titular)
    
    # caja_de_ahorro.titular = "martin"
    # print(caja_de_ahorro.titular)
    # caja_de_ahorro.depositarMonto(120)

    print(caja_de_ahorro.saldo)

    # caja_de_ahorro.extraerUnMonto(110)

    # print(caja_de_ahorro.saldo)

    # try:
    #     caja_de_ahorro.extraerUnMonto(20)
    # except ValueError as error:
    #     print(error)



    # print(caja_de_ahorro.saldo)

    # caja_de_ahorro.saldo = -1000    
    
    # print(caja_de_ahorro.saldo)

    
    