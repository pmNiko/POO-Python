class Valla(object):
    def __init__(self) -> None:
        self.__alta = True

    @property
    def alta(self): return self.__alta

    def cambiarEstado(self) -> None:
        """ Invierte el estado de la valla  """
        self.__alta = not self.alta