from Figura import Figura
from math import pi
class Circulo(Figura):
    def __init__(self,radio):
        self.__radio = radio
        super().__init__("Circulo")
        
    def calcular_area(self):
        return self.__piC() * self.__radio ** 2
        
    def calcular_perimetro(self):
        return 2 * self.__piC() * self.__radio
    
    def __piC(self):
        return pi