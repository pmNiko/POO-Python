"""
    Ejercicio 2:
        Modelar el objeto fecha en donde tendra:
            - un dia 
            - un mes 
            - un anio 
        
        y debera poder compararse con otra fecha:
            - (==, <, <=, >=, >)
            - esta entre "una_fecha" y "otra_fecha"

        Realizar los test necesarios que validen 
        el comportamiento.  
"""


class Fecha(object):
    __dia = 0
    __mes = 1
    __anio = 2

    @property
    def dia(self): return self.__dia
    @property
    def mes(self): return self.__mes
    @property
    def anio(self): return self.__anio



    def setearFecha(self, dia: int, mes: int, anio: int) -> None:
        self.dia = dia
        self.mes = mes
        self.anio = anio

    # def esIgual(self, una_fecha: 'Fecha') -> bool:
    #     return una_fecha == Fecha



















    # def __init__(self, dia:int , mes:int , anio:int  ) -> None:
    #     self.__dia = dia
    #     self.__mes = mes
    #     self.__anio = anio

    # def setearUnaFecha(self, dia:int, mes:int, anio:int ) -> None:
    #     self.dia = dia
    #     self.mes = mes
    #     self.anio = anio
    

    

    # def fechasIguales(self, fecha: 'Fecha') -> bool:
    #     return fecha == pass






















        
        




if __name__ == '__main__':  

    fecha_seteada = Fecha()

    # fecha_seteada.setearUnaFecha(20, 3, 2001)

    # print(fecha_seteada.esIgual(20, 3, 2001))
    
  





   
    

    

