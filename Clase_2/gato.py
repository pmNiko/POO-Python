from animal import Animal


class Gato(Animal):
    pass

class Perro(Animal):
    pass


if __name__ == '__main__':
    gato = Gato("gato", 4, "miau")
    perro = Perro("perro", 4, "guau")
    
    print(gato.datos())
    
    print(perro.datos())
