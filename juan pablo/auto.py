

class Auto(object):
    def __init__(self) -> None:
        self.__velocidad = 0 

    @property
    def velocidad(self) -> None: return self.__velocidad

    def acelerar(self, una_velocidad: int) -> None:
        """ velocidad no negativa """
        if una_velocidad > 0 :
            self.__velocidad += una_velocidad
        else: raise ValueError('La velocidad no puede ser negativa')

    def detenerse(self): self.__velocidad = 0

    def estaEnMovimiento(self) -> bool:
        """ Devuelve true si el auto esta en movimiento """
        return self.velocidad > 0


if __name__ == '__main__':
    auto = Auto()

    auto.acelerar = 100 
    print(auto.velocidad)