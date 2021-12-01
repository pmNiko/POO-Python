import unittest
from mi_fecha import MiFecha


class TestMiFecha(unittest.TestCase):
    def setUp(self):
        self._2_4_2020 = MiFecha(2, 4, 2020)

    # ---- Test una fecha es igual a otra fecha --------- #
    def test_unaFechaEsIgualAOtraFecha(self):
        _2_4_2020_bis = MiFecha(2, 4, 2020)

        self.assertTrue(self._2_4_2020 == _2_4_2020_bis)

    # ---- Test una fecha es menor que otra fecha --------- #

    def test_unaFechaEsMenorQueOtraFecha(self):
        _1_4_2020 = MiFecha(1, 4, 2020)

        self.assertTrue(_1_4_2020 < self._2_4_2020)

    # ---- Test una fecha no es menor que otra fecha --------- #

    def test_unaFechaNoEsMenorQueOtraFecha(self):
        _1_4_2020 = MiFecha(1, 4, 2020)

        self.assertFalse(self._2_4_2020 < _1_4_2020)

    # ---- Test una fecha es menor o igual a otra fecha --------- #

    def test_unaFechaEsMenorOIgualAOtraFecha(self):
        _1_4_2020 = MiFecha(1, 4, 2020)

        self.assertTrue(_1_4_2020 <= self._2_4_2020)

    # ---- Test una fecha es menor o igual a otra fecha segundo caso --------- #
    def test_unaFechaEsMenorOIgualAOtraFechaSegundoCaso(self):
        _2_4_2020_bis = MiFecha(2, 4, 2020)

        self.assertTrue(self._2_4_2020 <= _2_4_2020_bis)

    # ---- Test una fecha es mayor o igual a otra fecha--------- #
    def test_unaFechaEsMayorOIgualAOtraFecha(self):
        _1_4_2020 = MiFecha(1, 4, 2020)

        self.assertTrue(self._2_4_2020 >= _1_4_2020)

    # ---- Test una fecha es mayor o igual a otra fecha caso 2--------- #
    def test_unaFechaEsMayorOIgualAOtraFechaSegundoCaso(self):
        _2_4_2020_bis = MiFecha(2, 4, 2020)

        self.assertTrue(self._2_4_2020 >= _2_4_2020_bis)

    # ---- Test una fecha es mayor a otra fecha --------- #
    def test_unaFechaEsMayorAOtraFecha(self):
        _1_4_2020 = MiFecha(1, 4, 2020)

        self.assertTrue(self._2_4_2020 > _1_4_2020)

    # ---- Test una fecha se encuentra entre dos fechas --------- #

    def test_unaFechaEstaEntreDosFechas(self):
        _10_4_2020 = MiFecha(10, 4, 2020)
        _30_4_2020 = MiFecha(30, 4, 2020)

        self.assertTrue(_10_4_2020.entreDosFechas(self._2_4_2020, _30_4_2020))

    # ---- Test una fecha no se encuentra entre dos fechas --------- #

    def test_unaFechaNoEstaEntreDosFechas(self):
        _10_4_2020 = MiFecha(10, 4, 2020)
        _30_4_2020 = MiFecha(30, 4, 2020)

        self.assertFalse(self._2_4_2020.entreDosFechas(_10_4_2020, _30_4_2020))


if __name__ == "__main__":
    unittest.main()
