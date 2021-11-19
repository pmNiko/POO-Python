import unittest
from character import Character


class TestCharacter(unittest.TestCase):
    def setUp(self) -> None:
        self.character_A = Character('A')
        self.character_Z = Character('Z')

    def test_ElCharacterAEsIgualA_A(self):
        """ El caracter A es igual a A """
        A = Character('A')

        self.assertTrue(self.character_A == A)

    def test_ElCharacterANoEsIgualA_B(self):
        """ El caracter A es igual a A """
        B = Character('B')

        self.assertFalse(self.character_A == B)

    def test_ElCharacterAEsMenorA_Z(self):
        """ El caracter A es menor a Z """
        self.assertTrue(self.character_A < self.character_Z)

    def test_ElCharacterZNoEsMenorA_A(self):
        """ El caracter Z no es menor a A """
        self.assertFalse(self.character_Z < self.character_A)

    def test_ElCharacterAEsMenorOIgualA_Z(self):
        """ El caracter A es menor o igual a Z """
        self.assertTrue(self.character_A <= self.character_Z)

    def test_ElCharacterZEsMayorOIgualA_A(self):
        """ El caracter Z es mayor o igual a A """
        self.assertTrue(self.character_Z >= self.character_A)

    def test_ElCharacterFEstaEntreDosCaracteres(self):
        """ El caracter F esta entre dos caracteres """
        F = Character('F')

        self.assertTrue(F.entre(self.character_A, self.character_Z))

    def test_ElCharacterZEstaFueraDeRango(self):
        """ El caracter Z esta fuera de rango """
        F = Character('F')

        self.assertFalse(self.character_Z.entre(self.character_A, F))
