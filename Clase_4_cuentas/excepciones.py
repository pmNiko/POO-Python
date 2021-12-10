""" Definición de Excepciones personalizadas """

class ImposibleRealizarExtraccion(Exception):
        """ Excepción para definir que una extracción 
        no puede realizarse """
        pass
            


if __name__ == '__main__':
    try:
        raise ImposibleRealizarExtraccion({"mensaje":"Monto no disponible." })
    except ImposibleRealizarExtraccion as error:
        mensaje = error.args[0]
        print(mensaje["mensaje"])
    
    try:
        raise ImposibleRealizarExtraccion("Monto no disponible.")
    except ImposibleRealizarExtraccion as error:
        print(error)