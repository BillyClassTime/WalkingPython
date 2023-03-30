def ProcesoInicial():
    print('Buscar una hoja de papel')

def ProcesoDos():
    print('Doblar la hoja')

def SaludarATodos(*nombres):
    for i in nombres:
        print(f'hola:{i}')

def SaludarATodosDict(**nombres):
    for i in nombres:
        print(f'hola:{i} {nombres[i]}')

def Ciudades(Pais,ciudad='Oslo'):
    print(Pais,'',ciudad)

ProcesoInicial()
ProcesoDos()
colores=['azul','rojo','amarillo']
SaludarATodos('Olga')
SaludarATodos('Rafaela','Carla','Pedro')
SaludarATodos('Diego','Cynthia','Alvavro','Emiliano')
SaludarATodos()
SaludarATodos(345,'Miryam',True)
SaludarATodos(colores,'Helga')

SaludarATodosDict(nombre="Billy",apellidos='Vanegas')

Ciudades('Colombia','Bogotá')
Ciudades('Mexico','Ciudad de Mexico')
Ciudades('Noruega')
