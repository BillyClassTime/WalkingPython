from Figura import Figura

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura
        super().__init__("Triangulo")

    def calcular_area(self):
        return self.__base * self.__altura / 2
        
    def calcular_perimetro(self):
        return self.__base + 2 * (self.__altura ** 2 + self.__base ** 2) ** 0.5
    
   