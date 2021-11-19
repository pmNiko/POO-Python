""" la clase Numero: 
   - (==, <, <=, >=, >)
   - esta entre "un_numero" y "otro_numero" """
from magnitud_lineal import MagnitudLineal

# class Numero(MagnitudLineal):


class Numero(object):

    def __init__(self, numero) -> None:
        self.__numero = numero

    @property
    def numero(self): return self.__numero

    # overloading del operador "=="
    def __eq__(self, numero) -> bool: return self.numero == numero.numero

    # overloading del operador "<"
    def __lt__(self, numero) -> bool: return self.numero < numero.numero

    # overloading del operador "<="
    def __le__(self, numero):
        return ((self < numero) or (self == numero))

    # overloading del operador ">="
    def __ge__(self, numero) -> bool: return not self < numero

    # overloading del operador ">"
    def __gt__(self, numero) -> bool: return not self <= numero

    def entreDosNumeros(self, numero_inicio, numero_fin) -> bool:
        return numero_inicio <= self and numero_fin >= self


if __name__ == '__main__':
    numero_1 = Numero(6)
    numero_1 = Numero(1)
    numero_5 = Numero(5)

    print(numero_1.en)
