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