""" Definicion de la clase Usuario
    - El usuario consta de un nick, password y un email
    - Y contará con un metodo para cambiar el password y otro 
      para validar el password
"""


class Usuario(object):
    def __init__(self, nick, password, email) -> None:
        self.__nick = nick
        self.__password = password
        self.__email = email

    @property
    def nick(self): return self.__nick

    @property
    def email(self): return self.__email

    @property
    def password(self): return self.__password

    # ----- Metodos de la clase ----- #

    def validarPassword(self, un_password) -> bool:
        """ Metodo encargado de validar el password """
        return self.password == un_password

    def cambiarPassword(self, su_password, nuevo_password):
        """ Metodo encargado de cambiar el password """
        if self.validarPassword(su_password):
            self.__password = nuevo_password
        else:
            raise ValueError('Sus credenciales no son validas.')
        


if __name__ == '__main__':
    
    usuario = Usuario("Niko", "1234", "niko@gmail")
  
    
    print(usuario.password)
    
    usuario.cambiarPassword("1234", "superpass")
    
    print(usuario.password)
    
    respuesta = usuario.validarPassword("1234")
    
    print(respuesta)
    
    

    