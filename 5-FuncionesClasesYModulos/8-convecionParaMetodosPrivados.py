class Vehiculo():
    #Metodo _privado
    def __privado(self):
        print("soy privado") #utiliza esto solo dentro de la clase
    def metodo_publico(self):
        print("Soy un metodo público") #utilizado fuera y dentro de la clase

g1 = Vehiculo()
#g1.__privado()
g1._Vehiculo__privado()
g1.metodo_publico()