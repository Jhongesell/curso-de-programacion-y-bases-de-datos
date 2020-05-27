import math

class complejo:
    def __init__(self, real, imaginario):
        self.real = real
        self.img = imaginario
    def abs(self):
        print(math.sqrt((self.real * self.real) + (self.img * self.img)))

def main():
    numero = complejo(3,4)

    print(numero.real)
    print(numero.img)

    numero.abs()

if __name__ == '__main__':
    main()
