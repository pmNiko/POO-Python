from animal import Animal


class Gato(Animal):
    pass


if __name__ == '__main__':
    gato = Gato("gato", 4, "miau")
    print(gato.datos())
