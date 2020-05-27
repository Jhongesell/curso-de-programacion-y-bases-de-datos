class Animal:
    def __ini__(self):
        print("Animal creado")

    def quiensoy(self):
        print("Animal")

    def comer(self):
        print("Estoy comiendo")

class Perro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Perro creado")

    def quiensoy(self):
        print("Perro")

    def ladrar(self):
        print("Woof Woof Woof Woof!")

def main():
    d = Perro()
    d.quiensoy()
    d.comer()
    d.ladrar()
if __name__ == '__main__':
    main()
