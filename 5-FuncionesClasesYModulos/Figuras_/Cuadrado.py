from Figura import Figura

class Cuadrado(Figura):
    def __init__(self, lado):
        self.__lado = lado
        super().__init__("Circulo")

    def calcular_area(self):
        return self.__lado ** 2
        
    def calcular_perimetro(self):
        return 4 * self.__lado
