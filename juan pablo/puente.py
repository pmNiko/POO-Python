from valla import Valla 
from auto import Auto

class Puente(object):
    def __init__(self, un_numero: int) -> None:
        self.__numero = un_numero
        self.__valla = Valla()
        self.__auto = Auto()


    @property
    def numero(self): return self.__numero

    def laVallaEstaAlta(self) -> bool:
        """ Retorna true si la valla esta alta """
        return self.__valla.alta
    
    def bajarLaValla(self) -> None:
        """ El puente baja la valla cuando esta alta """
        if self.laVallaEstaAlta(): self.__valla.cambiarEstado()

    def subirLaValla(self) -> None:
        """ El puente sube la valla cuando esta baja """
        if not self.laVallaEstaAlta(): self.__valla.cambiarEstado()

    def vallaPuenteAlta(self) -> None:
        """ Si la valla del puente esta alta los autos pueden circular 
        a una velocidad de 40km/h """

        if self.laVallaEstaAlta(): self.__auto.acelerar(40)

    def vallaPuenteBaja(self):
        """ Si la valla del puente esta baja los autos deben detenerse"""

        if not self.laVallaEstaAlta(): self.__auto.detenerse()
