""" Definición de la clase Animal """


class Animal(object):
    def __init__(self, especie, cantidad_de_patas, sonido):
        self.__especie = especie
        self.__sonido = sonido
        self.__patas = cantidad_de_patas

    @property
    def especie(self): return self.__especie
    @property
    def patas(self): return self.__patas
    @property
    def sonido(self): return self.__sonido

    def datos(self):
        return f"Soy {self.especie} tengo {self.patas} patas y hago {self.sonido}."


if __name__ == '__main__':
    gato = Animal("gato", 4, "miau")
    print(gato.datos())
