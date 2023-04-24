class Personaje:
    def __init__(self, nombre, salud, ataque, defensa):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque
        self.defensa = defensa

    def recibir_dano(self, dano):
        self.salud = max(0, self.salud - dano)

    def atacar(self, personaje):
        dano = max(0, self.ataque - personaje.defensa)
        personaje.recibir_dano(dano)
        return dano

    def morir(self):
        print(f'{self.nombre} ha muerto.')

class Enemigo(Personaje):
    def __init__(self, nombre, salud, ataque, defensa, recompensa):
        super().__init__(nombre, salud, ataque, defensa)
        self.recompensa = recompensa

    def atacar(self, personaje):
        dano = max(0, self.ataque - personaje.defensa)
        personaje.recibir_dano(dano)
        print(f'{self.nombre} atacó a {personaje.nombre} y le hizo {dano} de daño.')
        if personaje.salud == 0:
            personaje.morir()
            return self.recompensa

    def morir(self):
        print(f'{self.nombre} ha sido derrotado.')
        return self.recompensa

class Jugador(Personaje):
    def __init__(self, nombre, salud, ataque, defensa, inventario=[]):
        super().__init__(nombre, salud, ataque, defensa)
        self.inventario = inventario

    def usar_item(self, item):
        if item in self.inventario:
            self.inventario.remove(item)
            item.usar(self)

class Zombie(Enemigo):
    def __init__(self, nombre='Zombie', salud=100, ataque=10, defensa=5, recompensa=10):
        super().__init__(nombre, salud, ataque, defensa, recompensa)
    

class Perro(Enemigo):
    def __init__(self, nombre='Perro', salud=80, ataque=20, defensa=10, recompensa=20):
        super().__init__(nombre, salud, ataque, defensa, recompensa)

class Boss(Enemigo):
    def __init__(self, nombre, salud, ataque, defensa, recompensa):
        super().__init__(nombre, salud, ataque, defensa, recompensa)

class Item:
    def __init__(self, nombre, efecto):
        self.nombre = nombre
        self.efecto = efecto

    def usar(self, personaje):
        pass

class Botiquin(Item):
    def __init__(self):
        super().__init__('Botiquin', 'restaura 20 puntos de salud')

    def usar(self, personaje):
        personaje.salud = min(personaje.salud + 20, 100)

class Arma(Item):
    def __init__(self, nombre, ataque):
        super().__init__(nombre, f'aumenta el ataque en {ataque} puntos')
        self._ataque = ataque            #Protegido _ (Solo una barra baja)
        self.__vigencia = 100            #Privado   __ (doble barra baja)

    def __usarInternamente(self, personaje):   #Privado  __ (doble barra baja)
        personaje.ataque += self.ataque
        
    def usar(self, personaje):
    	personaje.ataque += self.ataque

class Pistola(Arma):
    def __init__(self):
        super().__init__('Pistola', 20)

class Escopeta(Arma):
    def __init__(self):
        super().__init__('Escopeta', 30)


# implementado el polimorfismo objetos de diferenets classes que responden diferente a la llamada
# del mismo metodo o funcion
def comportamiento(enemigo,jugador):
    enemigo.atacar(jugador)
    enemigo.morir()

if __name__ == "__main__":

    jugador1 = Jugador("Billy",200,100,50)
    #Crear enemigos
    zombie1 = Zombie()
    perro1 = Perro()
    boos1 = Boss("jefe1",50,10,20,50)

    comportamiento(zombie1,jugador1)
    comportamiento(perro1,jugador1)
    comportamiento(boos1,jugador1)