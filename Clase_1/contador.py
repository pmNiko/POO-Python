""" Definamos una clase Contador 
    - Sabemos que un contador tiene un valor el cual ira acumulando 
    - Definamos dos metodos: 
        1- incrementar: incrementa el valor del contador 1 unidad
        2- decrementar: decrementa el valor del contador 1 unidad
"""


class Contador(object):
    """ La clase Contador sabe incrementar y decrementar su valor. """
    # atributo de la clase
    valor = 0

    # metodos de la clase Contador
    def incrementar(self) -> None:
        """ Incrementa en 1 el valor del contador y no recibe parametros. """
        self.valor = self.valor + 1
        # self.valor += 1

    def decrementar(self):
        """ Decrementa en 1 el valor del contador. """
        if self.valor > 0:
            self.valor = self.valor - 1
            # self.valor -= 1
        else:
            raise ValueError('Imposible decrementar el contador.')


if __name__ == "__main__":

    objeto_contador = Contador()  # Primero instanciamos la clase

    print(objeto_contador.valor)  # <= Verificamos su valor inicial

    # Accionamos el metodo para incrementar el valor del contador
    # objeto_contador.incrementar()
    # print(objeto_contador.valor)   # <= Verificamos su nuevo valor

    # # Accionamos el metodo para decrementar el valor del contador
    # objeto_contador.decrementar()
    # print(objeto_contador.valor)   # <= Verificamos su nuevo valor

    # try:
    #     objeto_contador.decrementar()
    # except ValueError as error:
    #     print(error)
