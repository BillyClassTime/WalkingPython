class Figura:
    def dibujar(self,nombre):
        print(f'Dibujando un:{nombre}')
class Triangulo(Figura):
    def __init__(self,nombre):
        self.nombre = nombre
class Rectangulo(Figura):
    def __init__(self,nombre):
        self.nombre = nombre
class Cuadrado(Figura):
    def __init__(self,nombre):
        self.nombre = nombre
def DibujarFigura(figura):
    figura.dibujar(figura.nombre)
triangulo = Triangulo('Triangulo verde')
cuadrado = Cuadrado('Cuadrado rojo')
rectangulo = Rectangulo('Rectangulo amarillo')
DibujarFigura(triangulo)
DibujarFigura(cuadrado)
DibujarFigura(rectangulo)