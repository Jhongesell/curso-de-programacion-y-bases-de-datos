class figura:
    def __init__(self, lados = 0, longitud_lado = 0.0, apotema = 0.0):
        self.lado = lados
        self.long = longitud_lado
        self.__apotema = apotema
        self.__perimetro = self.lado * self.long

    def __area(self):
        return ((self.__apotema * self.__perimetro) / 2 )

    def imprimir(self):
        a = self.__area()
        print(a)

def main():
    triangulo = figura(2,3,1.5)
    print(triangulo.lado)
    print(triangulo.long)

    triangulo.imprimir()
if __name__ == '__main__':
    main()
