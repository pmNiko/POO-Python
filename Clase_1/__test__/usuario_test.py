import unittest
from usuario import Usuario


class TestUsuario(unittest.TestCase):

    #  ----------- Test Validacion del password -------------- #
    def test_validarUnPasswordCorrecto(self):
        """ Validación de un password correcto """
        usuario = Usuario('Raul', 'superpassword', 'raul@gmail.com')

        self.assertTrue(usuario.validarPassword('superpassword'))

    #  ----------- Test Validacion de un password erroneo -------------- #
    def test_validarUnPasswordErroneo(self):
        """ Validación de un password incorrecto """
        usuario = Usuario('Raul', 'superpassword', 'raul@gmail.com')

        self.assertFalse(usuario.validarPassword('passwordIncorrecto'))

    #  ----------- Test Cambio de password -------------- #
    def test_CambioDePasswordConCredencialesCorrectas(self):
        """ Cambio de password - credenciales correctas """
        usuario = Usuario('Raul', 'superpassword', 'raul@gmail.com')  # setup

        self.assertTrue(usuario.validarPassword(
            'superpassword'))  # precondicion

        usuario.cambiarPassword(
            'superpassword', 'password1234')  # ejercitacion

        self.assertTrue(usuario.validarPassword(
            'password1234'))  # objetivo

    #  ----------- Test Error en el Cambio de password -------------- #
    def test_CambioDePasswordConCredencialesErroneas(self):
        """ Cambio de password - credenciales erroneas """
        usuario = Usuario('Raul', 'superpassword', 'raul@gmail.com')  # setup

        self.assertTrue(usuario.validarPassword(
            'superpassword'))  # precondicion

        with self.assertRaisesRegex(ValueError, 'Sus credenciales no son validas.'):
            usuario.cambiarPassword(
                'passwordIncorrecto', 'password1234')  # ejercitacion

        self.assertTrue(usuario.validarPassword(
            'superpassword'))  # post condicion
