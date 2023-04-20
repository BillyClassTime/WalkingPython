from Circulo import Circulo
from Cuadrado import Cuadrado
from Triangulo import Triangulo
from Pentagono import Pentagono

def procesarFigura(figura): #SOLO FAMILIA DE FIGURA, pero Python no obliga por no tener tipo rigidos
    area=figura.calcular_area()
    perimetro=figura.calcular_perimetro()
    salida = f"La figura es{figura}, su area es:{area} y su perimetro es:{perimetro}"
    print(salida)

def principal():
    circulo1 = Circulo(2)        #Creamos el objeto circulo1 CONDICION
    cuadrado1 = Cuadrado(2)      #Creamos el objeto cuadrado1
    triangulo1 = Triangulo(4,2)  #Creamos el objeto triangulo1
    pentagono1 = Pentagono()     #Creamos el objeto pentagono1 #no es puramente POO 

    procesarFigura(circulo1)     #__init__ NO ES PURAMENTE POO
    procesarFigura(cuadrado1)
    procesarFigura(triangulo1)
    procesarFigura(pentagono1)

    #print(circulo1.radio)      #No se puede acceder a radio, esta encapsulado (es privado en la clase círculo)
    print(circulo1)
    #print(cuadrado1.lado)       #No se puede acceder a lado, esta encapsulado (es privado en la clase cuadrado)
    print(cuadrado1)

if __name__ == "__main__":
    principal()