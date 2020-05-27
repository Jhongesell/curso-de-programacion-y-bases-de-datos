import math

class complejo:
    def __init__(self, real, imaginario):
        self.real = real
        self.img = imaginario

    def abs(self):
        print(math.sqrt((self.real * self.real) + (self.img * self.img)))

    def __add__(self, otro):
        return complejo(self.real + otro.real, self.img + otro.img)

    def __sub__(self, otro):
        return complejo(self.real - otro.real, self.img - otro.img)

    def mostrar(self):
        print(self.real)
        print(self.img)

def main():
    complejo1 = complejo(3,4)
    complejo2 = complejo(3,4)
    complejo3 = complejo1 + complejo2
    complejo4 = complejo1 - complejo2
    complejo3.mostrar()
    complejo4.mostrar()


print("Este es un texto de prueba")
if __name__ == '__main__':
    main()

print(type(main()))
print("-------")
