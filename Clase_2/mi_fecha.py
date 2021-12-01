""" Definición de la Clase MiFecha """
from magnitud_lineal import MagnitudLineal

# class MiFecha(MagnitudLineal):


class MiFecha(object):
    def __init__(self, un_dia, un_mes, un_anio) -> None:
        self.__dia = un_dia
        self.__mes = un_mes
        self.__anio = un_anio

    @property
    def dia(self): return self.__dia
    @property
    def mes(self): return self.__mes
    @property
    def anio(self): return self.__anio

    # Overloading del operador "=="
    def __eq__(self, una_fecha):
        return (
            self.anio == una_fecha.anio and
            self.mes == una_fecha.mes and
            self.dia == una_fecha.dia
        )

    # Overloading del operador "<"
    def __lt__(self, una_fecha):
        return (
            (self.anio < una_fecha.anio)
            or
            (
                self.anio == una_fecha.anio and
                self.mes < una_fecha.mes
            )
            or
            (
                self.anio == una_fecha.anio and
                self.mes == una_fecha.mes and
                self.dia < una_fecha.dia
            )
        )

    # Overloading del operador "<="
    def __le__(self, una_fecha):
        return (
            (self < una_fecha)
            or
            (
                self == una_fecha
            )
        )

    # Overloading del operador ">="
    def __ge__(self, una_fecha):
        return not self < una_fecha

    # Overloading del operador ">"
    def __gt__(self, una_fecha):
        return not self <= una_fecha

    def entreDosFechas(self, fecha_inicio, fecha_fin):
        # return super().entre(fecha_inicio, fecha_fin)
        return fecha_inicio <= self and fecha_fin >= self


if __name__ == "__main__":
    _1_4_2020 = MiFecha(1, 4, 2020)
    _10_4_2020 = MiFecha(10, 4, 2020)
    _30_4_2020 = MiFecha(30, 4, 2020)

    respuesta = _1_4_2020 <= _10_4_2020

    print(respuesta)
