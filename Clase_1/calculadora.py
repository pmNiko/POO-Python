""" Definición de la clase calculadora 
    - La calculadora tendra un resultado el cual iniciara en 0
    - Se reestablecerá a traves del metodo borrar
    - Debe poder realizar las operaciones básicas:
       sumar(sumando_1, sumando_2)
       restar(minuendo, sustraendo)
       multiplicar(multiplicando, multiplicador)
       dividir(dividendo, divisor)
       
"""


class Calculadora(object):
    """ Clase Calculadora  """

    __resultado = 0  # propiedad privada

    @property
    def resultado(self): return self.__resultado  # Guetter

    @resultado.setter
    def resultado(self, valor): self.__resultado = valor  # Setter

    # ------ Metodos de la clase ------- #
    def sumar(self, sumando1, sumando2):
        """ Metodo que realiza la suma y setea el valor de la calculadora. """
        self.resultado = sumando1 + sumando2

    def restar(self, minuendo, sustraendo):
        """ Metodo que realiza la resta y setea el valor de la calculadora. """
        self.resultado = minuendo - sustraendo

    def multiplicar(self, multiplicando, multiplicador):
        """ Metodo que realiza la multiplicacion y setea el valor de la calculadora. """
        self.resultado = multiplicando * multiplicador

    def dividir(self, dividendo, divisor):
        """ Metodo que realiza la division y setea el valor de la calculadora. """
        self.resultado = dividendo / divisor

    def borrar(self):
        """ Metodo que restaura la calculadora. """
        self.resultado = 0


if __name__ == "__main__":
    calculadora = Calculadora()

    print(calculadora.resultado)

    calculadora.sumar(2, 4)

    print(calculadora.resultado)

    calculadora.borrar()
    print(calculadora.resultado)

    calculadora.__resultado = 9
    print(calculadora.resultado)
